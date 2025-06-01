from fastapi import APIRouter
from pydantic import BaseModel

class Query(BaseModel):
    query: str

class LookupResult(BaseModel):
    links: list[str]
    summary: str

router = APIRouter()

@router.post("/", response_model=LookupResult)
async def lookup(query: Query):
    # Placeholder for retrieval augmented generation
    return LookupResult(links=[], summary="No documents found")
