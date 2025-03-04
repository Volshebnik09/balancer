from fastapi import APIRouter, Depends
from starlette import status

from schemas.CDN import UpdateCDNSchema, CDNResponseSchema
from services.CDN import CDNService

router = APIRouter(
    prefix="/cdn",
    tags=["CDN"],
)


@router.get(
    path="/",
    responses={
        status.HTTP_200_OK: {"model": CDNResponseSchema}
    }
)
async def get(
        service: CDNService = Depends(),
):
    return await service.get_config()


@router.patch(
    path="/",
    responses={
        status.HTTP_200_OK: {"model": CDNResponseSchema}
    }
)
async def update(
        body: UpdateCDNSchema,
        service: CDNService = Depends(),
):
    return await service.update_config(body)