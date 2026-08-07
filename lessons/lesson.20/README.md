# Шпаргалка: CSS, Bootstrap 5 и современные CSS-фреймворки

## 🎨 Что такое CSS

**CSS** отвечает за внешний вид HTML-страницы:

* цвета;
* шрифты;
* размеры;
* отступы;
* границы;
* фон;
* расположение элементов;
* состояния при наведении;
* адаптивность.

```text
HTML — структура и содержимое.
CSS — внешний вид.
```

---

# 🔌 Подключение CSS

## Inline-стили

Стиль записывается непосредственно внутри HTML-тега:

```html
<h1 style="color: darkblue; text-align: center;">
    Привет, мир!
</h1>
```

Общий формат:

```text
свойство: значение;
```

Несколько свойств разделяются точкой с запятой:

```html
<p style="font-size: 18px; font-weight: bold;">
    Текст
</p>
```

Используется для быстрых экспериментов и точечных изменений.

---

## Тег `<style>`

Стили записываются внутри `<head>`:

```html
<head>
    <style>
        h1 {
            color: darkblue;
            text-align: center;
        }

        p {
            font-size: 18px;
        }
    </style>
</head>
```

Одно правило применяется сразу ко всем подходящим элементам текущей страницы.

---

## Внешний CSS-файл

Структура проекта:

```text
project/
├── index.html
├── about.html
└── css/
    └── style.css
```

Подключение в `<head>`:

```html
<link rel="stylesheet" href="css/style.css">
```

Файл `css/style.css`:

```css
h1 {
    color: darkblue;
    text-align: center;
}
```

Один CSS-файл можно подключить к нескольким HTML-страницам.

---

# 🏷️ CSS-правило

```css
селектор {
    свойство: значение;
}
```

Пример:

```css
h1 {
    color: darkblue;
    font-size: 42px;
}
```

* `h1` — селектор;
* `color` — свойство;
* `darkblue` — значение.

---

# 🔍 Основные селекторы

## Селектор тега

Выбирает все теги указанного типа:

```css
p {
    color: #333333;
}
```

---

## Селектор класса

В HTML:

```html
<p class="lead-text">
    Важный текст
</p>
```

В CSS:

```css
.lead-text {
    font-size: 18px;
    font-weight: bold;
}
```

Класс начинается с точки:

```css
.lead-text
```

Один класс можно применять к нескольким элементам.

---

## Селектор идентификатора

В HTML:

```html
<article id="travel">
```

В CSS:

```css
#travel {
    border-left: 4px solid darkblue;
}
```

`id` должен быть уникальным на странице.

---

## Вложенные элементы

```css
.main-nav a {
    color: white;
}
```

Выбирает ссылки внутри элемента `.main-nav`.

Более подробный вариант:

```css
.main-nav ul li a {
    font-weight: bold;
}
```

Пробел обозначает вложенность.

---

## Группировка селекторов

```css
.feedback-form input,
.feedback-form textarea {
    border: 1px solid gray;
}
```

Одно правило применяется к нескольким селекторам.

---

# 🖱️ Псевдоклассы

## Наведение

```css
.main-nav a:hover {
    background-color: darkblue;
}
```

`:hover` срабатывает при наведении курсора.

---

## Фокус

```css
input:focus {
    border-color: darkblue;
}
```

`:focus` применяется к активному элементу.

---

## Фокус с клавиатуры

```css
button:focus-visible {
    outline: 3px solid rgba(31, 60, 136, 0.35);
}
```

`:focus-visible` помогает выделять элементы при навигации клавишей `Tab`.

---

# 📚 Каскад и приоритет

Общее правило:

```css
a {
    color: darkblue;
}
```

Более точное правило:

```css
.main-nav a {
    color: white;
}
```

Для ссылок внутри меню сработает более конкретное правило:

```css
.main-nav a
```

При одинаковых селекторах срабатывает правило, записанное ниже:

```css
.text {
    color: green;
}

.text {
    color: red;
}
```

Итоговый цвет — красный.

Inline-стиль имеет более высокий приоритет:

```html
<h1 style="color: red;">Заголовок</h1>
```

---

# ✍️ Текст и шрифты

