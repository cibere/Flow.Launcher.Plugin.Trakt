import trakt.tv
from flogin import Query

from ..results import UrlResult
from .base import BaseHandler


class ShowHandler(BaseHandler):
    endpoint = prefix = "show"

    async def callback(self, query: Query):
        assert self.plugin

        shows: list[trakt.tv.TVShow] = await self.search(query)
        for show in shows:
            res = UrlResult(title=show.title, sub=str(show.year or ""))
            res.url = show.ext
            yield res
