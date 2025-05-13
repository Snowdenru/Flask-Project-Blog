from flask import Flask, render_template, request, redirect, url_for, flash
from db import get_db_connection, init_db

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Главная страница
@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts ORDER BY created_at DESC').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

# Просмотр поста
@app.route('/post/<int:post_id>')
def post(post_id):
    conn = get_db_connection()
    
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    comments = conn.execute('''
        SELECT * FROM comments 
        WHERE post_id = ? AND parent_id IS NULL
        ORDER BY created_at DESC
    ''', (post_id,)).fetchall()
    
    conn.close()
    
    if post is None:
        flash('Post not found')
        return redirect(url_for('index'))
    
    return render_template('post.html', post=post, comments=comments)

# Создание поста
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author_name = request.form.get('author_name', 'Anonymous')
        
        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute(
                'INSERT INTO posts (title, content, author_name) VALUES (?, ?, ?)',
                (title, content, author_name)
            )
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    
    return render_template('create_post.html')

# Редактирование поста
@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        
        if not title:
            flash('Title is required!')
        else:
            conn.execute(
                'UPDATE posts SET title = ?, content = ? WHERE id = ?',
                (title, content, post_id)
            )
            conn.commit()
            conn.close()
            return redirect(url_for('post', post_id=post_id))
    
    conn.close()
    
    if post is None:
        flash('Post not found')
        return redirect(url_for('index'))
    
    return render_template('edit_post.html', post=post)

# Удаление поста
@app.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (post_id,))
    conn.commit()
    conn.close()
    flash('Post deleted successfully')
    return redirect(url_for('index'))

# Добавление комментария
@app.route('/post/<int:post_id>/comment', methods=['POST'])
def add_comment(post_id):
    author_name = request.form.get('author_name', 'Anonymous')
    content = request.form['content']
    parent_id = request.form.get('parent_id')
    
    if not content:
        flash('Comment content is required!')
    else:
        conn = get_db_connection()
        
        if parent_id:
            conn.execute(
                'INSERT INTO comments (post_id, author_name, content, parent_id) VALUES (?, ?, ?, ?)',
                (post_id, author_name, content, parent_id)
            )
        else:
            conn.execute(
                'INSERT INTO comments (post_id, author_name, content) VALUES (?, ?, ?)',
                (post_id, author_name, content)
            )
        
        conn.commit()
        conn.close()
    
    return redirect(url_for('post', post_id=post_id))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)