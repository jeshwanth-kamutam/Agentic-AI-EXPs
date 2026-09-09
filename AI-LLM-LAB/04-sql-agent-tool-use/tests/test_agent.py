from src.tools import SQLTools
from src.db_setup import setup_database
import os
import pytest

@pytest.fixture
def setup_test_db():
    db_path = "data/test_store.db"
    setup_database(db_path)
    yield db_path
    if os.path.exists(db_path):
        os.remove(db_path)

def test_list_tables(setup_test_db):
    tools = SQLTools(db_path=setup_test_db)
    tables = tools.list_tables()
    assert "products" in tables

def test_execute_sql(setup_test_db):
    tools = SQLTools(db_path=setup_test_db)
    res = tools.execute_sql("SELECT name FROM products WHERE id=1")
    assert "Laptop" in res
