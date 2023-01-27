# Примеры кода

## Переменные и присваивание

* Переменные называются одной 10 000 наиболее частотных словоформ латинского языка в нижнем регистре.
* Присваивание осуществляется в случае, если в одной строке находится имя переменной, которой присваивается значение, и разделенные с ним пробелами:
	1. значение
	2. имя другой переменной, из которой заимствуется значение, включая рабочую переменную `𐃰`;
	3. операция;
	4. встроенная функция;
	5. пользовательская функция.
* В рабочей переменной хранится результат последней операции, если для результата операции не была эксплицитно объявлена переменная.

### Примеры имен переменных

* odio
* orationem
* praesens
* urbi
* habitus
* istum
* metum
* fines
* istam
* poterant

### Присваивание

`praesens 5`

Переменной `praesens` присваивается значение `5`.

`orationem fines`

Переменной `orationem` присваивается значение переменной `fines`.

`urbi ᜅᜒ`

Переменной `urbi` присваивается результат, который возвращает встроенная функция `ᜅᜒ`.

```
ᜅᜒ
fines 𐃰
```

Переменной `fines` присваивается значение рабочей переменной `𐃰`, в которой хранится значение, возвращенное функцией `ᜅᜒ`.

## Печать в стандартный вывод

* Печать осуществляется с помощью встроенной функции `✎`.
* Печатаемое значение располагается справа от имени функции.
* Печатаемое значение помещается в рабочую переменную.

`✎ 5`

Выведет `5`.

```
poterant 7
✎ poterant
```

Выведет `7`

```
istam 7
✎ istam
✎ 𐃰
```

Выведет:

```
7
7
```

## Арифметика

* Оператор ставится перед числовыми значениями.
* Числовые значения разделяются пробелом.
* Операции производятся последовательно слева направо до конца строки.
* Если перед оператором объявлена переменная, результаты вычислений помещаются в нее.
* Если переменная не объявлена, результаты вычислений помещаются в рабочую переменную `𐃰`.
* Вызов рабочей переменной может быть неявным.

### Сложение
```
ᛝ 2 3
✎ 
```

`⋗ 5`

Неявный вызов рабочей переменной.

```
bonus ᛝ 2 3 12
✎ bonus
```

`⋗ 17`

Результат вычислений помещен в переменную `bonus`.

### Вычитание

```
ᚸ 21 7
minus 𐃰
✎ minus
```

`⋗ 14`

Результат вычислений помещен в рабочую переменную. Затем она явно вызвана и 

```
ᚸ 100 20 40
✎
```

`⋗ 40`

### Умножение

```
plurimum 10
ᛪ plurimum 20
✎ 
```

Выведет:

`200`

### Деление

Деление осуществляется слева направо. Если числовых значений в строке несколько, то каждое следующее деление производится с результатом предыдущего.

Деление на ноль дает `∅`. Любые арифметические операции с `∅` дают `∅`.

`✎ ᛄ 100 2`

Выведет `50`

`✎ ᛄ 100 10 2`

Выведет `5`

```
postremo ᛄ 10 0
✎ postremo 
✎ ᛝ postremo 2
```

Выведет:

```
∅
∅
```

### χ-квадрат

Вычисление критерия χ-квадрат производится для массива из 4 числовых значений, первые два из которых считаются верхней, а вторые два — нижней стороной квадрата. Операция возвращает значение p-value.

```
Ⰺ 113 144 125 129
✎ 𐃰
```

Выведет: `0,2716`

χ-квадрат вычисляется для массива:

```
datur『151 125 164 171』
sociis Ⰺ datur
✎ sociis
```

Выведет: `0,1818`

### Корреляция

Коэффициент корреляции Спирмена вычисляется для двух массивов чисел одинаковой длины.

```
maiores 『10 15 10 13 10 21』
singulorum 『14 18 10 18 6 19』
✎ ᬈ maiores singulorum
```

Выведет: `0,7359364`

Код аналогичен следующему:

```
✎ ᬈ 『10 15 10 13 10 21』『14 18 10 18 6 19』
```

### Вычисление процента

Процент вычисляется для двух числовых значений. Первое берется как целое, второе как доля.

`✎ ѯ 100 13`

