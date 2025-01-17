import trakt.movies
from flogin import Query

from ..results import UrlResult
from .base import BaseHandler


class MovieHandler(BaseHandler):
    endpoint = prefix = "movie"

    async def callback(self, query: Query):
        assert self.plugin

        movie: list[trakt.movies.Movie] = await self.search(query)
        for m in movie:
            res = UrlResult(m.title, sub=str(m.year or ""))
            res.url = m.ext
            yield res
