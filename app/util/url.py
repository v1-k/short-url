
from pydantic import BaseModel, AnyUrl, ValidationError
    
class URL(BaseModel):
    URI: AnyUrl

def validator(uri: str) -> bool:
    try:
        myAddress = URL(URI = uri)
        return True
    except(ValidationError):
        print('Invalid URI')
        return False