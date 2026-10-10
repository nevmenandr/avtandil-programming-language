"""Проверка отдельных правил грамматики."""

import pytest
from lark.exceptions import UnexpectedInput


# --- Присваивание ---

def test_assignment_parses(parser):
    parser.parse("praesens 5")


def test_assignment_from_variable(parser):
    parser.parse("orationem fines")


def test_assignment_from_builtin(parser):
    parser.parse("urbi ᜅᜒ")


# --- Арифметика ---

def test_arithmetic_addition(parser):
    parser.parse("ᛝ 2 3")


def test_arithmetic_with_variable(parser):
    parser.parse("bonus ᛝ 2 3 12")


def test_arithmetic_division_by_zero(parser):
    parser.parse("postremo ᛄ 10 0")


def test_chi2(parser):
    parser.parse("Ⰺ 113 144 125 129")


def test_correlation(parser):
    parser.parse("✎ ᬈ maiores singulorum")


def test_percent(parser):
    parser.parse("✎ ѯ 100 13")


# --- Условия ---

def test_equality(parser):
    parser.parse("metum 5\n𐄷 metum 3 ✎ Значения равны")


def test_inequality(parser):
    parser.parse("dominum 5\n𑚐 dominum 3 ✎ Значения не равны")


def test_nested_conditions(parser):
    code = (
        "dicendi 5\n"
        "𐄷 dicendi 3 ✎ Значение переменной равно 3\n"
        "𑚐 𐄷 dicendi 7 ✎ Значение переменной равно 7\n"
        "𑚐 ✎ Значение переменной не равно ни одному из известных значений"
    )
    parser.parse(code)


def test_approx_equality(parser):
    parser.parse("≈ 5 6 ✎ Числа приблизительно равны")


def test_greater_than(parser):
    parser.parse(
        "priusquam 5\nfaciunt 3\n"
        "អ priusquam faciunt ✎ Число ☘ priusquam больше"
    )


def test_even(parser):
    parser.parse("᭕ 14 ✎ Число четное")


def test_odd(parser):
    parser.parse("longius 5\nゅ longius ✎ Число ☘ longius нечетное")


# --- Циклы ---

def test_loop_count(parser):
    parser.parse("⊹ 4 ✎ итерация")


def test_loop_array(parser):
    parser.parse("⊹ 『20 13 21 42』 ✎ ♖")


def test_loop_infinite(parser):
    parser.parse("ਊ\n𑜐")


def test_loop_words(parser):
    parser.parse("fratres Мама мыла раму\nສ fratres ✎ ♖")


def test_loop_chars(parser):
    parser.parse("possis Вавилон\n𑚉 possis ✎ ♖")


# --- Строки ---

def test_string_declaration(parser):
    parser.parse("⚘ officium")


def test_string_multiline(parser):
    code = (
        "certum et leni coepit pandere vela Noto.\n"
        "Ast ubi paulatim praeceps audacia crevit\n"
        "⚘\n"
    )
    parser.parse(code)


def test_split(parser):
    parser.parse("honores Бобэоби пелись губы\n沙 б honores")


def test_split_words(parser):
    parser.parse("voluit Сторож курил\n𑜱 voluit")


def test_split_sentences(parser):
    parser.parse(
        "auxilium «Не шутите». Он не может понять.\n"
        "consulis ま auxilium"
    )


def test_join(parser):
    parser.parse("✎ 𐎺 ▣ 『20 13 21 42』")


def test_join_with_separator(parser):
    parser.parse("✎ 𐎺 - 『Диковины среднего возраста』")


def test_cut(parser):
    parser.parse("romanorum repente ✂ 55 placet")


def test_length(parser):
    parser.parse("✎ ᕘ deorum")


def test_find(parser):
    parser.parse("rerum quae 🔍︎ arma verum")


def test_replace(parser):
    parser.parse("accessit ဠ iussi montibus animi")


def test_strip_punctuation(parser):
    parser.parse("✎ 𑜹 senatus")


def test_lower(parser):
    parser.parse("✎ 平 locum")


def test_cyrillic(parser):
    parser.parse("✎ Җ ager")


def test_interpolation(parser):
    parser.parse("✎ Цицерон ☘ nomen ☘ cognomen")


# --- Тексты ---

def test_text_declaration(parser):
    code = (
        "libellus 🕮\n"
        "𐂲 О происхождении видов\n"
        "ҙ Издание второе\n"
        "ভ Чарлз Дарвин\n"
        "§ Введение\n"
        "¶ Когда мы смотрим на бесконечное разнообразие...\n"
        "𐄨 Лондон, 1859\n"
    )
    parser.parse(code)


# --- Массивы ---

def test_array_empty(parser):
    parser.parse("ᜈ vacua")


def test_array_nonempty(parser):
    parser.parse("ᜈ numeri 『20 13 21 42』")


def test_array_of_variables(parser):
    parser.parse("primus 10\nsecundus 20\nᜈ collectio 『primus secundus』")


def test_sort(parser):
    parser.parse("✎ 金 urbes")


def test_reverse_array(parser):
    parser.parse("✎ ʡ numeri")


