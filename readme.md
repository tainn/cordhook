# cordhook

a package that allows for explicit manipulation of discord webhook data

instead of having to manually build a deserialized `json` object and at that be careful of where certain keys
are, `cordhook` allows for explicit and flat declaration of the payload data by calling of methods that populate their
respective fields

## install

fetch the latest version of the package:

```console
python3 -m pip install git+https://github.com/tainn/cordhook.git@0.2.9
```

## usage

all attributes are optional. multiple embeds can be populated in a single payload. each method returns a class instance,
allowing for easy method chaining

### example

a minimal example setting the `username`, `embed_color`, `embed_description` values and posting the webhook:

```py
import cordhook

form = cordhook.Form()

form.username("Kaonashi").embed_color(0000000).embed_description("...")
form.post("webhook-url")
```

### form

for perspective, this is the raw form that is being populated through method calls:

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
