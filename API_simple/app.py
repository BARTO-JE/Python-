from crypt import methods
from flask import Flask, jsonify,request

app = Flask(__name__)

from productos import productos

@app.route('/ping') #Las rutas permite especificar los metodo HTTP, por defecto las rutas funcionan con metodo GET
def ping():
    return jsonify({"message":"Pong!"})


@app.route('/productos')
def get_productos():
    return jsonify({'Productos': productos, 'mensaje': "Lista de productos"})

@app.route('/productos/<string:nombre_producto>')
def get_producto(nombre_producto):
    busca_producto = [producto for producto in productos if producto['nombre'] == nombre_producto]
    if (len(busca_producto) > 0):
        return jsonify({'producto':busca_producto[0]})
    return jsonify({'mensaje':'Producto no encontrado' })

@app.route('/productos', methods = ['POST'])
def agregar_productos():
    nuevo_producto = {
        "nombre": request.json['nombre'], 
        "precio": request.json['precio'], 
        "cantidad":request.json['cantidad']
    }
    productos.append(nuevo_producto)
    return jsonify({"mensaje":"Prodcuto agregado satisfactoriamente","productos":productos})

@app.route('/productos/<string:nombre_producto>', methods = ['PUT'])
def editProducto(nombre_producto):
    busca_producto = [producto for producto in productos if producto['nombre'] == nombre_producto]
    if (len(busca_producto) > 0):
        busca_producto[0]['nombre'] = request.json ['nombre']
        busca_producto[0]['precio'] = request.json ['precio']
        busca_producto[0]['cantidad'] = request.json ['cantidad']
        return jsonify({
            "mensaje": 'Prodcuto actualizado',
            "producto": busca_producto[0]
        })
    return jsonify({"mensaje": 'Prodcuto no encontrado'})        

@app.route('/productos/<string:nombre_producto>', methods = ['DELETE'])
def eliminarProducto(nombre_producto):
    producto_encontrado=[producto for producto in productos if producto['nombre'] == nombre_producto]
    if len(producto_encontrado) > 0:
        productos.remove(producto_encontrado[0])
        return jsonify({
            "mensaje" : "Producto eliminado",
            "productos" : productos
        })
    return jsonify({"mensaje":"Producto no encontrado"})
if __name__ == '__main__':
    app.run(debug = True, port = 5000) 
