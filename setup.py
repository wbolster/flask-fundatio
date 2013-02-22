from setuptools import setup

setup(
    name="Flask-Fundatio",
    version='0.1.dev',
    author="Wouter Bolsterlee",
    author_email="uws@xs4all.nl",
    url="https://github.com/wbolster/flask-fundatio",
    license="BSD",
    install_requires=[
        "Flask >= 0.9",
    ],
    packages=['flask_fundatio']
)