def test_delete_element(parser):
    parser.parse("✎ խ numeri 2")


def test_append(parser):
    parser.parse("✎ ⟴ numeri 42")


def test_insert(parser):
    parser.parse("✎ ᙴ numeri 2 99")


def test_assoc(parser):
    parser.parse("✎ ਲ primi secundi")


def test_index(parser):
    parser.parse("✎ 👁 numeri 3")


# --- Регулярные выражения ---

def test_regex_find(parser):
    parser.parse("ɲ exemplum verba")


def test_regex_replace(parser):
    parser.parse("mutata ▧ exemplum novum verba")


# --- Файлы ---

def test_read_file(parser):
    parser.parse("liber ✯ carmen.txt")


def test_read_array(parser):
    parser.parse("versus 𐊚 poema.txt")


def test_read_csv(parser):
    parser.parse("tabula ⠝ cives.csv")


def test_read_xml(parser):
    parser.parse("carmina ཀོ carmen.xml")


def test_write_string(parser):
    parser.parse("𑜸 verba exitus.txt")


def test_write_binary(parser):
    parser.parse("℔ imago image.png")


def test_write_table(parser):
    parser.parse("⠞ tabula exitus.tsv")


def test_write_md(parser):
    parser.parse("ℌ libellus liber.md")


def test_write_xml(parser):
    parser.parse("ᜁ libellus carmen.xml")


# --- Встроенные функции ---

def test_print(parser):
    parser.parse("✎ 5")


def test_help(parser):
    parser.parse("⚜")


def test_help_function(parser):
    parser.parse("⚜ ᛄ")


def test_random(parser):
    parser.parse("urbi ᜅᜒ")


def test_time(parser):
    parser.parse("nunc ῷ")


def test_roman_date(parser):
    parser.parse("✎ ℕ 18 августа")


def test_human_time(parser):
    parser.parse("✎ Ѧ nunc")


# --- Пользовательские функции ---

def test_function_declaration(parser):
    parser.parse("❃ salve nomen\n✎ Привет, ☘ nomen!\n𑚟")


def test_function_return(parser):
    parser.parse("❃ duplica numerus\n𑚟 ᛪ numerus 2")


# --- Комментарии ---

def test_comment(parser):
    parser.parse("❦ Это комментарий\n✎ Привет")


def test_comment_after_code(parser):
    parser.parse("✎ Привет ❦ выводим приветствие")


# --- Сообщение об ошибке ---

def test_error_message(parser):
    parser.parse("☹ Файл не найден")


def test_error_in_condition(parser):
    parser.parse("via ∅\n𐄷 via ∅ ☹ Не указан путь к файлу")


# --- Высокоуровневые функции ---

def test_freq(parser):
    parser.parse("✎ ◈ verba")


def test_tfidf(parser):
    parser.parse("✎ 𐂓 documenta")


def test_ttr(parser):
    parser.parse("✎ į verba")


def test_web_string(parser):
    parser.parse("pagina ⌘ https://example.com")


def test_web_text(parser):
    parser.parse("pagina 枼 https://example.com/article")


def test_web_array(parser):
    parser.parse("situs 𐊙 https://example.com")


def test_web_binary(parser):
    parser.parse("imago 𐃏 https://example.com/image.png")


def test_web_site(parser):
    parser.parse("⚛ https://example.com")


def test_wikipedia(parser):
    parser.parse("pagina ☯ Автандил")


def test_pgn_load(parser):
    parser.parse("partia अ carmen.pgn")


def test_pgn_meta(parser):
    parser.parse("✎ ☪ partia")


def test_pgn_board(parser):
    parser.parse("⅊ partia 10")


def test_ml_train(parser):
    parser.parse("❂ tabula")


def test_ml_target(parser):
    parser.parse("☀ urbs\n❂ tabula")


def test_ml_save(parser):
    parser.parse("ଫ exemplum")


def test_ml_predict(parser):
    parser.parse("ល exemplum")


def test_delta(parser):
    parser.parse("𑜗 corpus")


def test_topic(parser):
    parser.parse("◎ corpus 5")


def test_graph_create(parser):
    parser.parse("graphus ☍ 『Москва Тбилиси』 『Москва Киев』")


def test_graph_rank(parser):
    parser.parse("✎ ⊷ graphus")


def test_graph_cluster(parser):
    parser.parse("✎ ଝ graphus")


# --- Конечные автоматы ---

def test_automaton_declaration(parser):
    code = (
        "initium ☰\n"
        "medium ☱\n"
        "finis ☲\n"
        "▞ initium finis\n"
        "initium a medium\n"
        "medium b finis\n"
        "finis a finis\n"
    )
    parser.parse(code)


def test_automaton_run(parser):
    parser.parse("status ☰ textus")


def test_automaton_with_marks(parser):
    code = (
        "initium ☰\n"
        "nomen ☱\n"
        "finis ☲\n"
        "error ☷\n"
        "▞ initium finis\n"
        "initium < nomen\n"
        "initium > error ☷\n"
        "nomen a nomen ☵\n"
        "nomen > finis ☲\n"
    )
    parser.parse(code)
