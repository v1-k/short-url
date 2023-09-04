
from pydantic import BaseModel, AnyUrl, ValidationError
    
class URL(BaseModel):
    URI: AnyUrl

def validator(uri: str) -> bool:
    if uri is None:
        return False
    try:
        myAddress = URL(URI = uri)
        return True
    except(ValidationError):
        return False