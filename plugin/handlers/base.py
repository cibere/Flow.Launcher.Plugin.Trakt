from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING, Awaitable

import trakt.sync
import trakt.errors
from flogin import Query, SearchHandler
from ..results import FetchAuthResult, AuthScriptResult

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
            return query.text.split(" ")[0] == self.prefix
        except IndexError:
            return False

    def get_text(self, query: Query):
        return query.text.removeprefix(self.prefix).strip()

    async def on_error(self, query: Query, error: Exception):
        if isinstance(error, trakt.errors.ForbiddenException):
            return [AuthScriptResult(), FetchAuthResult()]
        super().on_error(query, error)
