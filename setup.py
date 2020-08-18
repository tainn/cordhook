from setuptools import setup

setup(
    name='ookami',
    version='1.3',
    packages=['ookami'],
    url='https://github.com/tainn/ookami',
    license='GNU GPLv3',
    author='tainn',
    author_email='tainn@protonmail.com',
    description='Explicit discord webhook data manipulation',
    include_package_data=True,
    data_files=[('', ['ookami/form.json'])],
    install_requires=['requests']
)
