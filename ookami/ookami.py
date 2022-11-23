from __future__ import annotations

import requests


class Form:
    def __init__(self) -> None:
        self.form: dict = {
            "username": None,
            "avatar_url": None,
            "content": None,
            "tts": None,
            "embeds": [
                {
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
            ],
        }

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

    def embeds_author(self, name: str = None, url: str = None, icon_url: str = None) -> Form:
        self.form["embeds"][0]["author"] = {
            "name": name,
            "url": url,
            "icon_url": icon_url,
        }
        return self

    def embeds_color(self, color: int = None) -> Form:
        self.form["embeds"][0]["color"] = color
        return self

    def embeds_title(self, title: str = None) -> Form:
        self.form["embeds"][0]["title"] = title
        return self

    def embeds_url(self, url: str = None) -> Form:
        self.form["embeds"][0]["url"] = url
        return self

    def embeds_description(self, description: str = None) -> Form:
        self.form["embeds"][0]["description"] = description
        return self

    def embeds_fields(self, name: str = None, value: str = None, inline: bool = None) -> Form:
        self.form["embeds"][0]["fields"].append(
            {
                "name": name,
                "value": value,
                "inline": inline,
            }
        )
        return self

    def embeds_thumbnail(self, url: str = None) -> Form:
        self.form["embeds"][0]["thumbnail"] = {"url": url}
        return self

    def embeds_image(self, url: str = None) -> Form:
        self.form["embeds"][0]["image"] = {"url": url}
        return self

    def embeds_footer(self, text: str = None, icon_url: str = None) -> Form:
        self.form["embeds"][0]["footer"] = {"text": text, "icon_url": icon_url}
        return self

    def embeds_timestamp(self, timestamp: str = None) -> Form:
        self.form["embeds"][0]["timestamp"] = timestamp
        return self

    # Utility methods

    def post(self, url: str = None) -> None:
        requests.post(url, json=self.form)

    def embeds_fields_count(self) -> int:
        return len(self.form["embeds"][0]["fields"])
