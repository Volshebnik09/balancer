from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    db_url: str = ...
    dev_mode: bool = False

    class Config:
        pass


settings = Settings()

