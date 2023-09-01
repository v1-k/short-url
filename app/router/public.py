from fastapi import APIRouter, status
from fastapi.responses import RedirectResponse
from ..func import url
from .. import schema

router = APIRouter(
    prefix="",
    tags=['Public API']
)

# @router.get("/")
# def get():
#     return {"public": "public"}

@router.get("/{alias}")
async def redirect(alias: str) -> RedirectResponse:
    original_url = url.get(alias)
    if original_url is None:
        return {"message": "Not found"}
    return RedirectResponse(url=original_url)

@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=schema.CreateResponse)
async def create(data: schema.CreateRequest):
    alias = url.set(data)
    response = schema.CreateResponse(alias=alias)
    return response    
    