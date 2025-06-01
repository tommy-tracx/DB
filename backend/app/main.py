from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="DrBimmer OS")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health():
    return {"status": "ok"}

from .routes import pitcrew, techwriter, lookupbot

app.include_router(pitcrew.router, prefix="/api/pitcrew")
app.include_router(techwriter.router, prefix="/api/techwriter")
app.include_router(lookupbot.router, prefix="/api/lookupbot")
