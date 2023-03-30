# discord-webhook

[![Code style: black](https://img.shields.io/badge/style-black-000000.svg)](https://github.com/psf/black)

A package that allows for explicit manipulation of Discord webhook data.

Instead of having to manually build a deserialized `json` object and at that be careful of where certain keys
are, `cordhook` allows for explicit and flat declaration of the payload data by calling of methods that populate their
respective fields.

## Install

Fetch the latest version of the package:

```sh
pip3 install --upgrade git+https://github.com/tainn/discord-webhook.git
```

## Usage

All attributes are optional. Multiple embeds can be populated in a single payload. Each method returns a class instance,
allowing for easy method chaining.

### Example

A minimal example setting the `username`, `embed_color` and `embed_description` values and posting the webhook.

```py
import cordhook

# Load a raw form
form = cordhook.Form()

# Apply changes in-place
form.username("Kaonashi").embed_color(0000000).embed_description("...")

# Ready to post
form.post("webhook-url")
```

### Reference

A table featuring all available methods, their types, parameters and further info.

| method   | type    | param: type                                 | comment          |
|----------|---------|---------------------------------------------|------------------|
| `username` | content | `username: str`                             ||
| `avatar_url` | content | `avatar_url: str`                           ||
| `content` | content | `content: str`                              ||
| `tts` | content | `tts: bool`                                 ||
| `embed_author` | content | `name: str` :: `url: str` :: `icon_url: str` ||
| `embed_color` | content | `color: int`                                | decimal, not hex |
| `embed_title` | content | `title: str`                                ||
| `embed_url` | content | `url: str`                                  ||
| `embed_description` | content | `description: str`                          ||
| `embed_fields` | content | `name: str` :: `value: str` :: `inline: bool` ||
| `embed_thumbnail` | content | `url: str`                                  ||
| `embed_image` | content | `url: str`                                  ||
| `embed_footer` | content | `text: str` :: `icon_url: str`              ||
| `embed_timestamp` | content | `timestamp: str`                            | ISO8601          |
| `embed_fields_count` | utility ||
| `embeds_count` | utility ||
| `next_active_embed` | utility ||
| `change_active_embed` | utility | `embed: int`                                ||
| `post` | request | `webhook: str`                 | can be iterable  |

### Form

For perspective, this is the raw form that is being populated through method calls.

```py
{
    "username": None,
    "avatar_url": None,
    "content": None,
    "tts": None,
    "embeds": [
        {
            "author": {
                "name": None,
                "url": None,
                "icon_url": None
            },
            "color": None,
            "title": None,
            "url": None,
            "description": None,
            "fields": [],
            "thumbnail": {
                "url": None
            },
            "image": {
                "url": None
            },
            "footer": {
                "text": None,
                "icon_url": None
            },
            "timestamp": None
        }
    ]
}
```
