from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from .. import schema
from ..db.session import get_db
from ..db import util
from ..util import url

router = APIRouter(
    prefix="",
    tags=['Public API']
)

@router.get("/")
def get():
    return {"public": "public"}

@router.get("/{short_url}")
async def redirect(short_url: str, db: Session = Depends(get_db)) -> RedirectResponse:
    result = util.get(short_url, db)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not found")
    return RedirectResponse(url=result.url)

@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=schema.CreateResponse)
async def create(data: schema.CreateRequest, db: Session = Depends(get_db)):
    if not url.validator(data.url):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail=f"Invalid URL: {data.url}")
    short_url = util.set(data, db)
    response = schema.CreateResponse(short_url=short_url)
    return response

