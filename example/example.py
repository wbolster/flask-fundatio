#!/usr/bin/env python

from flask import Flask, render_template
from flask_fundatio import Fundatio

app = Flask(__name__)
foundation = Fundatio(app)


@app.route('/')
def home():
    return render_template(
        'home.html',
        title='Flask-Fundatio demo',
    )


if __name__ == '__main__':
    app.run(debug=True)
