# Sample agentic app using [aisuite](https://github.com/andrewyng/aisuite)

## Setup

1. `pip install "aisuite[all]"`

2. Set AISUITE_MODEL. E.g.,
```sh
export AISUITE_MODEL="anthropic:claude-sonnet-4-5"
# export AISUITE_MODEL="openai:gpt-5.1"
```

3. Export API key for selected model. E.g.,
```sh
export ANTHROPIC_API_KEY=...
# export OPENAI_API_KEY=...
```

## Projects

1. `tell_joke.py`: Tells a joke in Pirate English. [Source](https://github.com/andrewyng/aisuite)

2. `create_snake_game.py`: Creates Web-based Snake Game, `snake_game.html`. [Source](https://info.deeplearning.ai/claude-opus-4.5-saves-tokens-white-house-boosts-ai-powered-science-amazon-exposes-nova-2-pro-checkpoints-small-models-solve-hard-puzzels-2)