"""Show debugger error on annotated test fixtures and pydantic models on python 3.14.

- create python 3.14 venv
- pip install -r requirement.txt
- debug tests with pytest in vscode test explorer
"""

import pytest
from pydantic import BaseModel


# Note that fixture without annotations won't raise exception
@pytest.fixture
def simple_fixture():
    return 42


# Raises exception
@pytest.fixture
def annotated_fixture(simple_fixture: int) -> str:
    return f"This is an annotated fixture with value {simple_fixture}"


# Raises exception
class AnnotatedTest(BaseModel):
    """A test class with annotated attributes."""

    name: str
    value: int


# Raises exception
def test_simple_fixture() -> None:
    assert 1 + 1 == 2
