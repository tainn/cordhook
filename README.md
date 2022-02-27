# ookami-webhook

![package_version](https://img.shields.io/badge/package-1.9-b0c9ff)
![python_version](https://img.shields.io/badge/python-3.7-b0c9ff)

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

Metasyntactic variable names can be replaced with artibrary text, while explanatory strings have to be replaced with
specific values, such as links or timestamps.

All attributes are optional.

Each method returns a class instance, allowing for easy method chaining.

```py
import ookami

# Load a raw form
form = ookami.Form()

# We can apply attributes in-place
form.username(username='foo')
form.avatar_url(avatar_url='link-to-image')
form.content(content='bar')
form.tts(tts=False)

form.embeds_author(name='baz', url='link-to-page', icon_url='link-to-image')
form.embeds_color(color=6921661)  # Decimal, not hex
form.embeds_title(title='qux')
form.embeds_url(url='link-to-page')
form.embeds_description(description='quux')
form.embeds_fields(name='quuz', value='corge', inline=True)
form.embeds_thumbnail(url='link-to-image')
form.embeds_image(url='link-to-image')
form.embeds_footer(text='grault', icon_url='link-to-image')
form.embeds_timestamp(timestamp='yyyy-mm-ddThh:mm:ss.msZ')  # ISO8601 timestamp

# Ready to post
form.post('webhook-url')
```
