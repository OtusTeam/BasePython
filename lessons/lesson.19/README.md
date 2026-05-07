# Шпаргалка: Основы фронтенда

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

## ⚠️ Важные моменты

- Используйте семантические HTML теги для лучшей доступности
- Делайте сайт адаптивным с помощью медиа-запросов
- Всегда проверяйте существование элементов перед их использованием в JS
- Используйте `addEventListener` вместо `onclick` для лучшего контроля
- Минифицируйте CSS и JS для продакшена
- Тестируйте в разных браузерах 


# Шпаргалка: Bootstrap 5

## 📦 Подключение Bootstrap

### CDN подключение:
```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <!-- Контент -->
    
    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

---

## 📱 Grid System - Система сеток

### Контейнеры:
- `.container` - фиксированная ширина
- `.container-fluid` - на всю ширину экрана
- `.container-sm`, `.container-md`, `.container-lg`, `.container-xl` - адаптивные контейнеры

### Сетка (12 колонок):
```html
<div class="container">
    <div class="row">
        <div class="col-12 col-md-6 col-lg-4">Колонка 1</div>
        <div class="col-12 col-md-6 col-lg-4">Колонка 2</div>
        <div class="col-12 col-md-12 col-lg-4">Колонка 3</div>
    </div>
</div>
```

### Размеры экранов:
- `xs` - <576px (по умолчанию)
- `sm` - ≥576px
- `md` - ≥768px  
- `lg` - ≥992px
- `xl` - ≥1200px
- `xxl` - ≥1400px

---

## 🎨 Компоненты

### Кнопки:
```html
<button class="btn btn-primary">Основная</button>
<button class="btn btn-secondary">Вторичная</button>
<button class="btn btn-success">Успех</button>
<button class="btn btn-danger">Опасность</button>
<button class="btn btn-warning">Предупреждение</button>
<button class="btn btn-info">Информация</button>

<!-- Размеры -->
<button class="btn btn-primary btn-lg">Большая</button>
<button class="btn btn-primary btn-sm">Маленькая</button>

<!-- Контурные кнопки -->
<button class="btn btn-outline-primary">Контурная</button>
```

### Карточки:
```html
<div class="card" style="width: 18rem;">
    <img src="image.jpg" class="card-img-top" alt="...">
    <div class="card-body">
        <h5 class="card-title">Заголовок карточки</h5>
        <p class="card-text">Текст карточки...</p>
        <a href="#" class="btn btn-primary">Кнопка</a>
    </div>
</div>
```

### Навигация:
```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
        <a class="navbar-brand" href="#">Логотип</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link active" href="#">Главная</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">О нас</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
```

### Модальные окна:
```html
<!-- Кнопка для открытия модального окна -->
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
    Открыть модальное окно
</button>

<!-- Модальное окно -->
<div class="modal fade" id="exampleModal" tabindex="-1">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Заголовок</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
                Содержимое модального окна
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Закрыть</button>
                <button type="button" class="btn btn-primary">Сохранить</button>
            </div>
        </div>
    </div>
</div>
```

---

## 📝 Формы

### Основные элементы форм:
```html
<form>
    <div class="mb-3">
        <label for="email" class="form-label">Email</label>
        <input type="email" class="form-control" id="email" placeholder="name@example.com">
    </div>
    
    <div class="mb-3">
        <label for="password" class="form-label">Пароль</label>
        <input type="password" class="form-control" id="password">
    </div>
    
    <div class="mb-3">
        <label for="message" class="form-label">Сообщение</label>
        <textarea class="form-control" id="message" rows="3"></textarea>
    </div>
    
    <div class="mb-3 form-check">
        <input type="checkbox" class="form-check-input" id="check">
        <label class="form-check-label" for="check">Согласие на обработку данных</label>
    </div>
    
    <button type="submit" class="btn btn-primary">Отправить</button>
</form>
```

### Валидация форм:
```html
<form class="needs-validation" novalidate>
    <div class="mb-3">
        <input type="text" class="form-control" required>
        <div class="valid-feedback">Выглядит хорошо!</div>
        <div class="invalid-feedback">Пожалуйста, заполните это поле.</div>
    </div>
