from __future__ import annotations

import copy
from collections.abc import Iterable

import httpx

EMBED_STRUCT: dict = {
    "author": {
        "name": None,
        "url": None,
        "icon_url": None,
    },
    "color": None,
    "title": None,
    "url": None,
    "description": None,
    "fields": [],
    "thumbnail": {
        "url": None,
    },
    "image": {
        "url": None,
    },
    "footer": {
        "text": None,
        "icon_url": None,
    },
    "timestamp": None,
}

FULL_STRUCT: dict = {
    "username": None,
    "avatar_url": None,
    "content": None,
    "tts": None,
    "embeds": [EMBED_STRUCT],
}


class Form:
    def __init__(self) -> None:
        self.form: dict = copy.deepcopy(FULL_STRUCT)
        self.active_embed: int = 0

    # Form population methods

    def username(self, username: str = None) -> Form:
        self.form["username"] = username
        return self

    def avatar_url(self, avatar_url: str = None) -> Form:
        self.form["avatar_url"] = avatar_url
        return self

    def content(self, content: str = None) -> Form:
        self.form["content"] = content
        return self

    def tts(self, tts: bool = None) -> Form:
        self.form["tts"] = tts
        return self

    def embed_author(self, name: str = None, url: str = None, icon_url: str = None) -> Form:
        self.form["embeds"][self.active_embed]["author"] = {
            "name": name,
            "url": url,
            "icon_url": icon_url,
        }
        return self

    def embed_color(self, color: int = None) -> Form:
        self.form["embeds"][self.active_embed]["color"] = color
        return self

    def embed_title(self, title: str = None) -> Form:
        self.form["embeds"][self.active_embed]["title"] = title
        return self

    def embed_url(self, url: str = None) -> Form:
        self.form["embeds"][self.active_embed]["url"] = url
        return self

    def embed_description(self, description: str = None) -> Form:
        self.form["embeds"][self.active_embed]["description"] = description
        return self

    def embed_fields(self, name: str = None, value: str = None, inline: bool = None) -> Form:
        self.form["embeds"][self.active_embed]["fields"].append(
            {
                "name": name,
                "value": value,
                "inline": inline,
            }
        )
        return self

    def embed_thumbnail(self, url: str = None) -> Form:
        self.form["embeds"][self.active_embed]["thumbnail"] = {"url": url}
        return self

    def embed_image(self, url: str = None) -> Form:
        self.form["embeds"][self.active_embed]["image"] = {"url": url}
        return self

    def embed_footer(self, text: str = None, icon_url: str = None) -> Form:
        self.form["embeds"][self.active_embed]["footer"] = {"text": text, "icon_url": icon_url}
        return self

    def embed_timestamp(self, timestamp: str = None) -> Form:
        self.form["embeds"][self.active_embed]["timestamp"] = timestamp
        return self

    # Utility methods

    def embed_fields_count(self) -> int:
        return len(self.form["embeds"][self.active_embed]["fields"])

    def embeds_count(self) -> int:
        return len(self.form["embeds"])

    def next_active_embed(self) -> None:
        self.form["embeds"].append(copy.deepcopy(EMBED_STRUCT))
        self.active_embed += 1

    def change_active_embed(self, embed: int) -> None:
        self.active_embed: int = embed

    def post(self, url: str | Iterable[str] = None) -> None:
        if isinstance(url, str):
            httpx.post(url, json=self.form, timeout=10)
        elif isinstance(url, Iterable):
            for single in url:
                httpx.post(single, json=self.form, timeout=10)
