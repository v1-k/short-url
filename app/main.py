from fastapi import FastAPI
from .router import public
from .db import model
from .db.session import engine

model.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(public.router)