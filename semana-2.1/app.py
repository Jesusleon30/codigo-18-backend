from flask import Flask, jsonify, request

# este va hacer el main principal del proyecto
app = Flask(__name__)  # "__name__" == "__main__"


# decorador comienza con @app..... en este caso me permite crear una ruta
# despues del decorador va una funcion van siempre juntos


@app.route('/')
def home():
    datos = {
        "celulares": [
            {
                "id": 1,
                "marca": "apple",
                "modelo": "iPhone 15"
            },
            {
                "id": 2,
                "marca": "apple",
                "modelo": "iPhone 15"
            },
            {
                "id": 3,
                "marca": "apple",
                "modelo": "iPhone 15"
            }

        ]}

    return jsonify(datos)
    # return jsonify({
    #     "message": "hola mundo desde flask"
    # })


"""
vamos a hacer un ejemplo donde vamos a recibir la informacion del usuario pero desde POSTMAN
"""
"""
para recivir un dato del cliente atraverso postman requiero de importar de un request
"""


# metodo osea que metodo sopporta la url que va hacer post
@app.route('/api/v1/user', methods=['POST'])
def create_user():
    # quiere decir que va a tomar el json que envie el cliente y lo va a guardar en la variable user_data
    # en este caso el cliente es Postman
    user_data = request.get_json()
    # print (user_data)
    return jsonify({
        "new_user": user_data
    })


# para poder hacer que esto se ejecute mediante un servidor
# flask tiene esto implementado app.run(debug=True)
#  app.run que hace? lo que hace es crear un servidor local donde nos permite ejecutar en la computer
# debug=True  nos va hacer ver los log del computer para ver en tiempo real los cambios hechos xk si esta en false se va a mantener sin ver cambios
# buena practica es envolverlo en un if
if __name__ == '__main__':
    app.run(debug=True)
    # app.run(port=7000, debug=True)
    # si da error meter port=7000 le cambiamos el portal