Выведет: `13 ℅`

```
copias ѯ 1315 26
✎ copias
```

Выведет: `1,977186312`

## Условия

Синтаксис условия предполагает следующий порядок разделенных пробелами токенов:
1. оператор
2. первое сравниваемое значение
3. второе сравниваемое значение
4. код, который требуется выполнить, если условие соблюдено

Если условие не соблюдается, то код, который требуется выполнить, размещается на следующей строке после парного оператора. Пары операторов:
* `𐄷 𑚐`
* `≈ ≉`
* `᭕ ゅ`

Если сравниваемые значения представлены числами, то они могут быть представлены в условной конструкции as is. Если сравниваются строки, то они должны предварительно быть помещены в переменные.


### Равенство

```
metum 5
𐄷 metum 3 ✎ Значения равны 
```

В первой строке переменной `metum` присваивается значение `5`, во второй строке значение переменной `metum` сравнивается с числом `3`. Если значения равны, в стандартный вывод печатается: `Значения равны`. В данном случае программа ничего не выведет.

```
dominum 5
𑚐 dominum 3 ✎ Значения не равны 
✎ 𐃰
```

В первой строке переменной `dominum` присваивается значение `5`, во второй строке значение переменной `dominum` проверяется на неравенство с числом `3`. Программа выведет `Значения не равны`, эта строка будет помещена в рабочую переменную, которая распечатается в следующей строке. Таким образом, строка `Значения не равны` будет распечатана два раза.

```
certamen 5
𐄷 certamen 3 ✎ Значения равны 
𑚐 ✎ Значения не равны 
```

В первой строке переменной `certamen` присваивается значение `5`, во второй строке значение переменной `certamen` сравнивается с числом `3`. Если значения равны, в стандартный вывод печатается: `Значения равны`. Если значения не равны, будет выполнен код после оператора `𑚐` (его функциональность в данном случае аналогична оператору `else` в распространенных языках), то есть будет распечатана строка `Значения не равны`.

### Вложенные условия

```
dicendi 5
𐄷 dicendi 3 ✎ Значение переменной равно 3
𑚐 𐄷 dicendi 7 ✎ Значение переменной равно 7
𑚐 ✎ Значение переменной не равно ни одному из известных значений
```

В первой строке переменной `dicendi` присваивается значение `5`, во второй строке значение переменной `dicendi` сравнивается с числом `3`. Если значения не равны, то значение переменной `dicendi` сравнивается с числом `7`. Если повторное сравнение дает `False`, в стандартный вывод печатается строка `Значение переменной не равно ни одному из известных значений`.

### Приблизительное равенство

Этот вид условия проверяет равенство чисел в окне 1 целого числа слева и справа в натуральном ряду и равенство строк с учетом расстояния Левенштейна.

#### Приблизительное равенство чисел

`≈ 5 6 ✎ Числа приблизительно равны`

Выведет строку `Числа приблизительно равны`.

`≈ 5 10 ✎ Числа приблизительно равны`

Программа ничего не выведет.

```
scriptum 10
≈ scriptum 11
✎ Числа приблизительно равны
≉ ✎ Числа не равны даже приблизительно
```

Выведет строку `Числа не равны даже приблизительно`.

```
subito 10
≉ subito 11
✎ Числа не равны даже приблизительно
≈ ✎ Числа приблизительно равны
```

Выведет строку `Числа приблизительно равны`.

#### Приблизительное равенство строк

```
solet марка
gratiam маска
≈ solet gratiam ✎ Строки приблизительно равны
```

Выведет строку `Строки приблизительно равны`. Расстояние Левенштейна между строками равно 1.

```
naturae Пушкин
regis Пушкинский
≈ naturae regis ✎ Строки приблизительно равны
≉ ✎ Строки далеки друг от друга
```

Выведет строку `Строки далеки друг от друга`. Расстояние Левенштейна между строками больше 1.

### Больше

Условие выполняется, если первое значение больше, чем второе.

```
priusquam 5
faciunt 3
អ priusquam faciunt ✎ Число ☘ priusquam больше, чем ☘ faciunt
```

Выведет строку `Число 5 больше, чем 3`.

### Четность

