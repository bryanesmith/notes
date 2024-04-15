# DeepLearning.AI Short Course: Efficiently Serving LLMs

Started course: 2024/04/13
Taught by: Travis Addair, CTO of Predibase and lead maintainer of Horovod

## Summary

* This course covered:
    1. KV caching (prefill vs decode)
    2. Continuous batching
    3. Quantization
    4. Multi-LoRA (fine-tuned model inference)

* **Predibase**: deploy serverless, cost-effective, open source, fine-tuned LLMs

* **LoRAX**: open source, dynamically servers hundreds of  LLMs on single GPU

## 1. Introduction

## 2. Text Generation

* **Autoregressive language models** uses pass values of time series to predict future values, predicting the next word in a sequence of words

* Running inference on a LLM with PyTorch and **Hugging Face Transformers** is straightforward:
    ```py
    import matplotlib.pyplot as plt
    import numpy as np
    import time
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    model_name = "./models/gpt2"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    def generate_token(inputs):
        with torch.no_grad():
            outputs = model(**inputs)

            logits = outputs.logits
            last_logits = logits[0, -1, :]
            next_token_id = last_logits.argmax()
            return next_token_id
    
    generated_tokens = []
    prompt = "The quick brown fox jumped over the"
    next_inputs = tokenizer(prompt, return_tensors="pt")
    for _ in range(10):
        next_token_id = generate_token(next_inputs)
        
        next_inputs = {
            "input_ids": torch.cat(
                [next_inputs["input_ids"], next_token_id.reshape((1, 1))],
                dim=1),
            "attention_mask": torch.cat(
                [next_inputs["attention_mask"], torch.tensor([[1]])],
                dim=1),
        }
        
        next_token = tokenizer.decode(next_token_id)
        generated_tokens.append(next_token)

    print(f"{sum(durations_s)} s")
    print(generated_tokens)
    ```

* `torch.no_grad` disables gradient calculation and is used during inference

* ChatGPT 2 isn't state-of-the-art, but it is still useful as it has fewer parameters and hence inference is faster

* **KV-caching** (**key-value caching**) is a technique to speed up token generation by storing some tensors in the attention head for use in subsequent generation steps
    ```py
    # modify generate_token to return outputs.past_key_values
    def generate_token_with_past(inputs):
        with torch.no_grad():
            outputs = model(**inputs)

            logits = outputs.logits
            last_logits = logits[0, -1, :]
            next_token_id = last_logits.argmax()
            return next_token_id, outputs.past_key_values
    
    # ...

    # we're passing in the kv-cache via next_inputs "past_key_values"
    next_inputs = {
        "input_ids": next_token_id.reshape((1, 1)),
        "attention_mask": torch.cat(
            [next_inputs["attention_mask"], torch.tensor([[1]])],
            dim=1),
        "past_key_values": past_key_values,
    }
    ```

## 3. Batching

* **Synchronous batching** (aka, **batching**) means you wait for additional inputs to run a larger batch of inputs before running inference
    - Can wait until n inputs and/or maximum amount of wait time
    - Inferently trades off latency and throughput
    - To enable batching: (1) configure padding tokens in model and tokenizer, (2) tokenize inputs with `padding=True`, (3) pass in **position ids** that start at 0 after padding and increment by 1 each token
    - Typically left pad during inference, right pad during training
    ```py
    def generate_batch_tokens_with_past(inputs):
        with torch.no_grad():
            outputs = model(**inputs)

        logits = outputs.logits
        last_logits = logits[:, -1, :] # note: handling multiple inputs
        next_token_ids = last_logits.argmax(dim=1)
        return next_token_ids, outputs.past_key_values
    
    def generate_batch(inputs, max_tokens):
        # create a list of tokens for every input in the batch
        generated_tokens = [
            [] for _ in range(inputs["input_ids"].shape[0])
        ]

        attention_mask = inputs["attention_mask"]
        position_ids = attention_mask.long().cumsum(-1) - 1
        position_ids.masked_fill_(attention_mask == 0, 1)

        next_inputs = {
            "position_ids": position_ids,
            **inputs
        }

        for _ in range(max_tokens):
            next_token_ids, past_key_values = \
                generate_batch_tokens_with_past(next_inputs)

            next_inputs = {
                "input_ids": next_token_ids.reshape((-1, 1)),
                "position_ids": next_inputs["position_ids"][:, -1].unsqueeze(-1) + 1,
                "attention_mask": torch.cat([
                    next_inputs["attention_mask"],
                    torch.ones((next_token_ids.shape[0], 1)),  
                ], dim=1),
                "past_key_values": past_key_values,
            }

            next_tokens = tokenizer.batch_decode(next_token_ids)
            for i, token in enumerate(next_tokens):
                generated_tokens[i].append(token)
        return ["".join(tokens) for tokens in generated_tokens]
    
    generated_tokens = generate_batch(inputs, max_tokens=10)

    # print out prompt (in default color) and generated tokens (in red)
    for prompt, generated in zip(prompts, generated_tokens):
        print(prompt, f"\x1b[31m{generated}\x1b[0m\n")
    ```

## 4. Continuous Batching

