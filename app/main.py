import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from murf import Murf
from dotenv import load_dotenv
import requests

load_dotenv()

app = FastAPI()

# Mount static files and setup templates
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Initialize Murf Client
MURF_API_KEY = os.getenv("MURF_API_KEY", "ap2_4ae196e6-b04d-4684-8772-1ca82cd549ce")
client = Murf(api_key=MURF_API_KEY)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/voices")
async def get_voices():
    try:
        voices = client.text_to_speech.get_voices()
        return {"voices": [vars(v) for v in voices]}
    except Exception as e:
        print(f"Error fetching voices: {e}")
        return {"voices": []}

@app.post("/api/synthesize")
async def synthesize_text(request: Request):
    data = await request.json()
    text = data.get("text")
    voice = data.get("voice") or "en-GB-ryan"
    rate = data.get("rate")
    pitch = data.get("pitch")
    
    if not text:
        raise HTTPException(status_code=400, detail="Text is required")

    try:
        # Generate speech
        audio_response = client.text_to_speech.generate(
            text=text,
            voice_id=voice,
            rate=int(rate) if rate is not None else 0,
            pitch=int(pitch) if pitch is not None else 0
        )
        
        # Audio response contains 'audio_file' which is a URL
        audio_url = audio_response.audio_file
        
        # Download the audio file
        r = requests.get(audio_url)
        if r.status_code == 200:
            return HTMLResponse(content=r.content, media_type="audio/mpeg")
        else:
            raise HTTPException(status_code=500, detail="Failed to download audio from Murf")
            
    except Exception as e:
        print(f"Error in synthesis: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)