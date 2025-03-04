from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

class BaseTable(DeclarativeBase):
    ...

class CDN(BaseTable):
    __tablename__ = "cdn"
    host = Column(String, primary_key=True, index=True)
    redirect_each_n_requests = Column(Integer, default=0)

