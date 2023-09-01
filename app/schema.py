from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CreateLink(BaseModel):
    short_alias: str
    original_url: str
