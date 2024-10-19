from schemas.item_schemas import Item
# from services.service import 


from fastapi import APIRouter


router = APIRouter()

@router.post("/test1")
async def read_root(item:Item):
    


    return {"message": "Hello, FastAPI!"}


@router.get("/test1_confirm")
def start_test(a: int):
    print(a)

    return {"item 항목": a}
