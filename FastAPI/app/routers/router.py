from . import threads, executor
from schemas.schema import ui2simul
from services.service import simulation

from fastapi import APIRouter
import asyncio
from concurrent.futures import Future

router = APIRouter()


@router.post("/start")
async def start_simulation(item: ui2simul):
    # 실행중인 thread 개수 확인
    if len(threads) >= 1:
        return {"message": "Simulation is running"}
    elif item.masterid in threads:
        return {"message": f"ID {item.masterid} Simulation is running"}

    # 시뮬레이션 작업 실행
    task = simulation(item)
    loop = asyncio.get_running_loop()
    future: Future = loop.run_in_executor(executor, task.run)

    # threads 관리
    threads[item.masterid] = {
        "task": task,
        "future": future
    }

    # 작업이 완료되면 threads 삭제
    future.add_done_callback(lambda _: threads.pop(item.masterid, None))

    return {"message": "Simulation started"}


