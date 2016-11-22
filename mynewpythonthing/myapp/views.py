# -*- coding: utf-8 -*-
from flask import Blueprint

__all__ = ['myapp_app']

myapp_app = Blueprint('myapp_app', __name__)


@myapp_app.route('/')
def index():
    return "Hello World!"
