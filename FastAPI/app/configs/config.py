from pydantic_settings import BaseSettings

class run_setting(BaseSettings):
    host: str
    port: int

    class Config:
        env_file = ".env"
        extra = "ignore"