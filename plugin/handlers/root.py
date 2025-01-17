from __future__ import annotations

from typing import TYPE_CHECKING

from flogin import Query, SearchHandler
from ..results import BaseResult

if TYPE_CHECKING:
    from ..plugin import TraktPlugin  # noqa: F401


class RedirectResult(BaseResult):
    def __init__(self, keyword: str, title: str):
        super().__init__(
            title,
            icon="assets/app.png",
        )
        self.keyword = keyword

    async def callback(self):
        assert self.plugin
        assert self.plugin.last_query

        await self.plugin.last_query.update(text=f"{self.keyword} ")
        return False


class RootHandler(SearchHandler["TraktPlugin"]):
    async def callback(self, query: Query):
        yield RedirectResult("show", "Search TV Shows")
        yield RedirectResult("episode", "Search TV Episodes")
        yield RedirectResult("movie", "Search Movies")
        yield RedirectResult("person", "Search People")
