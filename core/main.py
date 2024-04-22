from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

from src.history_aware_getter import history_aware_getter

app = FastAPI()


class ChatRequest(BaseModel):
    text: str
    type: str

class Request(BaseModel):
    question: str
    history: list[ChatRequest]


@app.post("/")
def read_item(req: Request):
    answer = history_aware_getter(req.question, req.history)
    return { "answer": answer }
