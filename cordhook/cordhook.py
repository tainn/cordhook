from __future__ import annotations

import copy
from collections.abc import Iterable
from typing import TypedDict

import httpx


class EmbedStruct(TypedDict):
    author: dict[str, str | None]
    color: int | None
    title: str | None
    url: str | None
    description: str | None
    fields: list[dict[str, str | bool | None]]
    thumbnail: dict[str, str | None]
    image: dict[str, str | None]
    footer: dict[str, str | None]
    timestamp: str | None


class FullStruct(TypedDict):
    username: str | None
    avatar_url: str | None
    content: str | None
    tts: bool | None
    embeds: list[EmbedStruct]


EMBED_STRUCT: EmbedStruct = {
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

FULL_STRUCT: FullStruct = {
    "username": None,
    "avatar_url": None,
    "content": None,
    "tts": None,
    "embeds": [EMBED_STRUCT],
}


class Form:
    def __init__(self) -> None:
        self.form = copy.deepcopy(FULL_STRUCT)
        self.active_embed = 0

    def username(self, username: str | None = None) -> Form:
        self.form["username"] = username
        return self

    def avatar_url(self, avatar_url: str | None = None) -> Form:
        self.form["avatar_url"] = avatar_url
        return self

    def content(self, content: str | None = None) -> Form:
        self.form["content"] = content
        return self

    def tts(self, tts: bool | None = None) -> Form:
        self.form["tts"] = tts
        return self

    def embed_author(self, name: str | None = None, url: str | None = None, icon_url: str | None = None) -> Form:
        self.form["embeds"][self.active_embed]["author"] = {
            "name": name,
            "url": url,
            "icon_url": icon_url,
        }
        return self

    def embed_color(self, color: int | None = None) -> Form:
        self.form["embeds"][self.active_embed]["color"] = color
        return self

    def embed_title(self, title: str | None = None) -> Form:
        self.form["embeds"][self.active_embed]["title"] = title
        return self

    def embed_url(self, url: str | None = None) -> Form:
        self.form["embeds"][self.active_embed]["url"] = url
        return self

    def embed_description(self, description: str | None = None) -> Form:
        self.form["embeds"][self.active_embed]["description"] = description
        return self

    def embed_fields(self, name: str | None = None, value: str | None = None, inline: bool | None = None) -> Form:
        self.form["embeds"][self.active_embed]["fields"].append(
            {
                "name": name,
                "value": value,
                "inline": inline,
            }
        )
        return self

    def embed_thumbnail(self, url: str | None = None) -> Form:
        self.form["embeds"][self.active_embed]["thumbnail"] = {
            "url": url,
        }
        return self

    def embed_image(self, url: str | None = None) -> Form:
        self.form["embeds"][self.active_embed]["image"] = {
            "url": url,
        }
        return self

    def embed_footer(self, text: str | None = None, icon_url: str | None = None) -> Form:
        self.form["embeds"][self.active_embed]["footer"] = {
            "text": text,
            "icon_url": icon_url,
        }
        return self

    def embed_timestamp(self, timestamp: str | None = None) -> Form:
        self.form["embeds"][self.active_embed]["timestamp"] = timestamp
        return self

    def embed_fields_count(self) -> int:
        return len(self.form["embeds"][self.active_embed]["fields"])

    def embeds_count(self) -> int:
        return len(self.form["embeds"])

    def next_active_embed(self) -> None:
        self.form["embeds"].append(copy.deepcopy(EMBED_STRUCT))
        self.active_embed += 1

    def change_active_embed(self, embed: int) -> None:
        self.active_embed = embed

    def post(self, url: str | Iterable[str] | None = None) -> None:
        if isinstance(url, str):
            httpx.post(url, json=self.form, timeout=10)

        elif isinstance(url, Iterable):
            for single in url:
                httpx.post(single, json=self.form, timeout=10)
