"""Валидность EBNF-грамматики Avtandil."""

import pytest
from lark import Lark
from lark.exceptions import UnexpectedInput


def test_grammar_loads(grammar_text):
    """Грамматика должна загружаться без ошибок."""
    parser = Lark(grammar_text, start="program", parser="earley")
    assert parser is not None


def test_grammar_has_start_rule(grammar_text):
    """В грамматике должно быть правило program."""
    assert "program" in grammar_text


def test_grammar_has_no_undefined_rules(grammar_text):
    """Все используемые правила должны быть определены."""
    parser = Lark(grammar_text, start="program", parser="earley")
    assert parser is not None


def test_grammar_terminals_declared(grammar_text):
    """Все терминалы-операторы должны быть объявлены как правила."""
    required_terminals = [
        "OP_ADD", "OP_SUB", "OP_MUL", "OP_DIV",
        "OP_EQ", "OP_NEQ", "OP_APPROX", "OP_NOT_APPROX",
        "OP_LOOP", "OP_LOOP_INF", "OP_BREAK",
        "OP_PRINT", "OP_HELP", "OP_RANDOM", "OP_TIME",
        "OP_FUNC_DECL", "OP_RETURN",
        "OP_RE_FIND", "OP_RE_REPLACE",
        "OP_READ_STR", "OP_WRITE_STR",
        "OP_AUTOMATON",
    ]
    for terminal in required_terminals:
        assert terminal in grammar_text, f"Не объявлен терминал {terminal}"


def test_grammar_start_parses_empty_program(parser):
    """Пустая программа должна разбираться."""
    tree = parser.parse("")
    assert tree is not None


def test_grammar_rejects_garbage(parser):
    """Случайный текст не должен разбираться."""
    with pytest.raises(UnexpectedInput):
        parser.parse("@@@###$$$")
