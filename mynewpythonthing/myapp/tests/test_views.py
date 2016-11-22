# -*- coding: utf-8 -*-
from flask import url_for


def test_myapp_index(client):
    res = client.get(url_for('myapp_app.index'))
    assert res.data == b'Hello World!'
