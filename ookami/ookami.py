# Ookami

import os
import json
import requests


class Ookami:
    """Allows for explicit creation, population and posting of a discord webhook"""

    def __init__(self):
        """Loads the json form and creates a deserialized object"""

        ookami_dir = os.path.dirname(__file__)
        form_file = os.path.join(ookami_dir, 'form.json')

        with open(form_file, 'r') as jf:
            self.form = json.load(jf)

    def post(self, url: str = None):
        """Creates a post request on a provided webhook url"""

        requests.post(url, json=self.form)

    def username(self, data: str = None):
        """Overrides the current username of the webhook"""

        self.form['username'] = data

    def avatar_url(self, data: str = None):
        """Overrides the default avatar of the webhook"""

        self.form['avatar_url'] = data

    def content(self, data: str = None):
        """A simple message, contains up to 2000 characters"""

        self.form['content'] = data

    def tts(self, data: bool = None):
        """If True, the message will be pronounced in the chat like a tts message"""

        self.form['tts'] = data

    def embeds_author(self, name: str = None, url: str = None, icon_url: str = None):
        """Embed author object, includes:
        Name of the author,
        Url of the author; if name was used it becomes a hyperlink,
        Url of the author icon"""

        self.form['embeds'][0]['author'] = {'name': name,
                                            'url': url,
                                            'icon_url': icon_url}

    def embeds_color(self, data: int = None):
        """Color code of the embed; decimal numeral system is used, not hexadecimal"""

        self.form['embeds'][0]['color'] = data

    def embeds_title(self, data: str = None):
        """Title of the embed"""

        self.form['embeds'][0]['title'] = data

    def embeds_url(self, data: str = None):
        """Url of the embed; if title was used, it becomes a hyperlink"""

        self.form['embeds'][0]['url'] = data

    def embeds_description(self, data: str = None):
        """Description text"""

        self.form['embeds'][0]['description'] = data

    def embeds_fields(self, name: str = None, value: str = None, inline: bool = None):
        """Array of embed field objects, each element includes:
        Name of the field,
        Value of the field,
        Inline option; if True, fields will be displayed in the same line"""

        self.form['embeds'][0]['fields'].append({'name': name,
                                                 'value': value,
                                                 'inline': inline})

    def embeds_fields_count(self):
        """Returns the amount of elements in the embed fields list"""

        return len(self.form['embeds'][0]['fields'])

    def embeds_thumbnail(self, url: str = None):
        """Embed thumbnail object"""

        self.form['embeds'][0]['thumbnail'] = {'url': url}

    def embeds_image(self, url: str = None):
        """Embed image object, includes an image url"""

        self.form['embeds'][0]['image'] = {'url': url}

    def embeds_footer(self, text: str = None, icon_url: str = None):
        """Embed footer object, includes:
        Footer text; does not support Markdown,
        Url of the footer icon"""

        self.form['embeds'][0]['footer'] = {'text': text,
                                            'icon_url': icon_url}

    def embeds_timestamp(self, data: str = None):
        """ISO8601 timestamp (yyyy-mm-ddThh:mm:ss.msZ)"""

        self.form['embeds'][0]['timestamp'] = data
