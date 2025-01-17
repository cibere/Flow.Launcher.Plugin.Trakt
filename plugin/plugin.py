import trakt.core
from flogin import Plugin

from .handlers.episodes import EpisodeHandler
from .handlers.movies import MovieHandler
from .handlers.person import PersonHandler
from .handlers.shows import ShowHandler
from .handlers.root import RootHandler

trakt.core.load_config()


class TraktPlugin(Plugin):
    def __init__(self) -> None:
        super().__init__()

        self.register_search_handler(ShowHandler())
        self.register_search_handler(MovieHandler())
        self.register_search_handler(EpisodeHandler())
        self.register_search_handler(PersonHandler())
        self.register_search_handler(RootHandler())
