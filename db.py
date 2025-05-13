import sqlite3
from sqlite3 import Row  # Для работы с row_factory

def get_db_connection():
    conn = sqlite3.connect('blog.db')
    conn.row_factory = Row  # Возвращаем словари вместо кортежей
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Создаем таблицу постов
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            author_name TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Создаем таблицу комментариев
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            post_id INTEGER REFERENCES posts(id) ON DELETE CASCADE,
            author_name TEXT,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            parent_id INTEGER REFERENCES comments(id) ON DELETE SET NULL
        )
    """)
    
    conn.commit()
    conn.close()