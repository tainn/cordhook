from setuptools import setup

setup(
    name='ookami',
    version='1.0',
    packages=['ookami'],
    url='https://github.com/tainn1/ookami',
    license='GNU GPLv3',
    author='tainn',
    author_email='tainn@protonmail.com',
    description='Explicit discord webhook data manipulation',
    include_package_data=True,
    data_files=[('', ['ookami/form.json'])]
)
