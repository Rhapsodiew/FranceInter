from pydantic import BaseModel

class Text(BaseModel):
    msg: str
    translated: str | None = None
    ppl: int | None = None
    lang:str

class Img(BaseModel):
    path: str
    ppl: int | None = None

