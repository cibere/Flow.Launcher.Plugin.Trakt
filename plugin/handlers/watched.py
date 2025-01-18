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


class BasewatchedHandler(BaseHandler):
    prefix = "watched"

    def _sync_search(self, query: str):  # type: ignore
        print("getting watched")
        filter = self.prefix.split(" ")[-1]
        if filter == "all":
            return trakt.sync.get_watched()
        return trakt.sync.get_watched(filter)


class RootwatchedHandler(BaseHandler):
    prefix = "watched"

    async def callback(self, query: Query):  # type: ignore
        yield RedirectResult("watched all", "Search everything that you have watched")
        yield RedirectResult("watched movies", "Search for movies you have watched")
        yield RedirectResult("watched shows", "Search for shows you have watched")
        yield RedirectResult("watched seasons", "Search for seasons you have watched")
        yield RedirectResult(
            "watched episodes", "Search for episodes that you have watched"
        )


class AllwatchedHandler(BasewatchedHandler):
    prefix = "watched all"


class watchedMoviesHandler(BasewatchedHandler):
    prefix = "watched movies"


class watchedShowsHandler(BasewatchedHandler):
    prefix = "watched shows"


class watchedSeasonsHandler(BasewatchedHandler):
    prefix = "watched seasons"


class watchedEpisodesHandler(BasewatchedHandler):
    prefix = "watched episodes"


watched_handlers = (
    watchedEpisodesHandler(),
    watchedMoviesHandler(),
    watchedShowsHandler(),
    watchedSeasonsHandler(),
    AllwatchedHandler(),
    RootwatchedHandler(),
)
