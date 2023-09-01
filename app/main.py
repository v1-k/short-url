from fastapi import FastAPI
from .router import public

app = FastAPI()
app.include_router(public.router)