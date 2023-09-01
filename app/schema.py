from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CreateRequest(BaseModel):
    alias: Optional[str]
    url: str

class CreateResponse(BaseModel):
    alias: str