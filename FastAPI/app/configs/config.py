from pydantic_settings import BaseSettings

class setting(BaseSettings):
    thread: int

    class Config:
        env_file=".env"
        extra="ignore"

class run_setting(BaseSettings):
    host: str
    port: int

    class Config:
        env_file = ".env"
        extra = "ignore"