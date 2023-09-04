from pydantic import BaseModel
from typing import Optional

class CreateRequest(BaseModel):
    short_url: Optional[str] = None
    url: str

class CreateResponse(BaseModel):
    short_url: str

class TotalGeneratedResponse(BaseModel):
    total: int