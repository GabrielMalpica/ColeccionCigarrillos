from flask import Flask, send_file, request, jsonify,render_template
from psycopg2 import connect, extras

app = Flask(__name__)

host = 'localhost'
port = 5432
dbname = 'ventacigarrillos'
user = 'postgres'
password = '123456'

def get_connection():
    conn = connect(host=host, port=port, dbname=dbname,user = user, password=password)
    return conn

@app.get('/')
def home():
    return send_file('static/index.html')

#############Peticiones para traer informacion###########
@app.route('/cigarrillos')
def cigarrillos():
    return render_template('cigarrillos.html')

@app.get('/api/lista-de-cigarrillos')
def get_lista_cigarrillos():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('SELECT * FROM CIGARRILLOS')
    cigarrillos = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(cigarrillos)

@app.get('/api/lista-de-estancos')
def get_lista_estancos():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('SELECT * FROM ESTANCOS')
    estancos = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(estancos)

@app.get('/api/lista-de-almacenes')
def get_lista_almacenes():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('SELECT * FROM ALMACENES')
    almacenes = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(almacenes)


@app.get('/api/lista-de-compras')
def get_lista_compras():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('SELECT * FROM COMPRAS')
    compras = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(compras)

@app.route('/fabricantes')
def fabricantes():
    return render_template('fabricantes.html')

@app.get('/api/lista-de-fabricantes')
def get_lista_fabricantes():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('SELECT * FROM FABRICANTES')
    fabricantes = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(fabricantes)

@app.route('/manufactura')
def manufactura():
    return render_template('manufactura.html')

@app.get('/api/lista-de-manufactura')
def get_lista_manufactura():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('SELECT * FROM MANUFACTURA')
    manufactura = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(manufactura)

################################################################

############Peticiones para guardar informacion################
@app.route('/agregar-fabricante')
def agregar_fabricante():
    return render_template('agregarfabricante.html')

@app.post('/api/agregar-fabricante')
def create_fabricante():
    new_fabricante = request.get_json()
    nombre_fabricante = new_fabricante['fabricante']
    pais_fabricante = new_fabricante['pais']

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('INSERT INTO FABRICANTES (NOMBRE_FABRICANTE,PAIS) VALUES (%s,%s) RETURNING *',(nombre_fabricante,pais_fabricante))
    new_created_fabricante = cur.fetchone()
    print(new_created_fabricante)
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(new_created_fabricante)

##############Peticiones para actualizar informacion###############

@app.put('/api/manufactura/<id>')
def update_manufactura(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    new_manufactura_data = request.get_json()
    nombre_fabricante = new_manufactura_data['nombre_fabricante']
    carton = new_manufactura_data['carton']
    embalaje = new_manufactura_data['embalaje']

    cur.execute('UPDATE MANUFACTURA nombre_fabricante = %s, carton = %s, embalaje = %s WHERE id = %s RETURNING *',(nombre_fabricante,carton,embalaje,id))
    updated_manufactura = cur.fetchone()

    conn.commit()

    cur.close()
    conn.close()

    if update_manufactura is None:
        return jsonify({'message':'User not found'}),404

    return jsonify(update_manufactura)

if __name__ == '__main__':
    app.run(debug=True)
