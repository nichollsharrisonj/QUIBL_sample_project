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

## API

### Requests look like this:

```bash
POST /pledge/chat
```

```json
{
  "user_message": "<string>",
  "conversation": [
    { "role": " <user | assistant | system> ", "content": "<string>" },...
  ],
  "include_trace": false #(for prod)
}
```

(conversation is ordered least to most recent)

### Response look like this:

```json
{
  "intervention_id": "pledge",
  "content": "<string>",
  "trace_id": "<string>", #(can be ignored for prod)
  "guardrails_invoked": false #(might be relevant for UI, particularly escalation)
}
```

The frontend is expected to construct `{ role: "assistant", content: ... }` and append it to the history added with each call to the api. The API has an internal limit on history turns which is configured as part of the library, so passing additional conv turns doesn't make a difference.
