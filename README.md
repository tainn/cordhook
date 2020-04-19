# Ookami
![Version](https://img.shields.io/badge/version-v1.2-blue)
![License](https://img.shields.io/badge/license-GPLv3-orange)

`Ookami` is a package written in Python that allows for explicit manipulation of discord webhook data.

Instead of having to manually build a deserialized `json` object and at that be careful of where certain keys are, `Ookami` allows for explicit declaration of the webhook data by calling of methods that populate their respective fields.

## Install
`pip3 install --user git+git://github.com/tainn/ookami.git`

## Usage
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