```css
body {
    font-family: "Roboto", Arial, sans-serif;
    font-size: 16px;
    line-height: 1.6;
}
```

Основные свойства:

```css
font-family: Arial, sans-serif;
font-size: 18px;
font-weight: 700;
font-style: italic;
line-height: 1.6;
text-align: center;
text-decoration: none;
text-transform: uppercase;
letter-spacing: 2px;
```

---

## Подключение внешнего шрифта

В `<head>`:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<link
    href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap"
    rel="stylesheet"
>
```

В CSS:

```css
body {
    font-family: "Roboto", Arial, sans-serif;
}
```

После внешнего шрифта указываются резервные варианты.

---

# 🌈 Цвета

## Название цвета

```css
color: darkblue;
```

## HEX

```css
color: #1f3c88;
```

## RGB

```css
color: rgb(31, 60, 136);
```

## RGBA с прозрачностью

```css
background-color: rgba(31, 60, 136, 0.1);
```

Последнее значение — прозрачность:

```text
0   — полностью прозрачный;
1   — полностью непрозрачный.
```

---

# 🖼️ Фон

## Цвет фона

```css
body {
    background-color: #f4f6f8;
}
```

## Фоновое изображение

```css
.site-header {
    background-image: url("../images/cat.jpg");
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
}
```

Путь считается относительно CSS-файла.

## Изображение с затемнением

```css
.site-header {
    background-image:
        linear-gradient(
            rgba(20, 38, 80, 0.8),
            rgba(20, 38, 80, 0.8)
        ),
        url("../images/cat.jpg");

    background-position: center;
    background-size: cover;
}
```

---

# 📦 Блочная модель

HTML-элемент состоит из:

```text
content → padding → border → margin
```

* `content` — содержимое;
* `padding` — внутренний отступ;
* `border` — граница;
* `margin` — внешний отступ.

Пример:

```css
.article-card {
    max-width: 900px;
    margin: 24px auto;
    padding: 24px;

    background-color: white;
    border: 1px solid #d9e0e8;
    border-radius: 12px;

    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}
```

---

## Размеры

```css
width: 100%;
max-width: 900px;

height: 300px;
min-height: 200px;
```

Для контента обычно удобнее:

```css
width: 100%;
max-width: 900px;
```

Элемент может уменьшаться, но не станет шире заданного значения.

---

## `box-sizing`

```css
* {
    box-sizing: border-box;
}
```

`padding` и `border` включаются в заданную ширину элемента.

---

# 🧱 Блочные и строчные элементы

## Блочный элемент

```css
display: block;
```

* начинается с новой строки;
* занимает доступную ширину.

Примеры:

```html
<div>
<p>
<article>
```

## Строчный элемент

```css
display: inline;
```

* находится внутри строки;
* занимает ширину содержимого.

Примеры:

```html
<a>
<span>
```

## Строчно-блочный элемент

```css
display: inline-block;
```

Остаётся в строке, но может принимать:

* ширину;
* высоту;
* внутренние отступы.

---

# 🖼️ Адаптивные изображения

```css
.article-image {
    display: block;
    width: 100%;
    max-width: 800px;
    height: auto;
    border-radius: 10px;
}
```

Для фиксированной области:

```css
.article-image {
    width: 100%;
    height: 300px;
    object-fit: cover;
}
```

`object-fit: cover` сохраняет пропорции, но может обрезать часть изображения.

---

# 📐 Flexbox для меню

```css
.main-nav ul {
    display: flex;
    flex-wrap: wrap;
    gap: 16px;

    justify-content: center;
    align-items: center;

    list-style: none;
}
```

* `display: flex` — включает Flexbox;
* `gap` — расстояние между элементами;
* `justify-content` — выравнивание по основной оси;
* `align-items` — выравнивание по поперечной оси;
* `flex-wrap` — разрешает перенос элементов.

---

# 🔘 Кнопка на собственном CSS

```css
.submit-button {
    padding: 10px 20px;

    color: white;
    background-color: #1f3c88;

    border: 2px solid #1f3c88;
    border-radius: 8px;

    font: inherit;
    cursor: pointer;

    transition:
        background-color 0.2s ease,
        transform 0.2s ease;
}

