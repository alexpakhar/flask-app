import os
import time
import psycopg2
from flask import Flask

app = Flask(__name__)

def get_db():
    return psycopg2.connect(
        host=os.environ.get('DB_HOST', 'db'),
        database=os.environ.get('DB_NAME', 'testdb'),
        user=os.environ.get('DB_USER', 'testuser'),
        password=os.environ.get('DB_PASSWORD', 'P@ssw0rd2026!')
    )

@app.route('/')
def index():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute('SELECT version();')
        version = cur.fetchone()[0]
        cur.close()
        conn.close()
        return f'<h1>Flask + PostgreSQL</h1><p>Подключено к: {version}</p>'
    except Exception as e:
        return f'<h1>Ошибка подключения</h1><p>{e}</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
