from pydantic_settings import BaseSettings

class run_settings(BaseSettings):
    host: str
    port:int

    class Config:
        env_file = ".env"
        extra = "ignore"
        