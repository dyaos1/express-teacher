from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

from src.getter import getter

app = FastAPI()


@app.get("/test")
def read_root():
    answer = getter("tell me about middleware")
    return {"answer": f"{answer}"}


class ChatRequest(BaseModel):
    text: str
    type: str


class Request(BaseModel):
    question: str
    history: list[ChatRequest]


@app.post("/")
def read_item(req: Request):
    answer = getter(req.question)
    print(req.history)
    return {"answer": f"{answer}"}
