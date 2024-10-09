from fastapi import APIRouter
from schemas.item_schemas import Item


router = APIRouter()

@router.get("/items")
def start_test(a: int):
    print(a)

    return {"item 항목": a}


@router.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}