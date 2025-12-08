# Шпаргалка: Основы фронтенда

## 📝 HTML - Структура веб-страницы

### Основные теги:
```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Заголовок страницы</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <!-- Содержимое страницы -->
</body>
</html>
```

### Структурные теги:
- `<header>` - шапка сайта
- `<nav>` - навигация/меню
- `<main>` - основной контент
- `<article>` - статья/пост
- `<section>` - секция контента
- `<aside>` - боковая панель
- `<footer>` - подвал сайта

### Контентные теги:
```html
<h1>Главный заголовок</h1>
<h2>Подзаголовок</h2>
<p>Параграф текста</p>
<a href="https://example.com">Ссылка</a>
<img src="image.jpg" alt="Описание">
<ul>
    <li>Элемент списка</li>
</ul>
```

### Формы:
```html
<form action="/submit" method="post">
    <input type="text" name="name" placeholder="Имя">
    <input type="email" name="email" placeholder="Email">
    <textarea name="message" placeholder="Сообщение"></textarea>
    <button type="submit">Отправить</button>
</form>
```

---

## 🎨 CSS - Стилизация

### Подключение CSS:
```html
<!-- Внешний файл -->
<link rel="stylesheet" href="styles.css">

<!-- Внутренние стили -->
<style>
    body { font-family: Arial, sans-serif; }
</style>

<!-- Инлайн стили -->
<p style="color: red;">Красный текст</p>
```

### Основные свойства:
```css
/* Цвета и фон */
color: #333;
background-color: #f0f0f0;
background-image: url('bg.jpg');

/* Текст */
font-family: Arial, sans-serif;
font-size: 16px;
font-weight: bold;
text-align: center;
line-height: 1.5;

/* Размеры и отступы */
width: 300px;
height: 200px;
margin: 10px;           /* Внешние отступы */
padding: 20px;          /* Внутренние отступы */
border: 1px solid #ccc; /* Граница */
```

### Flexbox - современная раскладка:
```css
.container {
    display: flex;
    justify-content: center;    /* Горизонтальное выравнивание */
    align-items: center;        /* Вертикальное выравнивание */
    gap: 20px;                  /* Расстояние между элементами */
}

.item {
    flex: 1;                    /* Растянуть на всю ширину */
}
```

### Адаптивность:
```css
/* Медиа-запросы для адаптивности */
@media (max-width: 768px) {
    .container {
        flex-direction: column;
    }
}
```

### Псевдоклассы и эффекты:
```css
a:hover {
    color: blue;
    text-decoration: underline;
}

button:active {
    transform: scale(0.95);
}

.card {
    transition: transform 0.3s ease;
}

.card:hover {
    transform: translateY(-5px);
}
```

---

## ⚡ JavaScript - Интерактивность

### Подключение JS:
```html
<!-- Внешний файл -->
<script src="script.js"></script>

<!-- Внутренний скрипт -->
<script>
    console.log('Hello, World!');
</script>
```

### Работа с DOM:
```javascript
// Получение элементов
const element = document.getElementById('myId');
const elements = document.querySelectorAll('.myClass');
const button = document.querySelector('button');

// Изменение содержимого
element.textContent = 'Новый текст';
element.innerHTML = '<strong>HTML контент</strong>';

// Изменение стилей
element.style.color = 'red';
element.style.display = 'none';

// Добавление/удаление классов
element.classList.add('active');
element.classList.remove('hidden');
element.classList.toggle('visible');
```

### События:
```javascript
// Обработчик события
button.addEventListener('click', function() {
    alert('Кнопка нажата!');
});

// Сокращенная запись
button.onclick = () => {
    console.log('Клик по кнопке');
};

// Обработка формы
form.addEventListener('submit', function(e) {
    e.preventDefault(); // Предотвратить отправку
    const formData = new FormData(form);
    console.log(formData.get('name'));
});
```

### Практические примеры:
```javascript
// Показать/скрыть элемент
function toggleElement(id) {
    const element = document.getElementById(id);
    element.style.display = element.style.display === 'none' ? 'block' : 'none';
}

// Изменение темы
function toggleTheme() {
    document.body.classList.toggle('dark-theme');
}

// Валидация формы
function validateForm() {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    
    if (!name) {
        alert('Введите имя!');
        return false;
    }
    
    if (!email.includes('@')) {
        alert('Введите корректный email!');
        return false;
    }
    
    return true;
}
```

---

## 🎯 Готовые компоненты и паттерны

### Кнопка "Показать больше":
```html
<div id="content">
    <p>Видимый текст</p>
    <div id="hidden-content" style="display: none;">
        <p>Скрытый текст</p>
    </div>
    <button onclick="toggleContent()">Показать больше</button>
</div>
```

```javascript
function toggleContent() {
    const hidden = document.getElementById('hidden-content');
    const button = document.querySelector('button');
    
    if (hidden.style.display === 'none') {
        hidden.style.display = 'block';
        button.textContent = 'Показать меньше';
    } else {
        hidden.style.display = 'none';
        button.textContent = 'Показать больше';
    }
}
```

### Модальное окно:
```css
.modal {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0,0,0,0.5);
}

.modal-content {
    background-color: white;
    margin: 15% auto;
    padding: 20px;
    width: 80%;
    max-width: 500px;
}
```

```javascript
function openModal() {
    document.getElementById('modal').style.display = 'block';
}

function closeModal() {
    document.getElementById('modal').style.display = 'none';
}
```

### Слайдер изображений:
```javascript
let currentSlide = 0;
const slides = document.querySelectorAll('.slide');

function showSlide(n) {
    slides.forEach(slide => slide.style.display = 'none');
    currentSlide = (n + slides.length) % slides.length;
    slides[currentSlide].style.display = 'block';
}

function nextSlide() {
    showSlide(currentSlide + 1);
}

function prevSlide() {
    showSlide(currentSlide - 1);
}
```

---

## ⚠️ Важные моменты

- Используйте семантические HTML теги для лучшей доступности
- Делайте сайт адаптивным с помощью медиа-запросов
- Всегда проверяйте существование элементов перед их использованием в JS
- Используйте `addEventListener` вместо `onclick` для лучшего контроля
- Минифицируйте CSS и JS для продакшена
- Тестируйте в разных браузерах 