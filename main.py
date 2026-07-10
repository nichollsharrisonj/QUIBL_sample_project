import os
from pathlib import Path

import quibl
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI()
here = Path(__file__).resolve().parent


"""
To instantiate quibl bot, supply:
path, 
optional retrieval store path (where the vector db persists), 
credentials.
"""
pledge_bot = quibl.InterventionBot(
    here / "interventions" / "pledge",
    retrieval_store_path=os.getenv("QUIBL_RETRIEVAL_STORE_PATH", "/data/quibl/chroma"),
    credentials={"OPENAI_API_KEY": os.getenv("OPENAI_API_KEY", "")},
)

# Chat endpoint
@app.post("/pledge/chat")
async def pledge_chat(req: quibl.AssistantChatRequest):
    try:
        return await pledge_bot.chat(req)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


# Test web view for profiling the bot. Navigate to localhost:8000/pledge
@app.get("/pledge", response_class=HTMLResponse)
def pledge_index():
    return HTMLResponse(
        quibl.render_test_ui_html(
            intervention_id="pledge",
            title="PLEDGE",
            chat_endpoint="/pledge/chat",
            bot_info=pledge_bot.bot_info(),
        )
    )
