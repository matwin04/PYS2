from bottle import request, route, run, static_file, template, redirect
import socket
import sqlite3
#define IP
ip=socket.gethostbyname(socket.gethostname())
#Connect To Database
db = './pys2.db'
conn = sqlite3.connect(db)
c = conn.cursor()
#Define Route
@route('/pages/<filename:path>')
def serve_static(filename):
    return static_file(filename, root='./pages/')

@route('/')
def index():
    return template("./pages/index.html")
@route('/ps2')
def lines():
    c.execute("SELECT id, name, region, year FROM ps2")
    result = c.fetchall()
    region = request.query.get('region')
    print(region)
    output = template('./pages/ps2.html',
                      rows=result,
                      region=region,
                      )
    return output

@route('/psp')
def psp():
    c.execute("SELECT id, name FROM psp")
    result = c.fetchall()
    output = template('./pages/psp.html',
                      rows=result,
                      )
    return 
@route("/games/new",method="GET")
def new_game():
    if request.GET.get('add','').strip():
        name = request.GET.get('name','').strip()
        c.execute("INSERT INTO games (name) VALUES (?)", (name))
        conn.commit()
        return redirect('/games')
    else:
        return template('./pages/new_game.html')

run(host=ip,port=5555,debug=True,reloader=True,)