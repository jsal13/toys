import random

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()

origins = ["*"]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@api.get("/float")
def get_float() -> dict[str, float]:
    """Return a random float."""
    return {"data": random.random()}
