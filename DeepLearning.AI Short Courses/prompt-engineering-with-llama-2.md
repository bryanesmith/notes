# DeepLearning.AI Short Course: Prompt Engineering with Llama 2

Started course: 2024/04/16
Taught by: Amit Sangani (Meta)

## Introduction

* Llama is a family of models, not a single one

* **Instruction-tuned models** use **foundation models** (aka, **base models**) and running them through additional training, called **instruction tuning**
    - E.g., Llama 2 7B chat, Llama 2 13B chat, Llama 2 70B chat
    - However, it's more common to use the base model for fine tuning

- **Code Llama** comes in 7B/13B/34B, and there are three variants: (1) Code Llama, (2) Code Llama - Instruct, (3) Code Llama - Python

- **Purple Llama**: umbrella project for Generative AI Safety, and is made up of **CyberSecEval** (evaluates cybersecurity risks of LLM output) and **Llama Guard** (safety classifier model, detects harmful or toxic content)

## 1. Overview of Llama Models

* Llama 2 comes in three sizes: 7B, 13B, 70B

## 2. Getting Started with Llama 2

* Llama can be executed via cloud hosted services like Amazon Bedrock, Google Cloud, Microsoft Azure, Anyscale, Together.ai, etc

* Recommended format for writing Llama prompts:
    - **Instruction tags** `[INST]...[/INST]` for wrapping the prompt

* Minimal example:
    ```py
    from utils import llama
    prompt = "Help me write a birthday card for my dear friend Andrew."
    response = llama(prompt) # uses thre 7B-chat model by default
    print(response)
    ```

* Say you ask "What is the capital of France?"
    - The "chat" model will say "The capital of France is Paris"
    - The foundation model will output a bunch of other questions
    - Remember that the foundation model is designed to predict the next word in a sequence, not to answer questions

* By default, **temperature** is 0. This makes the model deterministic. Increase temperature to incorporate some randomness, non-determinism.

* Om average **1 token** is about 3/4 of a word
    - Note that setting `max_tokens` doesn't prompt Llama to give a briefer message; it just cuts off the message once reach limit

* If the prompt + response combined exceed 4097 tokens, will receive a validation error

* If you add a follow up prompt without providing context, it'll forget other details.

* While the helper method uses Together.ai, can also install and run locally
    - Note: you probably want the 7B version (which is quantized to 4 bites)
    1. Go to: https://ollama.com/download
    2. Download and install
    3. In CLI, run: `% ollama run llama2`
    4. When you are done, type: `/bye`. If you need help, type `/?`

## 3. Multi-turn Conversations

## 4. Prompt Engineering Techniques

## 5. Comparing Different Llama 2 models

## 6. Code Llama

## 7. Llama Guard

## 8. Walkthrough of Llama Helper Function (Optional)

## Conclusion