.submit-button:hover {
    background-color: #176b55;
    transform: translateY(-2px);
}

.submit-button:focus-visible {
    outline: 3px solid rgba(31, 60, 136, 0.35);
    outline-offset: 3px;
}
```

---

# 🔧 CSS-переменные

Глобальные переменные:

```css
:root {
    --primary-color: #1f3c88;
    --accent-color: #176b55;
    --page-background: #f4f6f8;
    --text-color: #2d3748;

    --base-radius: 12px;
    --base-spacing: 24px;
    --content-width: 900px;
}
```

Использование:

```css
body {
    color: var(--text-color);
    background-color: var(--page-background);
}

.article-card {
    max-width: var(--content-width);
    padding: var(--base-spacing);
    border-radius: var(--base-radius);
}
```

Резервное значение:

```css
color: var(--primary-color, darkblue);
```

Локальное переопределение:

```css
#nature {
    --primary-color: #b45309;
}
```

---

# 📏 Гибкий размер через `clamp()`

```css
.page-title {
    font-size: clamp(28px, 5vw, 42px);
}
```

* `28px` — минимальный размер;
* `5vw` — гибкий размер;
* `42px` — максимальный размер.

---

# 🅱️ Bootstrap 5

Bootstrap предоставляет:

* адаптивную сетку;
* готовые компоненты;
* кнопки;
* формы;
* карточки;
* таблицы;
* Navbar;
* утилитные классы.

---

# 🔌 Подключение Bootstrap через CDN

В `<head>`:

```html
<meta
    name="viewport"
    content="width=device-width, initial-scale=1"
>

<link
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css"
    rel="stylesheet"
>
```

Перед `</body>`:

```html
<script
    src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"
></script>
```

* CSS отвечает за оформление;
* JavaScript Bundle нужен интерактивным компонентам.

---

# 📁 Локальное подключение Bootstrap

Структура:

```text
project/
├── bootstrap/
│   ├── css/
│   │   └── bootstrap.min.css
│   └── js/
│       └── bootstrap.bundle.min.js
└── index.html
```

В `<head>`:

```html
<link
    rel="stylesheet"
    href="bootstrap/css/bootstrap.min.css"
>
```

Перед `</body>`:

```html
<script src="bootstrap/js/bootstrap.bundle.min.js"></script>
```

Собственный CSS подключается после Bootstrap:

```html
<link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
<link rel="stylesheet" href="css/style.css">
```

---

# 📦 Контейнеры Bootstrap

Ограниченный контейнер:

```html
<main class="container">
```

Контейнер на всю ширину:

```html
<main class="container-fluid">
```

---

# 📐 Утилиты Bootstrap

## Отступы

```text
m → margin
p → padding
```

Стороны:

```text
t → top
b → bottom
s → start
e → end
x → слева и справа
y → сверху и снизу
```

Примеры:

```html
<div class="p-4">Внутренний отступ</div>
<div class="mb-3">Отступ снизу</div>
<div class="mx-auto">Центрирование</div>
<div class="py-5">Отступ сверху и снизу</div>
```

---

## Текст

```html
<h1 class="text-center fw-bold text-uppercase">
    Заголовок
</h1>
```

Полезные классы:

```text
text-center
text-primary
text-white
text-body-secondary
fw-bold
fs-5
text-uppercase
text-decoration-none
```

---

## Фон, границы и тени

```html
<article
    class="
        bg-white
        border
        border-primary-subtle
        rounded-3
        shadow
        p-4
    "
>
```

---

## Размеры и отображение

```html
<div class="w-100">Ширина 100%</div>
<div class="d-block">Блочный элемент</div>
<div class="d-flex gap-3">Flexbox</div>
```

---

## Адаптивное изображение

```html
<img
    class="img-fluid rounded-3 shadow-sm"
    src="images/cat.jpg"
    alt="Кот"
>
```

`img-fluid` примерно соответствует:

```css
max-width: 100%;
height: auto;
```

---

# 🧩 Сетка Bootstrap

Основная структура:

```html
<div class="container">
    <div class="row">
        <div class="col">
            Колонка
        </div>
    </div>
