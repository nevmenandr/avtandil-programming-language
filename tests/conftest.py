"""Общие фикстуры для тестов грамматики Avtandil."""

from pathlib import Path

import pytest
from lark import Lark

GRAMMAR_PATH = Path(__file__).parent.parent / "pythondil" / "parser" / "avtandil.ebnf"
FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture(scope="session")
def grammar_text() -> str:
    """Текст EBNF-грамматики Avtandil."""
    return GRAMMAR_PATH.read_text(encoding="utf-8")


@pytest.fixture(scope="session")
def parser(grammar_text: str) -> Lark:
    """Парсер Avtandil, построенный по канонической грамматике."""
    return Lark(grammar_text, start="program", parser="earley", lexer="dynamic_complete")


@pytest.fixture(scope="session")
def valid_dir() -> Path:
    return FIXTURES / "valid"


@pytest.fixture(scope="session")
def invalid_dir() -> Path:
    return FIXTURES / "invalid"
