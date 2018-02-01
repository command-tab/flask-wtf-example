#!/usr/bin/env python

from app import app
import click
from flask.cli import FlaskGroup


def create_app(info):
    # I normally set up  Flask-Migrate here
    return app


@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    """
    A management script for the Flask application.
    """


if __name__ == '__main__':
    cli()
