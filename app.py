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

@app.route('/supuestos')
def supuestos():
    return render_template('supuestos.html')

#############MOSTRAR VISTAS####################

#############Peticiones para traer informacion###########

@app.route('/cigarrillos')
def cigarrillos():
    return render_template('/mostrar/cigarrillos.html')

@app.get('/api/lista-de-cigarrillos')
def get_lista_cigarrillos():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('SELECT * FROM CIGARRILLOS')
    cigarrillos = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(cigarrillos)

@app.route('/estancos')
def estancos():
    return render_template('/mostrar/estancos.html')

@app.get('/api/lista-de-estancos')
def get_lista_estancos():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('SELECT * FROM ESTANCOS')
    estancos = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(estancos)

@app.route('/almacenes')
def almacenes():
    return render_template('/mostrar/almacenes.html')

@app.get('/api/lista-de-almacenes')
def get_lista_almacenes():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('SELECT * FROM ALMACENES')
    almacenes = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(almacenes)

@app.route('/compras')
def compras():
    return render_template('/mostrar/compras.html')

@app.get('/api/lista-de-compras')
def get_lista_compras():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('SELECT * FROM COMPRAS')
    compras = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(compras)

@app.route('/ventas')
def ventas():
    return render_template('/mostrar/ventas.html')

@app.get('/api/lista-de-ventas')
def get_lista_ventas():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('SELECT * FROM VENTAS')
    ventas = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(ventas)

@app.route('/fabricantes')
def fabricantes():
    return render_template('/mostrar/fabricantes.html')

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
    return render_template('/mostrar/manufactura.html')

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
    return render_template('/agregar/agregarfabricante.html')

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

@app.route('/agregar-manufactura')
def agregar_manufactura():
    return render_template('/agregar/agregarmanufactura.html')

@app.post('/api/agregar-manufactura')
def create_manufactura():
    new_manufactura = request.get_json()
    marca_manufactura = new_manufactura['marca']
    nombre_fabricante = new_manufactura['nombre_fabricante']
    carton = new_manufactura['carton']
    embalaje = new_manufactura['embalaje']

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('INSERT INTO MANUFACTURA (MARCA, NOMBRE_FABRICANTE, CARTON, EMBALAJE) VALUES (%s, %s, %s, %s) RETURNING *', (marca_manufactura, nombre_fabricante, carton, embalaje))
    new_created_manufactura = cur.fetchone()
    conn.commit()

    cur.close()
    conn.close()
    return jsonify(new_created_manufactura)

@app.route('/agregar-compra')
def agregar_compra():
    return render_template('/agregar/agregarcompra.html')


@app.post('/api/agregar-compra')
def create_compra():
    new_compra = request.get_json()
    nif_estanco = new_compra['nif_estanco']
    marca = new_compra['marca']
    filtro = new_compra['filtro']
    color = new_compra['color']
    clase = new_compra['clase']
    mentol = new_compra['mentol']
    fecha_compra = new_compra['fecha_compra']
    c_comprada = new_compra['c_comprada']
    precio_compra = new_compra['precio_compra']

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('INSERT INTO COMPRAS (NIF_ESTANCO, MARCA, FILTRO, COLOR, CLASE, MENTOL, FECHA_COMPRA, C_COMPRADA, PRECIO_COMPRA) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *', 
                (nif_estanco, marca, filtro, color, clase, mentol, fecha_compra, c_comprada, precio_compra))
    new_created_compra = cur.fetchone()
    conn.commit()

    cur.close()
    conn.close()
    return jsonify(new_created_compra)

@app.route('/agregar-venta')
def agregar_venta():
    return render_template('/agregar/agregarventas.html')

@app.post('/api/agregar-venta')
def create_venta():
    new_venta = request.get_json()
    nif_estanco = new_venta['nif_estanco']
    marca = new_venta['marca']
    filtro = new_venta['filtro']
    color = new_venta['color']
    clase = new_venta['clase']
    mentol = new_venta['mentol']
    fecha_venta = new_venta['fecha_venta']
    c_venta = new_venta['c_venta']
    precio_venta = new_venta['precio_venta']

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('INSERT INTO COMPRAS (NIF_ESTANCO, MARCA, FILTRO, COLOR, CLASE, MENTOL, FECHA_VENTA, C_VENDIDA, PRECIO_VENTA) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *', 
                (nif_estanco, marca, filtro, color, clase, mentol, fecha_venta, c_venta, precio_venta))
    new_created_venta = cur.fetchone()
    conn.commit()

    cur.close()
    conn.close()
    return jsonify(new_created_venta)

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

##############REPORTES################
@app.route('/reporte-ventas')
def agregar_reporte_ventas():
    return render_template('/reportes/reporteventas.html')

@app.route('/api/reporte-ventas')
def get_reporte_ventas():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('SELECT MARCA, SUM(C_VENDIDA) as total_vendida FROM VENTAS GROUP BY MARCA')
    data = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return jsonify(data)

@app.route('/reporte-compras')
def agregar_reporte_compras():
    return render_template('/reportes/reportecompras.html')

@app.route('/api/reporte-compras')
def get_reporte_compras():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('SELECT MARCA, SUM(C_COMPRADA) as total_comprada FROM COMPRAS GROUP BY MARCA')
    data = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return jsonify(data)

@app.route('/reporte-cigarrillos')
def agregar_reporte_cigarrillos():
    return render_template('/reportes/reportecigarrillos.html')

@app.route('/api/reporte-cigarrillos')
def get_reporte_cigarrillos():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('SELECT MARCA, COUNT(*) as total_cigarrillos FROM CIGARRILLOS GROUP BY MARCA')
    data = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return jsonify(data)

@app.route('/reporte-ventas-estanco')
def agregar_reporte_ventas_estanco():
    return render_template('reportes/reporteventasestanco.html')

@app.route('/api/reporte-ventas-estanco')
def get_reporte_ventas_estanco():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('''
        SELECT NIF_ESTANCO, SUM(C_VENDIDA) as total_vendida
        FROM VENTAS
        GROUP BY NIF_ESTANCO
    ''')
    data = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return jsonify(data)

@app.route('/reporte-stock')
def agregar_reporte_stock():
    return render_template('/reportes/reportestock.html')

@app.route('/api/reporte-stock')
def get_reporte_stock():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    # Consulta SQL para obtener el stock actual por estanco
    cur.execute('''
        SELECT NIF_ESTANCO, MARCA, SUM(UNIDADES) as total_unidades
        FROM ALMACENES
        GROUP BY NIF_ESTANCO, MARCA
    ''')
    data = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return jsonify(data)

@app.route('/reporte-compras-fecha')
def agregar_reporte_compras_fecha():
    return render_template('/reportes/reportecomprasfecha.html')

@app.route('/api/reporte-compras-fecha')
def get_reporte_compras_fecha():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    # Consulta SQL para obtener las compras agrupadas por fecha
    cur.execute('''
        SELECT FECHA_COMPRA, SUM(C_COMPRADA) as total_comprada
        FROM COMPRAS
        GROUP BY FECHA_COMPRA
        ORDER BY FECHA_COMPRA
    ''')
    data = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
