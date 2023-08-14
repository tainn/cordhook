from setuptools import setup

setup(
    name="discord-webhook",
    version="2.4",
    packages=["cordhook"],
    url="https://github.com/tainn/discord-webhook",
    license="MIT",
    author="tainn",
    description="Explicit Discord webhook data manipulation",
    install_requires=["httpx==0.23.3"],
)
