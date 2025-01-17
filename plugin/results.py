from __future__ import annotations
from pathlib import Path
import random
import sys
import asyncio
import os
from typing import TYPE_CHECKING, Iterable
import trakt.core

from flogin import Glyph, ProgressBar, Result, ResultPreview
from flogin.utils import print

if TYPE_CHECKING:
    from .plugin import TraktPlugin  # noqa: F401


class BaseResult(Result["TraktPlugin"]):
    def __init__(
        self,
        title: str | None = None,
        sub: str | None = None,
        icon: str | None = None,
        title_highlight_data: Iterable[int] | None = None,
        title_tooltip: str | None = None,
        sub_tooltip: str | None = None,
        copy_text: str | None = None,
        score: int | None = None,
        preview: ResultPreview | None = None,
        progress_bar: ProgressBar | None = None,
        rounded_icon: bool | None = None,
        glyph: Glyph | None = None,
    ) -> None:
        super().__init__(
            title,
            sub,
            icon or "assets/app.png",
            title_highlight_data,
            title_tooltip,
            sub_tooltip,
            copy_text,
            score,
            "".join(
                random.choices("qwertyuiopasdfghjklzxcvbnm", k=5)
            ),  # temp fix to https://github.com/Flow-Launcher/Flow.Launcher/pull/3112
            preview,
            progress_bar,
            rounded_icon,
            glyph,
        )


class UrlResult(BaseResult):
    url: str

    async def callback(self):
        assert self.plugin

        await self.plugin.api.open_url("https://trakt.tv/" + self.url)


class AuthScriptResult(BaseResult):
    def __init__(self):
        super().__init__(
            "You are unauthorized",
            sub="Click to run the authorization script",
            icon="assets/app.png",
            score=100,
        )

    async def callback(self):
        assert self.plugin
        executable = sys.executable.replace("pythonw", "python")
        auth_script = Path(self.plugin.metadata.directory) / "auth_script.py"
        print(executable)
        print(auth_script)
        cmd = f"{executable} {auth_script}"
        print(cmd)
        await asyncio.to_thread(os.system, cmd)


class FetchAuthResult(BaseResult):
    def __init__(self):
        super().__init__("Fetch Auth details from auth script", icon="assets/app.png")

    async def callback(self):
        assert self.plugin

        trakt.core.load_config()
        await self.plugin.api.show_notification(
            "Trakt", "Authorization Details Fetched"
        )
        return False
