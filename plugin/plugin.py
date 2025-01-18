import trakt.core
from flogin import Plugin

from .handlers.collection import collection_handlers
from .handlers.episodes import EpisodeHandler
from .handlers.movies import MovieHandler
from .handlers.person import PersonHandler
from .handlers.root import RootHandler
from .handlers.shows import ShowHandler
from .handlers.watched import watched_handlers
from .handlers.watchlist import watchlist_handlers

trakt.core.load_config()


class TraktPlugin(Plugin):
    def __init__(self) -> None:
        super().__init__()

        self.register_search_handler(ShowHandler())
        self.register_search_handler(MovieHandler())
        self.register_search_handler(EpisodeHandler())
        self.register_search_handler(PersonHandler())
        self.register_search_handlers(*watchlist_handlers)
        self.register_search_handlers(*watched_handlers)
        self.register_search_handlers(*collection_handlers)
        self.register_search_handler(RootHandler())
