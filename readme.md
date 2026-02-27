# cordhook

Discord [webhook](https://discord.com/developers/docs/resources/webhook) data manipulation

Instead of having to manually build a deserialized `json` object, `cordhook` allows for explicit and flat declaration of
the payload data by calling of methods that populate their respective fields

## Install

Fetch the package via [uv](https://docs.astral.sh/uv)

```sh
uv pip install git+https://github.com/tainn/cordhook.git@0.2.10
```

## Usage

All attributes are optional. Multiple embeds can be populated in a single payload. Each method returns a class instance,
allowing for method chaining

### Example

A minimal example setting the `username`, `embed_color`, `embed_description` values and posting the webhook

```py
from cordhook import Form

form = Form()

form.username("kaonashi").embed_color(0000000).embed_description("...")
form.post("webhook-url")
```

### Form

The raw `json` form that is being populated through method calls
(source: [birdie0](https://birdie0.github.io/discord-webhooks-guide/discord_webhook.html))

```json
{
  "username": null,
  "avatar_url": null,
  "content": null,
  "tts": null,
  "embeds": [
    {
      "author": {
        "name": null,
        "url": null,
        "icon_url": null
      },
      "color": null,
      "title": null,
      "url": null,
      "description": null,
      "fields": [],
      "thumbnail": {
        "url": null
      },
      "image": {
        "url": null
      },
      "footer": {
        "text": null,
        "icon_url": null
      },
      "timestamp": null
    }
  ]
}
```
