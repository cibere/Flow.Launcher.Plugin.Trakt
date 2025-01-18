from __future__ import annotations

from typing import TYPE_CHECKING

import trakt.errors
import trakt.sync
from flogin import Query
from flogin.utils import print

from ..results import RedirectResult
from .base import BaseHandler

if TYPE_CHECKING:
    from ..plugin import TraktPlugin  # noqa: F401


class BaseWatchlistHandler(BaseHandler):
    prefix = "watchlist"

    def _sync_search(self, query: str):  # type: ignore
        print("getting watchlist")
        filter = self.prefix.split(" ")[-1]
        if filter == "all":
            return trakt.sync.get_watchlist()
        return trakt.sync.get_watchlist(filter)


class RootWatchlistHandler(BaseHandler):
    prefix = "watchlist"

    async def callback(self, query: Query):  # type: ignore
        yield RedirectResult("watchlist all", "Search All of your watchlists")
        yield RedirectResult("watchlist movies", "Search for movies in your watchlist")
        yield RedirectResult("watchlist shows", "Search for shows in your watchlist")
        yield RedirectResult(
            "watchlist seasons", "Search for seasons in your watchlist"
        )
        yield RedirectResult(
            "watchlist episodes", "Search for episodes in your watchlist"
        )


class AllWatchlistHandler(BaseWatchlistHandler):
    prefix = "watchlist all"


class WatchlistMoviesHandler(BaseWatchlistHandler):
    prefix = "watchlist movies"


class WatchlistShowsHandler(BaseWatchlistHandler):
    prefix = "watchlist shows"


class WatchlistSeasonsHandler(BaseWatchlistHandler):
    prefix = "watchlist seasons"


class WatchlistEpisodesHandler(BaseWatchlistHandler):
    prefix = "watchlist episodes"


watchlist_handlers = (
    WatchlistEpisodesHandler(),
    WatchlistMoviesHandler(),
    WatchlistShowsHandler(),
    WatchlistSeasonsHandler(),
    AllWatchlistHandler(),
    RootWatchlistHandler(),
)