</div>
```

Bootstrap делит строку на 12 частей:

```html
<div class="col-12">100%</div>
<div class="col-6">50%</div>
<div class="col-4">33%</div>
<div class="col-3">25%</div>
```

---

## Адаптивные колонки

```html
<div class="col-12 col-md-6 col-lg-4">
    Статья
</div>
```

* маленький экран — одна колонка;
* от `md` — две колонки;
* от `lg` — три колонки.

Контрольные точки:

| Префикс      | Минимальная ширина |
| ------------ | -----------------: |
| без префикса |              `0px` |
| `sm`         |            `576px` |
| `md`         |            `768px` |
| `lg`         |            `992px` |
| `xl`         |           `1200px` |
| `xxl`        |           `1400px` |

---

## Расстояние между колонками

```html
<div class="row g-4">
```

* `g-*` — все промежутки;
* `gx-*` — горизонтальные;
* `gy-*` — вертикальные.

---

# 🧭 Bootstrap Navbar

```html
<nav
    class="navbar navbar-expand-lg bg-dark"
    data-bs-theme="dark"
>
    <div class="container">
        <a class="navbar-brand" href="#">
            Travel Blog
        </a>

        <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#mainNavbar"
        >
            <span class="navbar-toggler-icon"></span>
        </button>

        <div
            class="collapse navbar-collapse"
            id="mainNavbar"
        >
            <ul class="navbar-nav ms-auto">
                <li class="nav-item">
                    <a class="nav-link active" href="#">
                        Главная
                    </a>
                </li>

                <li class="nav-item">
                    <a class="nav-link" href="#travel">
                        Путешествия
                    </a>
                </li>
            </ul>
        </div>
    </div>
</nav>
```

Значения должны совпадать:

```html
data-bs-target="#mainNavbar"
id="mainNavbar"
```

Для раскрытия меню нужен:

```html
bootstrap.bundle.min.js
```

---

# 🔘 Bootstrap-кнопки

```html
<button class="btn btn-primary">
    Основная
</button>

<button class="btn btn-outline-primary">
    Контурная
</button>

<button class="btn btn-success btn-sm">
    Маленькая
</button>

<button class="btn btn-danger btn-lg">
    Большая
</button>
```

Ссылка в виде кнопки:

```html
<a class="btn btn-warning" href="about.html">
    Подробнее
</a>
```

`<a>` используется для перехода, `<button>` — для действия.

---

# 🃏 Bootstrap Card

```html
<article class="card h-100 shadow-sm">
    <img
        class="card-img-top"
        src="images/cat.jpg"
        alt="Кот"
    >

    <div class="card-body d-flex flex-column">
        <h2 class="card-title h4">
            Путешествие на Байкал
        </h2>

        <p class="card-text">
            Описание путешествия.
        </p>

        <a
            class="btn btn-primary mt-auto"
            href="#"
        >
            Подробнее
        </a>
    </div>
</article>
```

Основные классы:

```text
card
card-img-top
card-body
card-title
card-text
```

---

# 📝 Bootstrap-форма

```html
<form class="bg-white rounded-3 shadow p-4">
    <div class="mb-3">
        <label class="form-label" for="name">
            Имя
        </label>

        <input
            class="form-control"
            type="text"
            id="name"
            name="user_name"
        >
    </div>

    <div class="mb-3">
        <label class="form-label" for="message">
            Сообщение
        </label>

        <textarea
            class="form-control"
            id="message"
            rows="5"
        ></textarea>
    </div>

    <button class="btn btn-primary w-100">
        Отправить
    </button>
</form>
```

Основные классы:

```text
form-label
form-control
```

---

# 📊 Bootstrap-таблица

```html
<div class="table-responsive">
    <table
        class="
            table
            table-striped
            table-hover
            table-bordered
            align-middle
        "
    >
        <thead class="table-primary">
            <tr>
                <th scope="col">Место</th>
                <th scope="col">Город</th>
            </tr>
        </thead>

        <tbody>
            <tr>
                <th scope="row">1</th>
                <td>Москва</td>
            </tr>
        </tbody>
    </table>
