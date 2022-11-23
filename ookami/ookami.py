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
        """Overrides the current username of the webhook."""

        self.form["username"] = username
        return self

    def avatar_url(self, avatar_url: str = None) -> Form:
        """Overrides the default avatar of the webhook."""

        self.form["avatar_url"] = avatar_url
        return self

    def content(self, content: str = None) -> Form:
        """Sets a simple message that contains up to 2000 characters."""

        self.form["content"] = content
        return self

    def tts(self, tts: bool = None) -> Form:
        """If True, the message will be pronounced in the chat like a tts message."""

        self.form["tts"] = tts
        return self

    def embeds_author(self, name: str = None, url: str = None, icon_url: str = None) -> Form:
        """Sets the embed author object. If name is used, url becomes a hyperlink."""

        self.form["embeds"][0]["author"] = {
            "name": name,
            "url": url,
            "icon_url": icon_url,
        }
        return self

    def embeds_color(self, color: int = None) -> Form:
        """Sets the color of the embed via a color code (decimal numeral system is used, not hexa)."""

        self.form["embeds"][0]["color"] = color
        return self

    def embeds_title(self, title: str = None) -> Form:
        """Sets a title of the embed."""

        self.form["embeds"][0]["title"] = title
        return self

    def embeds_url(self, url: str = None) -> Form:
        """Sets an url of the embed: if title was used it becomes a hyperlink."""

        self.form["embeds"][0]["url"] = url
        return self

    def embeds_description(self, description: str = None) -> Form:
        """Sets a description."""

        self.form["embeds"][0]["description"] = description
        return self

    def embeds_fields(self, name: str = None, value: str = None, inline: bool = None) -> Form:
        """Sets an array of embed field objects."""

        self.form["embeds"][0]["fields"].append(
            {
                "name": name,
                "value": value,
                "inline": inline,
            }
        )
        return self

    def embeds_thumbnail(self, url: str = None) -> Form:
        """Sets an embed thumbnail."""

        self.form["embeds"][0]["thumbnail"] = {"url": url}
        return self

    def embeds_image(self, url: str = None) -> Form:
        """Sets an embed image."""

        self.form["embeds"][0]["image"] = {"url": url}
        return self

    def embeds_footer(self, text: str = None, icon_url: str = None) -> Form:
        """Sets an embed footer, does not support Markdown."""

        self.form["embeds"][0]["footer"] = {"text": text, "icon_url": icon_url}
        return self

    def embeds_timestamp(self, timestamp: str = None) -> Form:
        """Sets a timestamp, ISO8601 timestamp (yyyy-mm-ddThh:mm:ss.msZ)."""

        self.form["embeds"][0]["timestamp"] = timestamp
        return self

    # Utility methods

    def post(self, url: str = None) -> None:
        """Creates a post request on a provided webhook url."""

        requests.post(url, json=self.form)

    def embeds_fields_count(self) -> int:
        """Counts the amount of elements in the embed fields list."""

        return len(self.form["embeds"][0]["fields"])
