from fastapi import FastAPI
from fastapi.params import Depends

from api import CDN
from schemas.balancer import BalancerParams
from services.CDN import CDNService

app = FastAPI()
app.include_router(CDN.router)

@app.get("/")
async def root(
        params:BalancerParams = Depends(),
        service: CDNService = Depends(),
):
    return await service.get_redirect(params.video)

