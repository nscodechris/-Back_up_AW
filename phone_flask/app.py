from flask import *
import datetime
import sqlite3
import psycopg2


'''dum = [
  ['arne', '013-131313'], ['berith','01234'], ['caesar','077-1212321']
]'''
'''conn = psycopg2.connect(
                database='phone', user='postgres', password='Cvmillan10!?', host='localhost', port='5432')'''


def read_phonelist(C):
    cur = C.cursor()
    cur.execute("SELECT * FROM phonelist;")
    rows = cur.fetchall()
    cur.close()
    return rows
def add_phone(C, name, phone):
    cur = C.cursor()
    cur.execute(f"INSERT INTO phonelist (name, phone) VALUES ('{name}', '{phone}');")
    cur.close()
def delete_phone(C, name):
    cur = C.cursor()
    cur.execute(f"DELETE FROM phonelist WHERE name = '{name}';")
    cur.close()

def update_phone(C, name, phone, name_id):
    cur = C.cursor()
    cur.execute(f"UPDATE phonelist SET name = '{name}', phone = '{phone}' WHERE name_id = {name_id};")
    cur.close()


def save_phonelist(C):
    cur = C.cursor()
    try:
        cur.execute("COMMIT;")
    except:
        print("No changes!")
    cur.close()



app = Flask(__name__)

@app.route("/")
def start():
    conn = sqlite3.connect("phone.db")
    smart = read_phonelist(conn)
    now = datetime.datetime.now()
    D = [str(now.year%100), str(now.month), str(now.day)]
    if len(D[1])<2:
        D[1] = '0'+D[1]
    if len(D[2])<2:
        D[2] = '0'+D[2]
    return render_template('list.html', list=smart, date=D)


@app.route("/delete")
def delete_func():
    conn = sqlite3.connect("phone.db")
    name = request.args['name']
    delete_phone(conn, name)
    save_phonelist(conn)
    return render_template('delete.html', name=name)

@app.route("/insert")
def insert_func():
    conn = sqlite3.connect("phone.db")
    name = request.args['name']
    phone = request.args['phone']
    add_phone(conn, name, phone)
    save_phonelist(conn)
    return render_template('insert.html', name=name, phone=phone)

@app.route("/update")
def update_func():
    conn = sqlite3.connect("phone.db")
    smart = read_phonelist(conn)
    name_id = request.args['name_id']
    name = request.args['name']
    phone = request.args['phone']
    update_phone(conn, name, phone, name_id)
    save_phonelist(conn)
    return render_template('update.html', list=smart, name_id=name_id, name=name, phone=phone)
