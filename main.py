import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from typing import List
from dotenv import load_dotenv
from groq import Groq

# Load environment configurations from your .env file
load_dotenv()

if not os.getenv("GROQ_API_KEY"):
    raise ValueError("CRITICAL ERROR: 'GROQ_API_KEY' is missing inside your environment/.env configuration.")

# Initialize the standard FastAPI instance
app = FastAPI(
    title="TaleStudio Enterprise AI", 
    description="Polished Google-styled AI Story Generator using Groq & Llama 3.3 70B"
)

# Mount Static Files (CSS) and configure templates directory
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Initialize official Groq client with explicit API key loading
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Input Payload Validation Schema
class StoryGenerationPayload(BaseModel):
    theme: str = Field(..., min_length=2, max_length=100)
    genre: str = Field(..., min_length=2, max_length=50)
    characters: List[str] = Field(..., min_items=1)
    word_count: int = Field(default=400, ge=100, le=2500) # Flexible targeting window

@app.get("/", response_class=HTMLResponse)
async def serve_home(request: Request):
    """
    Serves the polished responsive frontend dashboard.
    Uses explicit keyword arguments to support the latest Starlette/FastAPI signatures.
    """
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/api/generate")
async def process_story_request(payload: StoryGenerationPayload):
    """
    Communicates via high-speed inference with llama-3.3-70b-versatile on Groq cloud.
    Returns clean structural raw markdown string contents to the frontend.
    """
    character_line = ", ".join([char.strip() for char in payload.characters if char.strip()])
    if not character_line:
        raise HTTPException(status_code=400, detail="Please provide a valid character list.")

    try:
        completion = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a masterful, award-winning creative fiction author. "
                        f"Write a compelling narrative targeting approximately {payload.word_count} words using standard clean Markdown syntax. "
                        "Structure your story precisely using a clear, highly engaging primary title (# Title), elegant multi-paragraph spacings, "
                        "and vivid sensory imagery. Never include conversational meta-commentary, notes, intros, or outros."
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"Core Conceptual Theme: {payload.theme}\n"
                        f"Literary Genre: {payload.genre}\n"
                        f"Key Cast Characters: {character_line}\n"
                        f"Required Length Target: ~{payload.word_count} words\n\n"
                        f"Draft the full stylized literary markdown content now:"
                    )
                }
            ],
            temperature=0.82,  # Balancing predictability and creative variation
            max_tokens=min(payload.word_count + 500, 3500) # Safely scale allocation ceiling dynamically
        )
        
        raw_story_markdown = completion.choices[0].message.content
        return {"success": True, "story": raw_story_markdown}

    except Exception as api_err:
        raise HTTPException(status_code=500, detail=f"Groq Cloud Failure: {str(api_err)}")