# Flask - Практические занятия

## Flask Блог

Простой блог на Flask с возможностью создания, редактирования и удаления постов, а также добавления комментариев.

### Функционал

- 📝 Главная страница со списком всех постов
- 📄 Страница просмотра полного текста статьи
- 💬 Отображение полного списка комментариев к статье
- ✏️ Форма для создания новой статьи
- ➕ Форма для добавления комментариев к статье
- 🔄 Редактирование существующей статьи
- ❌ Удаление существующей статьи
- 👥 Возможность указания имени автора для статей и комментариев
- ↩️ Возможность ответа на существующие комментарии (вложенные комментарии)

### Технологии

- Python 3
- Flask
- SQLite (через sqlite3)
- Jinja2
- HTML/CSS (Bootstrap)

### Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш-username/flask-blog.git
   cd flask-blog
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Инициализируйте базу данных:
   ```bash
   python db.py
   ```

4. Запустите приложение:
   ```bash
   python app.py
   ```

5. Откройте в браузере:
   ```
   http://localhost:5000
   ```

### Структура проекта

```
.
├── app.py                # Основное Flask-приложение
├── db.py                 # Работа с базой данных
├── blog.db               # Файл базы данных SQLite
├── requirements.txt      # Зависимости
└── templates             # Шаблоны Jinja2
    ├── base.html         # Базовый шаблон
    ├── create_post.html  # Форма создания поста
    ├── edit_post.html    # Форма редактирования поста
    ├── index.html        # Главная страница
    └── post.html         # Страница поста с комментариями
```

### Деплой

Для деплоя на хостинг (например, Heroku):

1. Установите Heroku CLI и войдите в систему:
   ```bash
   heroku login
   ```

2. Создайте новое приложение:
   ```bash
   heroku create your-app-name
   ```

3. Добавьте файл `Procfile` с содержимым:
   ```
   web: gunicorn app:app
   ```

4. Установите gunicorn:
   ```bash
   pip install gunicorn
   ```

5. Закоммитьте изменения и запушите на Heroku:
   ```bash
   git add .
   git commit -m "Prepare for deployment"
   git push heroku master
   ```

6. Откройте приложение:
   ```bash
   heroku open
   ```

### Дополнительные настройки

Для использования PostgreSQL вместо SQLite:

1. Установите psycopg2:
   ```bash
   pip install psycopg2-binary
   ```

2. Измените `get_db_connection()` в `db.py`:
   ```python
   def get_db_connection():
       conn = psycopg2.connect(
           host="your-host",
           database="your-db",
           user="your-user",
           password="your-password"
       )
       return conn
   ```

3. Обновите SQL-запросы в соответствии с синтаксисом PostgreSQL (замените `?` на `%s`).

 
