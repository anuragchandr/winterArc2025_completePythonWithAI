import pytest
from db import Database
@pytest.fixture

def db():
    database = Database()
    yield database
    database.data.clear()

def test_add_user(db):
    db.add_user(1,"anurag")
    assert db.get_user(1) == "anurag"

def test_add_existing_user(db):
    db.add_user(1,"anurag")
    with pytest.raises(ValueError, match="User already exists"):
        db.add_user(1,"anurag")

def test_delete_user(db):
    db.add_user(2,"nrg")
    db.delete_user(2)
    assert db.get_user(2) is None