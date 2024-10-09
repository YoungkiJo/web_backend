from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    host: str
    port: int
    api1: str

    class Config:
        env_file = ".env"
