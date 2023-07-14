from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Fungsi ini akan membuka koneksi ke database dan mengembalikan objek koneksi
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Fungsi ini akan menutup koneksi ke database
def close_db_connection(conn):
    conn.close()

# Fungsi ini akan menginisialisasi tabel dan menambahkan beberapa data awal ke dalamnya
def init_database():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS data (
        	no INTEGER NOT NULL,
            nim INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            asal TEXT NOT NULL,
            prodi TEXT NOT NULL,
            jenjang TEXT NOT NULL

        )
    ''')
    cursor.execute('SELECT COUNT(*) FROM data')
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.execute('''
            INSERT INTO data (no, nim, nama, asal, prodi, jenjang) VALUES
            (1, 195410229, 'Satria Dwi H', 'Bantul', 'TI', 'S1' ),
            (1, 195410230, 'Reza Dian S', 'Bantul', 'TI', 'S1'),
            (1, 195410231, 'Ikhsan', 'Kulon Progo', 'TI', 'S1')
        ''')
    conn.commit()
    close_db_connection(conn)

# Route untuk menampilkan data dari tabel
@app.route('/data')
def data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM data')
    rows = cursor.fetchall()
    close_db_connection(conn)
    return render_template('data.html', rows=rows)

if __name__ == '__main__':
    init_database()
    app.run()