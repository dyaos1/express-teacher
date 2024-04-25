from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

from src.history_aware_getter import history_aware_getter
from src.setter import setter

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


@app.get("/set")
def set_data():
    status = 'success'
    try :
        setter()
    except Exception as e:
        print(e)
        status = 'fail'
    return {"status": status}
