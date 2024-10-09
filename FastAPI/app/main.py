from fastapi import FastAPI
from api.router import router
from core.config import Settings

app = FastAPI()

app.include_router(router)



if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=Settings().host, port=Settings().port)

# uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload