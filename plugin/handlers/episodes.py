import trakt.tv
from flogin import Query

from ..results import UrlResult
from .base import BaseHandler


class EpisodeHandler(BaseHandler):
    endpoint = prefix = "episode"

    async def callback(self, query: Query):
        assert self.plugin

        eps: list[trakt.tv.TVEpisode] = await self.search(query)
        for ep in eps:
            res = UrlResult(ep.title, sub=f"Show: {ep.show}")
            res.url = ep.ext
            yield res
