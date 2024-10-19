from pydantic import BaseModel


class Item(BaseModel):
    masterid: str

    data: Optional[]