from configs.config import setting
from schemas.schema import ui2simul, ui2simul_confirm


from fastapi import APIRouter
from concurrent.futures import ThreadPoolExecutor
import asyncio

router = APIRouter()

executor = ThreadPoolExecutor(max_workers=setting().thread)
tasks = dict()

@router.post("/start")
async def start_simulation(item: ui2simul):
    global tasks

    masterid = item.masterid

    if masterid in tasks and not tasks[masterid].done():
        return {"message": f"simulation is already running for {masterid}"}
    
    task = simulation()
    tasks[masterid] = asyncio.create_task(task.run())

    return {"message": "Simulation start"}

@router.get("/confirm")
async def confirm_simulation(item: ui2simul_confirm):
    global tasks

    masterid = item.masterid

    if masterid in tasks and not tasks[masterid].done():
        return {"message": f"simulation is already running for {masterid}"}

    


