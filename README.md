# Sample QUIBL Project

A minimal example of a [QUIBL](https://test.pypi.org/project/quibl/) intervention chatbot for PLEDGE

## Components

**`interventions/pledge/`**: the bot config directory:

- `config.yml`: RAG settings (chunking, embedding model, retrieval strategy)
- `guardrails/`: NeMo safety and topic rails
- `orchestration/`: system prompt and main LLM config
- `corpus/`: PDF documents the bot answers from

**`main.py`**: a minimal FastAPI app that instantiates the bot from the config and exposes a chat endpoint and quibl's builtin test ui.

## Requirements

- Docker and Docker Compose
- An OpenAI API key

## Run

```bash
docker compose up
```

Then open `http://localhost:8000/pledge` in a browser to chat with the bot.

See `http://localhost:8000/docs` for fastapi's auto-generated docs of the api.

The vector index is built from the corpus on first run and persists in a Docker volume (`quibl_data:/data/quibl`)
