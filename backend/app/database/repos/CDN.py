from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.engine import get_async_session
from database.models import CDN
from schemas.CDN import UpdateCDNSchema


class CDNRepo:
    def __init__(
            self,
            session: AsyncSession = Depends(get_async_session)
    ):
        self.session = session

    async def _create_without_commit(self):
        cdn = CDN(host="", redirect_each_n_requests=-1)
        self.session.add(cdn)
        return cdn

    async def get_or_create(self):
        stmt = select(CDN)
        result = await self.session.execute(stmt)
        cdn: CDN = result.scalars().one_or_none()
        if cdn is None:
            cdn = await self._create_without_commit()
        await self.session.commit()
        return cdn

    async def update(self, body: UpdateCDNSchema):
        cdn = await self.get_or_create()
        cdn.redirect_each_n_requests = body.redirect_each_n_requests
        cdn.host = body.host
        await self.session.commit()
        return cdn



