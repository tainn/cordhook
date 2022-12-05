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
- `1`: arbitrary integer
- `image`: link to an image
- `page`: link to a page
- `0000000`: decimal color value, not hex
- `bool`: opposite bool
- `timestamp`: ISO8601 timestamp
- `webhook`: webhook url

All attributes are optional. Multiple embeds can be populated in a single payload. Each method returns a class instance,
allowing for easy method chaining.

```py
import cordhook

# Load a raw form
form = cordhook.Form()

# We can apply attributes in-place
form.username(username="...")
form.avatar_url(avatar_url="image")
form.content(content="...")
form.tts(tts=False)

form.embed_author(name="...", url="page", icon_url="image")
form.embed_color(color=0000000)
form.embed_title(title="...")
form.embed_url(url="page")
form.embed_description(description="...")
form.embed_fields(name="...", value="...", inline=True)
form.embed_thumbnail(url="image")
form.embed_image(url="image")
form.embed_footer(text="...", icon_url="image")
form.embed_timestamp(timestamp="timestamp")

# Utility methods
form.embed_fields_count()
form.embeds_count()
form.next_active_embed()
form.change_active_embed(embed=1)

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
