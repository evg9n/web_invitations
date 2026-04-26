# Веб-приглашения

Веб-приложение для рассылки персональных свадебных приглашений. Каждый гость получает уникальную ссылку, по которой подтверждает присутствие, выбирает трансфер и напитки. Результаты экспортируются в Excel.

## Стек

- **Backend:** Django 5, Django REST Framework, PostgreSQL
- **Frontend:** Django Templates, Tailwind CSS, vanilla JS
- **Инфраструктура:** Docker Compose, Gunicorn, Nginx

## Быстрый старт

### 1. Настройка окружения

Перейдите в директорию `env/` — там находятся два шаблона:

```bash
cp env/.env.template .env
cp env/docker.env.template docker.env
```

Заполните `.env`: секретный ключ Django, данные БД, и детали события (имена, дата, место, координаты карты).

### 2. Запуск через Docker

```bash
docker-compose up
```

Поднимается три сервиса: PostgreSQL, Django (Gunicorn), Nginx.

### 3. Применить миграции и создать администратора

```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

### 4. Сборка CSS (для разработки)

```bash
npm install
npm run build:css
```

## Переменные окружения

| Переменная | Описание |
|---|---|
| `SECRET_KEY_DJANGO` | Секретный ключ Django |
| `DEBUG_DJANGO` | Режим отладки (True/False) |
| `ALLOWED_HOSTS` | Разрешённые хосты |
| `NAME_GROOM`, `NAME_BRIDE` | Имена жениха и невесты |
| `DAY`, `MONTH`, `YEAR`, `HOUR`, `MINUTES` | Дата и время события |
| `PLACE` | Место проведения |
| `WIDTH`, `LONGITUDE`, `NAME_LABEL` | Координаты и подпись на карте |
| `USERNAME_DB`, `PASSWORD_DB`, `NAME_DB`, `HOST_DB`, `PORT_DB` | Подключение к PostgreSQL |

## Администрирование

Панель администратора: `/my-admin/here-adminka/`

Управление гостями, событиями, городами трансфера и напитками.

## Экспорт результатов

`GET /api/v1/get-result` — возвращает Excel-файл с ответами гостей. Требует Token-аутентификацию.
