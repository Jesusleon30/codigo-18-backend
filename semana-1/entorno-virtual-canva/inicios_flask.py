from flask import Flask, request


# indicar si nuestro archivo es el archivo principal , si el archivo es el principal su valor sera "__main__"
app = Flask(__name__)

productos = [
    {
        "id": 1,
        "nombre": "platano",
        "precio": 3.50
    },
    {
        "id": 2,
        "nombre": "sandia",
        "precio": 2.80
    },
    {
        "id": 3,
        "nombre": "tomate",
        "precio": 2.30
    },
]

# decorador
@app.route("/")
def inicio():
    # modificar el comportamiento del metodo route de la clase Flask para evitar modificar el metodo en la misma clase
    print("hola")
    return "bienvenido a mi aplicacion "


@app.route("/productos", methods=['GET', 'POST'])
def gestion_productos():
    print (request.method)
    if request.method == 'GET':
        return{
            'content': productos
        }
    elif request.method == 'POST':
        # get_json() > convierte la data entrante a un formato diccionario
        print(request.get_json())
        data = request.get_json()
        #print(data.get('id'))
        productos.append(data)
        return{
            'message': 'producto creado exitosamente'
        }
    return {
        "content": productos
    }


if __name__ == "__main__":
    app.run(debug=True)
