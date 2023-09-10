import os

import pytest


@pytest.fixture
def app(monkeypatch):
    db_path = os.path.abspath("test.db")
    monkeypatch.setenv('SQLALCHEMY_DATABASE_URI', f"sqlite:///{db_path}")
    from app.main import create_app
    app = create_app()
    return app


@pytest.fixture
def client(app):
    app.testing = True
    return app.test_client()
