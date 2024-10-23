from configs.config import setting
from schemas.schema import ui2simul, ui2simul_confirm


from fastapi import APIRouter, HTTPException
from concurrent.futures import ThreadPoolExecutor
import asyncio

router = APIRouter()

executor = ThreadPoolExecutor(max_workers=setting().thread)
threads = dict()

@router.post("/start")
async def start_simulation(item: ui2simul):
    if item.masterid in threads:
        raise HTTPException(status_code=400, detail="Simulation already running.")
 
    task = simulation(item)
    future = asyncio.create_task(task.run())

    threads[item.masterid] = {
        "task": task,
        "future": future
    }

    return {"message": "Simulation start"}

@router.get("/confirm")
async def confirm_simulation(item: ui2simul_confirm):
    if item.masterid not in threads:
        raise HTTPException(status_code=404, detail="Simulation not found.")

    task = threads[item.masterid]["task"]

    print(task.result)

    


