from __future__ import annotations

import requests


class Form:
    """Allows for explicit and flat creation, population and posting of a discord webhook."""

    def __init__(self) -> None:
        """Sets the hard-coded form dict."""

        self.form: dict = {
            'username': None,
            'avatar_url': None,
            'content': None,
            'tts': None,
            'embeds': [
                {
                    'author': {
                        'name': None,
                        'url': None,
                        'icon_url': None
                    },
                    'color': None,
                    'title': None,
                    'url': None,
                    'description': None,
                    'fields': [],
                    'thumbnail': {
                        'url': None
                    },
                    'image': {
                        'url': None
                    },
                    'footer': {
                        'text': None,
                        'icon_url': None
                    },
                    'timestamp': None
                }
            ]
        }

    # Form population methods

    def username(self, username: str = None) -> Form:
        """Overrides the current username of the webhook.

        :param username: specified username
        """
        self.form['username'] = username
        return self

    def avatar_url(self, avatar_url: str = None) -> Form:
        """Overrides the default avatar of the webhook.

        :param avatar_url: url to the avatar
        """
        self.form['avatar_url'] = avatar_url
        return self

    def content(self, content: str = None) -> Form:
        """Sets a simple message that contains up to 2000 characters.

        :param content: content of the message
        """
        self.form['content'] = content
        return self

    def tts(self, tts: bool = None) -> Form:
        """If True, the message will be pronounced in the chat like a tts message.

        :param tts: bool switch for pronounciation
        """
        self.form['tts'] = tts
        return self

    def embeds_author(self, name: str = None, url: str = None, icon_url: str = None) -> Form:
        """Sets the embed author object.

        :param name: name of the author
        :param url: url of the author: if name was used it becomes a hyperlink
        :param icon_url: url of the author icon
        """
        self.form['embeds'][0]['author'] = {
            'name': name,
            'url': url,
            'icon_url': icon_url
        }
        return self

    def embeds_color(self, color: int = None) -> Form:
        """Sets the color of the embed via a color code (decimal numeral system is used, not hexa).

        :param color: the color code
        """
        self.form['embeds'][0]['color'] = color
        return self

    def embeds_title(self, title: str = None) -> Form:
        """Sets a title of the embed.

        :param title: title of the embed
        """
        self.form['embeds'][0]['title'] = title
        return self

    def embeds_url(self, url: str = None) -> Form:
        """Sets an url of the embed: if title was used it becomes a hyperlink.

        :param url: url of the embed
        """
        self.form['embeds'][0]['url'] = url
        return self

    def embeds_description(self, description: str = None) -> Form:
        """Sets a description.

        :param description: description text
        """
        self.form['embeds'][0]['description'] = description
        return self

    def embeds_fields(self, name: str = None, value: str = None, inline: bool = None) -> Form:
        """Sets an array of embed field objects.

        :param name: name of the field
        :param value: value of the field
        :param inline: inline option: if True, fields will be displayed in the same line
        """
        self.form['embeds'][0]['fields'].append(
            {
                'name': name,
                'value': value,
                'inline': inline
            }
        )
        return self

    def embeds_thumbnail(self, url: str = None) -> Form:
        """Sets an embed thumbnail.

        :param url: embed thumbnail object
        """
        self.form['embeds'][0]['thumbnail'] = {'url': url}
        return self

    def embeds_image(self, url: str = None) -> Form:
        """Sets an embed image.

        :param url: embed image object, includes an image url
        """
        self.form['embeds'][0]['image'] = {'url': url}
        return self

    def embeds_footer(self, text: str = None, icon_url: str = None) -> Form:
        """Sets an embed footer.

        :param text: footer text: does not support Markdown
        :param icon_url: url of the footer icon
        """
        self.form['embeds'][0]['footer'] = {
            'text': text,
            'icon_url': icon_url
        }
        return self

    def embeds_timestamp(self, timestamp: str = None) -> Form:
        """Sets a timestamp.

        :param timestamp: ISO8601 timestamp (yyyy-mm-ddThh:mm:ss.msZ)
        """
        self.form['embeds'][0]['timestamp'] = timestamp
        return self

    # Utility methods

    def post(self, url: str = None) -> None:
        """Creates a post request on a provided webhook url.

        :param url: webhook url
        """
        requests.post(url, json=self.form)

    def embeds_fields_count(self) -> int:
        """Counts the amount of elements in the embed fields list.

        :return: the count
        """
        return len(self.form['embeds'][0]['fields'])