Этот вид условия проверяет число на четность. Со строкой эта операция невозможна.

`᭕ 14 ✎ Число четное`

Выведет строку `Число четное`.

```
longius 5
ゅ longius ✎ Число ☘ longius нечетное
```

Выведет строку `Число 5 нечетное`.

## Циклы

### Заданное число итераций

Цикл можно задать, указав нужное число итераций. Тело цикла располагается на той же строке.

`⊹ 4 ✎ итерация`

Выведет:

```
итерация
итерация
итерация
итерация
```

Номер итерации хранится в переменной `𐂅`

`⊹ 3 ✎ 𐂅`

Выведет:

```
1
2
3
```

Если тело не умещается в одной строке, телом цикла считается код до инструкции, прерывающей исполнение.

```
⊹ 10 ✎ 𐂅
𐄷 𐂅 3 𑜐 
✎ Цикл завершен
```

Выведет:

```
1
2
3
Цикл завершен
```

### Цикл по массиву

С помощью цикла можно обходить массив. В переменной `♖` хранится содеримое элемента на текущей итерации.

```
⊹ 『20 13 21 42』 ✎ ♖
```

Выведет:

```
20
13
21
42
```

Чтобы вывести одновременно номер итерации и содержимое элемента, нужно конкатенировать строки:

```
⊹ 『20 13 21 42』 ✎ 𐎺 𐂅. ♖
```

Выведет:

```
1. 20
2. 13
3. 21
4. 42
```

### Бесконечный цикл

У бесконечного цикла нет переменной, хранящей число итераций.

Бесконечный цикл будет исполнен только в случае, если предусмотрено условие его прерывания. В противном случае интерпретатор сообщит об ошибке. 

```
provinciam ῷ
ਊ
aliquanto ῷ
invidia ᚸ aliquanto provinciam
អ invidia 1000 𑜐
```

Цикл будет выполнятся не больше 1000 секунд. 

### Цикл по словам в строке

При выполнении этого вида цикла строка автоматически разбивается по пробелам и на каждой итерации цикла в переменной `♖` хранится одно слово.

```
fratres Мама мыла раму
ສ fratres ✎ ♖
```

Выведет:

```
Мама
мыла
раму
```

Условие внутри цикла:

```
fratres Мама мыла раму
tenuit мыло
ສ fratres
≈ ♖ tenuit ✎ Слово похоже на "☘ tenuit"
𑜐
```

Выведет:

```
Мама
Слово похоже на "мыло"
раму
```

### Цикл по символам в строке

В этом цикле на каждой итерации в переменной `♖` хранится один символ.

```
possis Вавилон
𑚉 possis ✎ ♖
```

Выведет:

```
В
а
в
и
л
о
н
```

## Работа со строками

### Особенности присваивания

Задание пустой строки: `⚘ officium`

В случае со строками присваивание осуществляется таким образом, что первое слово в строке считается именем переменной, а вся остальная строка после пробела — значением. Окончанием присваиваемых данных считается зарезервированный языком токен, начинающий новую строку, или переменная, начинающая строку, содержащую зарезервированные языком токены.

Так, в коде 

```
certum et leni coepit pandere vela Noto.
Ast ubi paulatim praeceps audacia crevit
cordaque languentem dedidicere metum,
iam vagus irrumpit pelagus caelumque secutus
Aegaeas hiemes Ioniumque domat.
⚘
```

Слово `certum` считается именем переменной, а весь остальной текст после пробела до символа `⚘` — присвоенной переменной `certum` строкой.

```
ສ certum
𐄷 𐂅 3 ✎ ♖
អ 𐂅 23 ✎ ♖
𑜐
```

Выведет:

```
coepit
hiemes
Ioniumque
domat
```

```
oculis Naso Tomitanae iam non nouus incola terrae
hoc tibi de Getico litore mittit opus.
Si uacat, hospitio peregrinos, Brute, libellos
excipe dumque aliquo, quolibet abde modo.
lege ᕘ oculis
```

Слово `oculis` считается именем переменной, а весь остальной текст после пробела до слова `lege` — присвоенной переменной `oculis` строкой.

### Разбиение строки

Разбить строку на элементы массива по шаблону можно так: 

