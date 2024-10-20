from fastapi import FastAPI
from routers.router import router
from configs.config import run_settings

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=run_settings().host, port=run_settings().port)