"""Полнота грамматики: все разделы языка должны быть описаны."""

import pytest

REQUIRED_RULES = {
    "арифметика": ["OP_ADD", "OP_SUB", "OP_MUL", "OP_DIV",
                    "OP_CHI2", "OP_CORR", "OP_PERCENT"],
    "условия": ["OP_EQ", "OP_NEQ", "OP_APPROX", "OP_NOT_APPROX",
                 "OP_GT", "OP_EVEN", "OP_ODD"],
    "циклы": ["OP_LOOP", "OP_LOOP_INF", "OP_LOOP_WORDS", "OP_LOOP_CHARS",
              "OP_REVERSE", "OP_BREAK"],
    "строки": ["OP_SPLIT", "OP_SPLIT_WORDS", "OP_SPLIT_SENTS",
               "OP_JOIN", "OP_CUT", "OP_LEN", "OP_FIND",
               "OP_REPLACE", "OP_STRIP_PUNCT", "OP_LOWER",
               "OP_CYRILLIC", "OP_INTERP"],
    "тексты": ["TEXT_TITLE", "TEXT_SUBTITLE", "TEXT_AUTHOR",
               "TEXT_PARAGRAPH", "TEXT_ABZAC", "TEXT_SIGNATURE"],
    "массивы": ["ARRAY_DECL", "OP_SORT", "OP_REVERSE_ARR",
                "OP_DEL_ELEM", "OP_APPEND", "OP_INSERT",
                "OP_ASSOC", "OP_INDEX"],
    "регулярные_выражения": ["OP_RE_FIND", "OP_RE_REPLACE"],
    "файлы": ["OP_READ_STR", "OP_READ_ARR", "OP_READ_CSV",
              "OP_READ_XML", "OP_WRITE_STR", "OP_WRITE_BIN",
              "OP_WRITE_TABLE", "OP_WRITE_MD", "OP_WRITE_XML"],
    "встроенные_функции": ["OP_PRINT", "OP_HELP", "OP_RANDOM",
                            "OP_TIME", "OP_ROMAN_DATE", "OP_HUMAN_TIME"],
    "пользовательские_функции": ["OP_FUNC_DECL", "OP_RETURN"],
    "комментарии": ["COMMENT"],
    "сообщение_об_ошибке": ["OP_ERROR"],
    "высокоуровневые": ["OP_FREQ", "OP_TFIDF", "OP_TTR",
                         "OP_WEB_STR", "OP_WEB_TEXT", "OP_WEB_ARR",
                         "OP_WEB_BIN", "OP_WEB_SITE", "OP_WIKIPEDIA",
                         "OP_PGN_LOAD", "OP_PGN_META", "OP_PGN_BOARD",
                         "OP_ML_TRAIN", "OP_ML_TARGET", "OP_ML_SAVE",
                         "OP_ML_PREDICT", "OP_DELTA", "OP_TOPIC",
                         "OP_GRAPH_CREATE", "OP_GRAPH_RANK",
                         "OP_GRAPH_CLUST"],
    "конечные_автоматы": ["OP_AUTOMATON", "TRI_START", "TRI_MID",
                           "TRI_ACCEPT", "TRI_SKIP", "TRI_REPEAT",
                           "TRI_RECORD", "TRI_CHECK", "TRI_ERROR"],
}


@pytest.mark.parametrize("section,rules", REQUIRED_RULES.items())
def test_section_rules_present(grammar_text, section, rules):
    """Каждый раздел языка должен иметь объявленные правила."""
    for rule in rules:
        assert rule in grammar_text, (
            f"Раздел «{section}»: отсутствует правило {rule}"
        )


def test_all_readme_operators_in_grammar(grammar_text):
    """Все операторы из README должны присутствовать в грамматике."""
    readme_operators = [
        "⋈", "⚘", "🕮", "ᜈ", "∅",
        "ᛝ", "ᚸ", "ᛪ", "ᛄ",
        "Ⰺ", "ᬈ", "ѯ",
        "𐄷", "𑚐", "≈", "≉", "អ", "᭕", "ゅ",
        "⊹", "ਊ", "ສ", "𑚉", "Ⱗ", "𑜐",
        "𐂅", "♖",
        "沙", "𑜱", "ま", "𐎺", "✂", "ᕘ",
        "🔍︎", "ဠ", "𑜹", "𐃨", "平", "Җ", "☘", "▣",
        "𐂲", "ҙ", "ভ", "§", "¶", "𐄨",
        "金", "ʡ", "խ", "⟴", "ᙴ", "ਲ", "👁",
        "ɲ", "▧",
        "✯", "𐊚", "⠝", "ཀོ", "𑜸", "℔", "⠞", "ℌ", "ᜁ",
        "✎", "⚜", "ᜅᜒ", "ῷ", "ℕ", "Ѧ", "𐃰",
        "❃", "𑚟",
        "❦",
        "☹",
        "◈", "𐂓", "į",
        "⌘", "枼", "𐊙", "𐃏", "⚛",
        "☯",
        "अ", "☪", "⅊",
        "❂", "☀", "ଫ", "ល",
        "𑜗",
        "◎",
        "☍", "⊷", "ଝ",
        "▞", "☰", "☱", "☲", "☳", "☴", "☵", "☶", "☷",
    ]
    missing = [op for op in readme_operators if op not in grammar_text]
    assert not missing, f"В грамматике отсутствуют операторы: {missing}"
