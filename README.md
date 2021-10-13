# ookami-webhook

A package written in Python that allows for explicit manipulation of Discord webhook data.

Instead of having to manually build a deserialized `json` object and at that be careful of where certain keys
are, `ookami` allows for explicit and flat declaration of the webhook data by calling of methods that populate their
respective fields.

## Install

Fetch the latest version of the package

```sh
pip3 install --user --upgrade git+git://github.com/tainn/ookami-webhook.git
```

## Usage

A collection of all keys is available in the constructor.

```py
import ookami

# Load a raw form
form = ookami.Form()

# We can apply attributes in-place
form.content('Hello!')
form.embeds_color(6921661)
form.embeds_title('Update')

# Ready to post
form.post(webhook_url)
```
