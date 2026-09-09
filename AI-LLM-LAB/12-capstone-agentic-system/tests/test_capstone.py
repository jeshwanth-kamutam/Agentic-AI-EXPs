from src.capstone import MasterAgent, SQLAgent
from src.db_setup import setup_database
import os
import pytest

@pytest.fixture
def setup_test_db():
    db_path = "data/test_enterprise.db"
    setup_database(db_path)
    yield db_path
    if os.path.exists(db_path):
        os.remove(db_path)

def test_sql_agent(setup_test_db):
    agent = SQLAgent(db_path=setup_test_db)
    res = agent.get_salary("Alice")
    assert res[0] == "Engineering"
    assert res[1] == 120000

def test_master_agent(setup_test_db):
    agent = MasterAgent()
    agent.sql.db_path = setup_test_db
    res = agent.process("What is Alice's bonus?")
    assert "$12000.0" in res
