# Ookami
A package written in Python that allows explicit manipulation of discord webhook data.

## Usage
Instead of having to manually build a deserialized `json` object and at that be careful of where certain keys are, `Ookami` allows for explicit declaration of the webhook data by calling of functions that populate their respective fields.

```
import requests, ookami

# Save a default deserialized json
form = ookami.load_form()

# We can apply attributes in-place
ookami.content(form=form, data='Hello!')
ookami.embeds_color(form=form, data=6921661)
ookami.embeds_title(form=form, data='Update')

# Ready to post
requests.post(webhook_url, json=form)
```
