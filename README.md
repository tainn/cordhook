# Ookami
![Version](https://img.shields.io/badge/version-v1.2-blue)
![License](https://img.shields.io/badge/license-GPLv3-orange)

A package written in Python that allows explicit manipulation of discord webhook data.

## Install
`pip3 install --user git+git://github.com/tainn/ookami.git`

## Usage
Instead of having to manually build a deserialized `json` object and at that be careful of where certain keys are, `Ookami` allows for explicit declaration of the webhook data by calling of methods that populate their respective fields.

```py
import ookami

# Save a default deserialized json object
form = ookami.Ookami()

# We can apply attributes in-place
form.content('Hello!')
form.embeds_color(6921661)
form.embeds_title('Update')

# Ready to post
form.post(webhook_url)
```
