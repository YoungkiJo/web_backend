from routers.router import router
from configs.config import run_setting

from fastapi import FastAPI

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=run_setting().host, port=run_setting().port)