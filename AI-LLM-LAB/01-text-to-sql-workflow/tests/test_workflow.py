import os
import pytest
from src.db_setup import setup_database
from src.workflow import TextToSQLWorkflow

@pytest.fixture
def setup_test_db():
    db_path = "data/test_university.db"
    setup_database(db_path)
    yield db_path
    if os.path.exists(db_path):
        os.remove(db_path)

def test_schema_retrieval(setup_test_db):
    workflow = TextToSQLWorkflow(db_path=setup_test_db, use_mock=True)
    schema = workflow.get_schema()
    assert "departments" in schema
    assert "students" in schema

def test_mock_sql_generation(setup_test_db):
    workflow = TextToSQLWorkflow(db_path=setup_test_db, use_mock=True)
    schema = workflow.get_schema()
    sql = workflow.generate_sql("Show the top 5 students by marks.", schema)
    assert "SELECT" in sql
    assert "ORDER BY marks DESC" in sql

def test_sql_execution(setup_test_db):
    workflow = TextToSQLWorkflow(db_path=setup_test_db, use_mock=True)
    results = workflow.execute_sql("SELECT name FROM departments WHERE id=1;")
    assert results[0][0] == "Computer Science"
