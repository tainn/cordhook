# discord-webhook

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

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

The following values can be replaced with:

- `...`: artibrary text
- `image`: link to an image
- `page`: link to a page
- `0000000`: decimal color value, not hex
- `bool`: opposite bool
- `timestamp`: ISO8601 timestamp
- `webhook`: webhook url

All attributes are optional. Only a single element of an embed is currently supported. Each method returns a class
instance, allowing for easy method chaining.

```py
import cordhook

# Load a raw form
form = cordhook.Form()

# We can apply attributes in-place
form.username(username="...")
form.avatar_url(avatar_url="image")
form.content(content="...")
form.tts(tts=False)

form.embeds_author(name="...", url="page", icon_url="image")
form.embeds_color(color=0000000)
form.embeds_title(title="...")
form.embeds_url(url="page")
form.embeds_description(description="...")
form.embeds_fields(name="...", value="...", inline=True)
form.embeds_thumbnail(url="image")
form.embeds_image(url="image")
form.embeds_footer(text="...", icon_url="image")
form.embeds_timestamp(timestamp="timestamp")

# Ready to post
form.post("webhook")
```

## Form

For perspective, this is the raw form that is being populated through method calls:

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