```
honores Бобэоби пелись губы
沙 б honores
⊹ 𐃰 ✎ 𐎺 𐂅. ♖
```

Выведет:

```
1. Бо
2. эо
3. и пелись гу
4. ы
```

Разбить строку на слова:

```
voluit Сторож курил и спокойно глядел дальше – в бога он от частых богослужений не верил
𑜱 voluit
⊹ 𐃰 𐄷 𐂅 4 ✎ ♖
```

Выведет: `спокойно`

Разбить строку на предложения:

```
auxilium «Не шутите с терминологией, Антон! Терминологическая путаница влечет за собой опасные последствия». Он никак не может понять, что нормальный уровень средневекового зверства это счастливый вчерашний день Арканара.
consulis ま auxilium
⊹ consulis ✎ 𐂅
```

Выведет:

```
1
2
3
```

Разбить строку в произвольном месте (по позиции символа):

```
placet Средневековое целое — это органическая нерасторжимость производства идей и производства вещей.
romanorum repente ✂ 55 placet
✎ romanorum
✎ repente
```

Выведет:

```
Средневековое целое — это органическая нерасторжимость 
производства идей и производства вещей.
```

### Конкатенация

Разделитель указывается после названия функции до данных. Если разделителем должен быть пробел, то он указывается как `▣`. Если не указать разделитель, то им будет пустая строка.

#### Конкатенация массивов

`✎ 𐎺 ▣ 『20 13 21 42』`

Выведет: `20 13 21 42`

`✎ 𐎺 - 『Диковины среднего возраста』`

Выведет: `Диковины-среднего-возраста`

#### Конкатенация строк

```
singulis Железно
quarum дорожный
✎ 𐎺 singulis quarum
```

Выведет: `Железнодорожный`

### Вычисление длины строки

```
deorum Предлог – самая частотная служебная часть речи
✎ ᕘ deorum
```

Выведет: `46`

```
deorum Политическая деятельность всецело располагается за рамками этики, цель всякой политики – захват и удержание власти
romanus ᕘ deorum
✎ romanus
```

Выведет: `114`

### Поиск и замена подстроки

Функция возвращает начальную и конечную позицию символов, соответствующих первой найденной подстроке. Если подстрока не найдена, возвращается `∅`.

```
verum Микросоциологи не верят в существование общества
arma вован
rerum quae 🔍︎ arma verum
✎ rerum
✎ quae
```

Выведет:

```
32
37
```

Если переменные не заданы, позиции символов помещаются в массив:

```
quibus Микросоциологи не верят в существование общества
simul вован
🔍︎ simul quibus
⊹ 𐃰 ✎ ♖
```

Выведет:

```
32
37
```

Функция `ဠ` позволяет заменить все вхождения подстрок в строке.

```
animi Вместо Бога — милиционера бояться!
iussi о
montibus V
accessit ဠ iussi montibus animi
✎ accessit
```

Выведет: `ВместV БVга — милициVнера бVяться!`

### Работа со знаками препинания

Набор знаков препинания хранится в специальной переменной `𐃨`

Его можно распечатать: `✎ 𐃨`

Функция `𑜹` позволяет удалить все знаки препинания, находящиеся между словами.

```
senatus Она вошла и говорит: "Что за табак... О, как он воняет!.." А потом упала. И больше не шевелится!
✎ 𑜹 senatus
```

Выведет: `Она вошла и говорит Что за табак О как он воняет А потом упала И больше не шевелится`

### Регистр символов

Понизить регистр символов позволяет функция `平`. Допускается одновременное его использование вместе с функцией `𑜹`:

```
locum Она вошла и говорит: "Что за табак... О, как он воняет!.." А потом упала. И больше не шевелится!
✎ 𑜹 平 locum
```

Выведет: `она вошла и говорит что за табак о как он воняет а потом упала и больше не шевелится`

### Кириллица

Функция `Җ` позволяет возвращать кириллические символы строки, а также дефисы внутри слов и пробелы.

```
ager По-немецки такие стихи для запоминания называются "ослиными мостиками" Eselsbrücken
✎ Җ ager
```

Выведет: `По-немецки такие стихи для запоминания называются ослиными мостиками`










