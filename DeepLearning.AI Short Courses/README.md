# DeepLearning.AI Short Courses

## Efficiently Serving LLMs
2024/04/13

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

* **Continuous batching**: still greedily process requests as they come in, but incorporate new requests in an existing batch
    - Significant performance improvements:
        - Achieves both lower latency and high throughput
        - Performance is particularly positively improved when prompts vary significantly in length, as we no longer wait for particularly long prompts to complete
        - This is how we'll achieve the streaming token prediction used to seeing with LLM prompts
    - Note that unlike synchronous batches, each prompt will be at a very different points in sequence (e.g., we may be starting tokens for a new prompt in the same request that we're completing another promp)
    - To add more prompts to a running batch, we'll (1) run a **prefill step** where create a separate batch for new prompts (to fill up the batch capacity) and then (2) **merge batches** to pad the tokens so that we can merge together the original and newly created batch into single batch
    - Then after generating the next tokens for our batch, we'll then run a **filter step** in which we (1) remove any prompts that are done, and (2) remove excess padding that was used to facilitate the "merge batches" step

* `tqdm`: Python library for generating CLI progress bars