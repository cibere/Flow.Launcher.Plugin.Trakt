from __future__ import annotations

from typing import TYPE_CHECKING

from flogin import Query, SearchHandler

from ..results import RedirectResult

if TYPE_CHECKING:
    from ..plugin import TraktPlugin  # noqa: F401


class RootHandler(SearchHandler["TraktPlugin"]):
    async def callback(self, query: Query):
        yield RedirectResult("show", "Search TV Shows")
        yield RedirectResult("episode", "Search TV Episodes")
        yield RedirectResult("movie", "Search Movies")
        yield RedirectResult("person", "Search People")
        yield RedirectResult("watchlist", "Search your watchlist")
        yield RedirectResult("watched", "Search your watched items")
        yield RedirectResult("collection", "Search your collection")
