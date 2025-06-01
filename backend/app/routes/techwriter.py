from fastapi import APIRouter
from pydantic import BaseModel

class FreeText(BaseModel):
    text: str

class SOP(BaseModel):
    title: str
    description: str | None = None
    steps: list[str]
    tools: list[str] | None = None
    triggers: list[str] | None = None

router = APIRouter()

@router.post("/", response_model=SOP)
async def generate_sop(free_text: FreeText):
    # Placeholder for GPT-4 interaction
    return SOP(title="Generated SOP", steps=["Step 1"], description="", tools=[], triggers=[])
