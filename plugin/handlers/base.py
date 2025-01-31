from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING, Awaitable

import trakt.errors
import trakt.sync
from flogin import Query, SearchHandler
from flogin.utils import print

from ..results import AuthScriptResult, FetchAuthResult, UrlResult

if TYPE_CHECKING:
    from ..plugin import TraktPlugin  # noqa: F401


class BaseHandler(SearchHandler["TraktPlugin"]):
    prefix: str
    endpoint: str

    def _sync_search(self, query: str):
        return trakt.sync.search(query, search_type=self.endpoint)

    def search(self, query: Query) -> Awaitable:
        return asyncio.to_thread(self._sync_search, self.get_text(query))

    def condition(self, query: Query) -> bool:
        try:
            return query.text.startswith(self.prefix)
        except IndexError:
            return False

    def get_text(self, query: Query):
        return query.text.removeprefix(self.prefix).strip()

    async def on_error(self, query: Query, error: Exception):
        if isinstance(error, trakt.errors.ForbiddenException):
            return [AuthScriptResult(), FetchAuthResult()]
        super().on_error(query, error)

    async def callback(self, query: Query):
        assert self.plugin

        eps = await self.search(query)
        print(eps)
        return [UrlResult.from_trakt_obj(obj) for obj in eps]
