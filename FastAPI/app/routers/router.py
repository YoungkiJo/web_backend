from . import event

from fastapi import APIRouter
import asyncio

router = APIRouter()

tasks = dict()
queues = dict()

@router.get("/")
def root():
    return {"message": "Hello"}

@router.post("/item")
async def start_simulation(item):

    if len(queues) > 0:
        return {"message":"동작중"}

    if item.id not in queues:
        queues[item.id] = asyncio.Queue()
    
    task = simulation(queues[item.id])

    tasks[item.id] = asyncio.create_task(task.run())
    asyncio.create_task(tasks[item.id])

    return {"message": "Start"}

@router.get("/confirm")
async def confirm_simulation(item):
    if item.id not in queues:
        print(f"No queue found for tastk {item.id}")
        return
    
    result = await queues[item.id].get()
    print(f"Task {item.id} intermediate result: {result}")
    queues[item.id].task_done()
    


    


