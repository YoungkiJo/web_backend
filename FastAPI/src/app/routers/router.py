from schemas.item_schema import Item


from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_root():
    return {"message": "Hello, FastAPI"}

@router.post("/test1")
async def start_test(item: Item):
    print(item)

    return {"item 항목": item.s}