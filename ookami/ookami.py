# Ookami

import os
import json


def load_form() -> dict:
    """Loads the json form and retuns a deserialized object"""
    ookami_dir = os.path.dirname(__file__)
    form_file = os.path.join(ookami_dir, 'form.json')

    with open(form_file, 'r') as jf:
        form = json.load(jf)

    return form


def dumps_form(form: dict) -> str:
    """Dumps the json form and retuns a serialized object"""
    return json.dumps(form)


def username(form: dict, data: str = None):
    """Overrides the current username of the webhook"""
    form['username'] = data


def avatar_url(form: dict, data: str = None):
    """Overrides the default avatar of the webhook"""
    form['avatar_url'] = data


def content(form: dict, data: str = None):
    """A simple message, contains up to 2000 characters"""
    form['content'] = data


def tts(form: dict, data: bool = None):
    """If True, the message will be pronounced in the chat like a tts message"""
    form['tts'] = data


def embeds_author(form: dict, data_name: str = None, data_url: str = None, data_icon_url: str = None):
    """Embed author object, includes:
    Name of the author,
    Url of the author. If name was used, it becomes a hyperlink,
    Url of the author icon"""
    form['embeds'][0]['author'] = {'name': data_name,
                                   'url': data_url,
                                   'icon_url': data_icon_url}


def embeds_color(form: dict, data: int = None):
    """Color code of the embed. Decimal numeral system is used, not hexadecimal"""
    form['embeds'][0]['color'] = data


def embeds_title(form: dict, data: str = None):
    """Title of the embed"""
    form['embeds'][0]['title'] = data


def embeds_url(form: dict, data: str = None):
    """Url of the embed. If title was used, it becomes a hyperlink"""
    form['embeds'][0]['url'] = data


def embeds_description(form: dict, data: str = None):
    """Description text"""
    form['embeds'][0]['description'] = data


def embeds_fields(form: dict, data_name: str = None, data_value: str = None, data_inline: bool = None):
    """Array of embed field objects, each element includes:
    Name of the field,
    Value of the field,
    Inline option. If True, fields will be displayed in the same line"""
    form['embeds'][0]['fields'].append({'name': data_name,
                                        'value': data_value,
                                        'inline': data_inline})


def embeds_thumbnail(form: dict, data_url: str = None):
    """Embed thumbnail object"""
    form['embeds'][0]['thumbnail'] = {'url': data_url}


def embeds_image(form: dict, data_url: str = None):
    """Embed image object, includes:
    Image url"""
    form['embeds'][0]['image'] = {'url': data_url}


def embeds_footer(form: dict, data_text: str = None, data_icon_url: str = None):
    """Embed footer object, includes:
    Footer text. Does not support Markdown,
    Url of the footer icon"""
    form['embeds'][0]['footer'] = {'text': data_text,
                                   'icon_url': data_icon_url}


def embeds_timestamp(form: dict, data: str = None):
    """ISO8601 timestamp (yyyy-mm-ddThh:mm:ss.msZ)"""
    form['embeds'][0]['timestamp'] = data
