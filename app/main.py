from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .router import public
from .db import model
from .db.session import engine

model.Base.metadata.create_all(bind=engine)
app = FastAPI()

origins = ["*"]#,"http://stackapex.com", "https://stackapex.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
)

app.include_router(public.router)