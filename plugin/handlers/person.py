import trakt.tv
from flogin import Query

from ..results import UrlResult
from .base import BaseHandler


class PersonHandler(BaseHandler):
    endpoint = prefix = "person"

    async def callback(self, query: Query):
        assert self.plugin

        people: list[trakt.tv.Person] = await self.search(query)
        for person in people:
            res = UrlResult(person.name)
            res.url = person.ext
            yield res