* **Continuous batching**: still greedily process requests as they come in, but incorporate new requests in an existing batch
    - Significant performance improvements:
        - Achieves both lower latency and high throughput
        - Performance is particularly positively improved when prompts vary significantly in length, as we no longer wait for particularly long prompts to complete
        - This is how we'll achieve the streaming token prediction used to seeing with LLM prompts
    - Note that unlike synchronous batches, each prompt will be at a very different points in sequence (e.g., we may be starting tokens for a new prompt in the same request that we're completing another promp)
    - To add more prompts to a running batch, we'll (1) run a **prefill step** where create a separate batch for new prompts (to fill up the batch capacity) and then (2) **merge batches** to pad the tokens so that we can merge together the original and newly created batch into single batch
    - Then after generating the next tokens for our batch, we'll then run a **filter step** in which we (1) remove any prompts that are done, and (2) remove excess padding that was used to facilitate the "merge batches" step

* `tqdm`: Python library for generating CLI progress bars

## 5. Quantization

* Note: we need trick PyTorch into thinking parameters are float32, even when not (else we get errors):
    ```py
    # fix dtype post quantization to "pretend" to be fp32
    def get_float32_dtype(self):
        return torch.float32
    GPT2Model.dtype = property(get_float32_dtype)
    ```

* Get **memory footprint** of Hugging Face transformer model:
    ```py
    model.get_memory_footprint()
    ```

* **FP32** (float32) is the standard floating point representation for neural networks
    - 23 of the bits are the **mantissa**, meaning most of the bits are for precision

| Data Type | Bits | Exponent | Mantissa |
| --------- | ---- | -------- | -------- |
| FP32 | 32 | 8 | 23 |
| FP16 | 16 | 5 | 10 |
| BF16 (Brain Floating point) | 16 | 8 | 7 |
| FP8 (E5M2) | 8 | 5 | 2 |

* Note: not all hardware supports all of these data types

* **Quanitization** is about compressing data, not about representing same info in smaller data types
    - Store metadata to reconstruct data during forward pass
    - Trades off some computation speed for smaller memory footprint

* **Zero-Point Quanitization** 
    - Compute min and max values, and then compress all numbers [min]-[max] as unsigned 8 bit integers between 0..255
    - E.g., `[3.14063, 2.90192, 0.57782, -0.14590, -1.29091]` -> `[255, 241, 107, 65, 0]`
    - Cannot use the integers during inference; must **dequantize** during inference (either just-in-time or before inference)
        - Just-in-time is harder, but it's kind of the point of quantization
    - This is a **lossy compression**, and it does have an impact on the quality of model predictions

* Think of quanitization as a type of lossy compression:
    ```py
    def quantize(t):
        # obtain range of values in the tensor to map between 0 and 255
        min_val, max_val = t.min(), t.max()

        # determine the "zero-point", or value in the tensor to map to 0
        scale = (max_val - min_val) / 255
        zero_point = min_val

        # quantize and clamp to ensure we're in [0, 255]
        t_quant = (t - zero_point) / scale
        t_quant = torch.clamp(t_quant, min=0, max=255)

        # keep track of scale and zero_point for reversing quantization
        state = (scale, zero_point)

        # cast to uint8 and return
        t_quant = t_quant.type(torch.uint8)
        return t_quant, state

    def dequantize(t, state):
        scale, zero_point = state
        return t.to(torch.float32) * scale + zero_point
    ```

* To quantize a model:
    ```py
    def quantize_model(model):
        states = {}
        for name, param in model.named_parameters():
            param.requires_grad = False
            param.data, state = quantize(param.data)
            states[name] = state
        return model, states

    quant_model, states = quantize_model(model)
    quant_model.get_memory_footprint()
    # 137022768, 137MB (4x reduction)
    ```

## 6. Low-Rank Adaptation

* **Low-Rank Adaptation** (**LoRA**) is about fine-tuning a model without updating model parameters
    - normally, with **fine-tuning** all model parameters are updated during backpropogation
    - with **LoRA layers**, we only train maybe 1% of the parameters; this layer contains an original linear layer and two new tensors, `A` and `B`, where:
        - `A` has shape `(hidden_size, rank)` where `rank << hidden_size` and `rank` is a hyperparameter
        - `B` has shape `(rank, hidden_size)` 
        - Note `A` and `B` have the same shape as the neighboring hidden layer, but has far fewer parameters

```py
# toy model. note the self.linear. (We'll swap with a LoRA layer.)
class TestModel(torch.nn.Module):
    def __init__(self, hidden_size):
        super().__init__()
        self.embedding = torch.nn.Embedding(10, hidden_size)
        self.linear = torch.nn.Linear(hidden_size, hidden_size)
        self.lm_head = torch.nn.Linear(hidden_size, 10)
    
    def forward(self, input_ids):
        x = self.embedding(input_ids)
        x = self.linear(x)
        x = self.lm_head(x)
        return x

hidden_size = 1024
model = TestModel(hidden_size)

class LoraLayer(torch.nn.Module):
    def __init__(self, base_layer, r):
        super().__init__()
        self.base_layer = base_layer
        
        d_in, d_out = self.base_layer.weight.shape
        self.lora_a = torch.randn(d_in, r)
        self.lora_b = torch.randn(r, d_out) 
        
    def forward(self, x):
        y1 = self.base_layer(x)
        y2 = x @ self.lora_a @ self.lora_b
        return y1 + y2

# swap the model's original linear layer with a LoRA layer
lora_layer = LoraLayer(model.linear, 2)
model.linear = lora_layer
```

## 7. Multi-LoRA inference

* **Multi-LoRA** allows us to load one pre-trained **backbone model** and multiple different LoRAs to serve multiple fine-tuned model from a single deployment

## 8. LoRAX

* **LoRAX** is an open source LLM inference service maintained by Predibase

* **Adapters** (run inference with a fine-tuned model, e.g., LoRA) available through Hugging Face Hub, Predibase, S3, etc
    - Can significantly improve performance; e.g., **named entity recognition (NER) tasks** 

* **Structured generation**: define a schema for output. (LoRAX supports Pydantic)