from setuptools import setup

setup(
    name='ookami-webhook',
    version='1.4',
    packages=['ookami'],
    url='https://github.com/tainn/ookami-webhook',
    license='GNU GPLv3',
    author='tainn',
    description='Explicit Discord webhook data manipulation',
    include_package_data=True,
    data_files=[('', ['ookami/form.json'])],
    install_requires=['requests']
)
