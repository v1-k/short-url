from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from . import schema

url_mappings = {
    "yt": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
}

app = FastAPI()

def get_original_url(short_alias: str) -> str:
    print(url_mappings)
    return url_mappings.get(short_alias)

def save_mapping(data: schema.CreateLink) -> None:
    url_mappings[data.short_alias] = data.original_url

@app.post("/create")
async def create_short_link(data: schema.CreateLink):
    save_mapping(data.short_alias, data.original_url)
    return {"message": "Short link created successfully"}

@app.get("/{short_alias}")
async def redirect(short_alias: str) -> RedirectResponse:
    
    original_url = get_original_url(short_alias)
    if original_url is None:
        return {"message": "Not found"}
    return RedirectResponse(url=original_url)