</form>
```

---

## 🎯 Утилитные классы

### Отступы (margin/padding):
```html
<!-- Margin -->
<div class="m-3">Отступы со всех сторон</div>
<div class="mt-2">Отступ сверху</div>
<div class="mb-4">Отступ снизу</div>
<div class="mx-auto">Центрирование по горизонтали</div>

<!-- Padding -->
<div class="p-3">Внутренние отступы</div>
<div class="pt-2">Внутренний отступ сверху</div>
```

Размеры отступов: `0`, `1`, `2`, `3`, `4`, `5` (0rem, 0.25rem, 0.5rem, 1rem, 1.5rem, 3rem)

### Цвета:
```html
<!-- Цвет текста -->
<p class="text-primary">Основной цвет</p>
<p class="text-success">Зеленый цвет</p>
<p class="text-danger">Красный цвет</p>

<!-- Цвет фона -->
<div class="bg-primary text-white">Синий фон</div>
<div class="bg-warning">Желтый фон</div>
```

### Выравнивание текста:
```html
<p class="text-start">Влево</p>
<p class="text-center">По центру</p>
<p class="text-end">Вправо</p>
```

### Flexbox утилиты:
```html
<div class="d-flex justify-content-center align-items-center">
    <div>Центрированный контент</div>
</div>

<div class="d-flex justify-content-between">
    <div>Слева</div>
    <div>Справа</div>
</div>
```

---

## 📋 Практические примеры

### Карточка товара:
```html
<div class="card h-100">
    <img src="product.jpg" class="card-img-top" alt="Товар">
    <div class="card-body d-flex flex-column">
        <h5 class="card-title">Название товара</h5>
        <p class="card-text flex-grow-1">Описание товара...</p>
        <div class="d-flex justify-content-between align-items-center">
            <span class="h5 mb-0 text-primary">1000 ₽</span>
            <button class="btn btn-outline-primary">Купить</button>
        </div>
    </div>
</div>
```

### Форма обратной связи:
```html
<div class="container mt-5">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <div class="card">
                <div class="card-header">
                    <h4 class="mb-0">Связаться с нами</h4>
                </div>
                <div class="card-body">
                    <form>
                        <div class="mb-3">
                            <input type="text" class="form-control" placeholder="Имя">
                        </div>
                        <div class="mb-3">
                            <input type="email" class="form-control" placeholder="Email">
                        </div>
                        <div class="mb-3">
                            <textarea class="form-control" rows="4" placeholder="Сообщение"></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary w-100">Отправить</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
```

### Галерея изображений:
```html
<div class="row g-3">
    <div class="col-md-4" data-aos="fade-up">
        <div class="card">
            <img src="image1.jpg" class="card-img-top" alt="Фото 1">
        </div>
    </div>
    <div class="col-md-4" data-aos="fade-up" data-aos-delay="100">
        <div class="card">
            <img src="image2.jpg" class="card-img-top" alt="Фото 2">
        </div>
    </div>
    <div class="col-md-4" data-aos="fade-up" data-aos-delay="200">
        <div class="card">
            <img src="image3.jpg" class="card-img-top" alt="Фото 3">
        </div>
    </div>
</div>
```

---

## 🎨 Кастомизация

### Переменные CSS:
```css
:root {
    --bs-primary: #custom-color;
    --bs-font-family-base: 'Custom Font', sans-serif;
}
```

### Собственные стили поверх Bootstrap:
```css
/* Кастомные кнопки */
.btn-custom {
    background-color: #ff6b6b;
    border-color: #ff6b6b;
    color: white;
}

.btn-custom:hover {
    background-color: #ff5252;
    border-color: #ff5252;
}

/* Кастомные карточки */
.card-hover {
    transition: transform 0.3s ease;
}

.card-hover:hover {
    transform: translateY(-5px);
}
```

---

## ⚠️ Важные моменты

- Bootstrap использует mobile-first подход
- Всегда включайте viewport meta тег
- JavaScript компоненты требуют подключения Bootstrap JS
- Используйте утилитные классы для быстрой стилизации
- Проверяйте совместимость с вашим проектом
- Кастомизируйте переменные CSS для уникального дизайна 