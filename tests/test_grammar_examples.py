"""Разбор примеров программ на Avtandil."""

from pathlib import Path

import pytest
from lark.exceptions import UnexpectedInput

EXAMPLES = Path(__file__).parent.parent / "examples"


@pytest.mark.parametrize("example", sorted(EXAMPLES.glob("*.avt")))
def test_example_parses(parser, example):
    """Каждый пример должен разбираться без ошибок."""
    code = example.read_text(encoding="utf-8")
    tree = parser.parse(code)
    assert tree is not None


@pytest.mark.parametrize("example", sorted(EXAMPLES.glob("*.avt")))
def test_example_not_empty(parser, example):
    """Каждый пример должен содержать хотя бы одну инструкцию."""
    code = example.read_text(encoding="utf-8").strip()
    assert code, f"Пример {example.name} пуст"


def test_valid_fixtures_parse(parser, valid_dir):
    """Все валидные фикстуры должны разбираться."""
    for fixture in valid_dir.glob("*.avt"):
        code = fixture.read_text(encoding="utf-8")
        parser.parse(code)


def test_invalid_fixtures_rejected(parser, invalid_dir):
    """Все невалидные фикстуры должны отвергаться."""
    for fixture in invalid_dir.glob("*.avt"):
        code = fixture.read_text(encoding="utf-8")
        with pytest.raises(UnexpectedInput):
            parser.parse(code)
