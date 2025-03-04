from fastapi.params import Depends
from fastapi.responses import RedirectResponse

from database.repos.CDN import CDNRepo
from schemas.CDN import UpdateCDNSchema

request_counter = 0

class CDNService:
    def __init__(
            self,
            CDNRepo: CDNRepo = Depends()
    ):
        self.CDNRepo = CDNRepo

    def _get_host(self, url: str):
        host = url.split("/")[2]
        return host

    def _get_bucket_name(self, host: str):
        bucket_name = host.split(".")[0]
        return bucket_name

    def _get_video_path(self, url: str):
        video_path = "/".join(url.split("/")[3:])
        return video_path

    async def get_config(self):
        return await self.CDNRepo.get_or_create()

    async def update_config(self, body: UpdateCDNSchema):
        return await self.CDNRepo.update(body)

    async def redirect_in_cdn(self, url: str):
        config = await self.CDNRepo.get_or_create()
        video_path = self._get_video_path(url)
        host = self._get_host(url)
        bucket_name = self._get_bucket_name(host)
        url = f"https://{config.host}/{bucket_name}/{video_path}"
        return RedirectResponse(url, status_code=301)


    async def get_redirect(self, url: str):
        global request_counter
        config = await self.CDNRepo.get_or_create()

        request_counter+= 1

        if config.redirect_each_n_requests == 0 or request_counter % config.redirect_each_n_requests == 0:
            request_counter = 0
            return RedirectResponse(url, status_code=301)

        return await self.redirect_in_cdn(url)

