from pydantic import BaseModel


class UpdateCDNSchema(BaseModel):
    redirect_each_n_requests: int
    host: str

class CDNResponseSchema(BaseModel):
    redirect_each_n_requests: int
    host: str