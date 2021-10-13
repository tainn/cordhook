import requests

from raw import raw_form


class Form:
    """
    Allows for explicit and flat creation, population and posting of a discord webhook
    - Segment 1 features: form population methods
    - Segment 2 features: utility methods
    """

    def __init__(self) -> None:
        """
        Loads the hard-coded raw form dict from the included raw module
        """
        self.form: dict = raw_form()

    # Segment 1

    def username(self, username: str = None) -> None:
        """
        :param username: overrides the current username of the webhook
        """
        self.form['username'] = username

    def avatar_url(self, avatar_url: str = None) -> None:
        """
        :param avatar_url: overrides the default avatar of the webhook
        """
        self.form['avatar_url'] = avatar_url

    def content(self, content: str = None) -> None:
        """
        :param content: a simple message, contains up to 2000 characters
        """
        self.form['content'] = content

    def tts(self, tts: bool = None) -> None:
        """
        :param tts: if True, the message will be pronounced in the chat like a tts message
        """
        self.form['tts'] = tts

    def embeds_author(self, name: str = None, url: str = None, icon_url: str = None) -> None:
        """
        Embed author object

        :param name: name of the author
        :param url: url of the author; if name was used it becomes a hyperlink
        :param icon_url: url of the author icon
        """
        self.form['embeds'][0]['author'] = {
            'name': name,
            'url': url,
            'icon_url': icon_url
        }

    def embeds_color(self, color: int = None) -> None:
        """
        :param color: color code of the embed (decimal numeral system is used, not hexa)
        """
        self.form['embeds'][0]['color'] = color

    def embeds_title(self, title: str = None) -> None:
        """
        :param title: title of the embed
        """
        self.form['embeds'][0]['title'] = title

    def embeds_url(self, url: str = None) -> None:
        """
        :param url: url of the embed; if title was used, it becomes a hyperlink
        """
        self.form['embeds'][0]['url'] = url

    def embeds_description(self, description: str = None) -> None:
        """
        :param description: description text
        """
        self.form['embeds'][0]['description'] = description

    def embeds_fields(self, name: str = None, value: str = None, inline: bool = None) -> None:
        """
        Array of embed field objects

        :param name: name of the field
        :param value: value of the field
        :param inline: inline option; if True, fields will be displayed in the same line
        """
        self.form['embeds'][0]['fields'].append(
            {
                'name': name,
                'value': value,
                'inline': inline
            }
        )

    def embeds_thumbnail(self, url: str = None) -> None:
        """
        :param url: embed thumbnail object
        """
        self.form['embeds'][0]['thumbnail'] = {'url': url}

    def embeds_image(self, url: str = None) -> None:
        """
        :param url: embed image object, includes an image url
        """
        self.form['embeds'][0]['image'] = {'url': url}

    def embeds_footer(self, text: str = None, icon_url: str = None) -> None:
        """
        Embed footer object

        :param text: footer text; does not support Markdown
        :param icon_url: url of the footer icon
        """
        self.form['embeds'][0]['footer'] = {
            'text': text,
            'icon_url': icon_url
        }

    def embeds_timestamp(self, timestamp: str = None) -> None:
        """
        :param timestamp: ISO8601 timestamp (yyyy-mm-ddThh:mm:ss.msZ)
        """
        self.form['embeds'][0]['timestamp'] = timestamp

    # Segment 2

    def post(self, url: str = None) -> None:
        """
        :param url: creates a post request on a provided webhook url
        """
        requests.post(url, json=self.form)

    def embeds_fields_count(self) -> int:
        """
        :return: the amount of elements in the embed fields list
        """
        return len(self.form['embeds'][0]['fields'])
