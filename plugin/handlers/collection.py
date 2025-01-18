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


class BasecollectionHandler(BaseHandler):
    prefix = "collection"

    def _sync_search(self, query: str):  # type: ignore
        print("getting collection")
        filter = self.prefix.split(" ")[-1]
        if filter == "all":
            return trakt.sync.get_collection()
        return trakt.sync.get_collection(filter)


class RootcollectionHandler(BaseHandler):
    prefix = "collection"

    async def callback(self, query: Query):  # type: ignore
        yield RedirectResult("collection all", "Search everything in your collection")
        yield RedirectResult(
            "collection movies", "Search for movies in your collection"
        )
        yield RedirectResult("collection shows", "Search for shows in your collection")
        yield RedirectResult(
            "collection seasons", "Search for seasons in your collection"
        )
        yield RedirectResult(
            "collection episodes", "Search for episodes in your collection"
        )


class AllcollectionHandler(BasecollectionHandler):
    prefix = "collection all"


class collectionMoviesHandler(BasecollectionHandler):
    prefix = "collection movies"


class collectionShowsHandler(BasecollectionHandler):
    prefix = "collection shows"


class collectionSeasonsHandler(BasecollectionHandler):
    prefix = "collection seasons"


class collectionEpisodesHandler(BasecollectionHandler):
    prefix = "collection episodes"


collection_handlers = (
    collectionEpisodesHandler(),
    collectionMoviesHandler(),
    collectionShowsHandler(),
    collectionSeasonsHandler(),
    AllcollectionHandler(),
    RootcollectionHandler(),
)