</div>
```

* `table` — базовое оформление;
* `table-striped` — чередование строк;
* `table-hover` — подсветка;
* `table-bordered` — границы;
* `table-responsive` — горизонтальная прокрутка.

---

# 🧱 Готовые блоки Bootstrap

Официальные примеры содержат:

* Headers;
* Heroes;
* Pricing;
* Album;
* Sign-in;
* Dashboard.

Правильный порядок работы:

```text
открыть пример
→ изучить структуру
→ выбрать нужный блок
→ скопировать только его
→ проверить CSS и JavaScript
→ изменить тексты, ссылки и изображения
```

Нельзя вставлять один полный HTML-документ внутрь другого:

```html
<!DOCTYPE html>
<html>
<head>
<body>
```

Переносится только нужный блок из `<body>`.

---

# 🌬️ Tailwind CSS

Tailwind использует utility-first-подход.

Bootstrap:

```html
<button class="btn btn-primary">
    Кнопка
</button>
```

Tailwind:

```html
<button
    class="
        rounded-lg
        bg-blue-600
        px-5
        py-3
        font-semibold
        text-white
    "
>
    Кнопка
</button>
```

---

# 🔌 Подключение Tailwind через Play CDN

В `<head>`:

```html
<script
    src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"
></script>
```

Play CDN используется для обучения и экспериментов, но не для production.

---

# 🎨 Основные классы Tailwind

## Фон и текст

```html
<body class="bg-slate-100 text-slate-800">
```

## Контейнер

```html
<main class="mx-auto max-w-5xl px-4 py-10">
```

## Карточка

```html
<article
    class="
        overflow-hidden
        rounded-2xl
        bg-white
        shadow-xl
        md:flex
    "
>
```

## Изображение

```html
<img
    class="
        h-64
        w-full
        object-cover
        md:h-auto
        md:w-1/2
    "
    src="images/cat.jpg"
    alt="Кот"
>
```

## Кнопка

```html
<a
    class="
        rounded-lg
        bg-blue-600
        px-5
        py-3
        font-semibold
        text-white
        transition
        hover:bg-blue-700
        focus:ring-4
        focus:ring-blue-300
    "
    href="#"
>
    Подробнее
</a>
```

---

# 📱 Адаптивность Tailwind

```html
<h1 class="text-3xl md:text-5xl">
    Заголовок
</h1>
```

* `text-3xl` — базовый размер;
* `md:text-5xl` — размер от контрольной точки `md`.

Состояния:

```text
hover:bg-blue-700
focus:ring-4
```

---

# 🏗️ Tailwind для production

Установка CLI:

```bash
npm install tailwindcss @tailwindcss/cli
```

Входной CSS:

```css
@import "tailwindcss";
```

Запуск сборки:

```bash
npx @tailwindcss/cli \
    -i ./src/input.css \
    -o ./src/output.css \
    --watch
```

* `-i` — входной файл;
* `-o` — итоговый файл;
* `--watch` — автоматическая пересборка.

---

# 🔄 Сравнение подходов

| Подход          | Основная идея                 | Пример                   |
| --------------- | ----------------------------- | ------------------------ |
| Собственный CSS | Пишем свои правила            | `.article-card`          |
| Bootstrap       | Используем готовые компоненты | `.card`, `.btn`          |
| Tailwind CSS    | Собираем дизайн из утилит     | `p-6 bg-white shadow-xl` |

---

# ⚠️ Важные моменты

* CSS отвечает за внешний вид HTML.
* Для основного проекта лучше использовать внешний CSS-файл.
* Классы можно применять к нескольким элементам.
* `id` должен быть уникальным.
* `padding` — внутренний отступ.
* `margin` — внешний отступ.
* `box-sizing: border-box` упрощает расчёт размеров.
* Не удаляйте стили фокуса без замены.
* Собственный CSS подключается после Bootstrap.
* Не подключайте Bootstrap через CDN и локально одновременно.
* CSS и JavaScript Bootstrap должны быть одной версии.
* Bootstrap JavaScript нужен интерактивным компонентам.
* Готовые блоки нужно адаптировать под проект.
* Tailwind Play CDN не используется в production.
* Bootstrap и Tailwind не заменяют знание HTML и CSS.

