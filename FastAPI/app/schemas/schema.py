from pydantic import BaseModel


class ui2simul(BaseModel):
    masterid: str

class ui2simul_confirm(BaseModel):
    masterid: str