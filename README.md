# INTERACTING WITH LOCALLY RUNNING MODELS

## Overview

This repository contains utilities to interact with locally running language models (LLMs), like LM Studio. It includes a function to send prompts, maintain conversation history, and display all previous interactions.

## Usage

### Prerequisites

- Python 3.8+
- OpenAI-compatible client library (or LM Studio Python client)
- LM Studio running locally (Windows or Linux with GUI)

### Example

```python
from lmstudio_utils import interact_with_llm

# Send a prompt to the model
interact_with_llm("Hello LM Studio!", model="qwen3-0.6b")
interact_with_llm("Explain transformers in simple terms.", model="qwen3-0.6b")
