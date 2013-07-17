from setuptools import setup

setup(
    name="Flask-Fundatio",
    description=("Flask extension to integrate the Foundation "
                 "front-end framework"),
    version='0.1',
    author="Wouter Bolsterlee",
    author_email="uws@xs4all.nl",
    url="https://github.com/wbolster/flask-fundatio",
    license="BSD",
    install_requires=[
        "Flask >= 0.9",
    ],
    packages=['flask_fundatio'],
    include_package_data=True,
)
