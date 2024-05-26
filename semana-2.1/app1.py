from flask import Flask, jsonify, request
import bcrypt

# este va hacer el main principal del proyecto
app = Flask(__name__)  # "__name__" == "__main__"


# creo una variable users y dentro este array vacio voy a guardar los usuarios que se creen mediante el postman
users = []


def encrypt_password(password):
    """
    1 paso:
    generar un salt 
    salt: es un numero aleatorio que se genera y es concatenado al password, este se usa 
    por seguridad y para evitar ataques de fuerza bruta
    """
    salt = bcrypt.gensalt()  # esto se encarga de generar un numero en automatico y ese numero se le agrega al password
    return bcrypt.hashpw(password.encode('utf-8'), salt)
# vamos a tener que incryptar y desincryptar


# decorador comienza con @app..... en este caso me permite crear una ruta
# despues del decorador va una funcion van siempre juntos

@app.route('/')
def home():
    return jsonify(users)


# metodo osea que metodo sopporta la url que va hacer post
@app.route('/api/v1/user', methods=['POST'])
def create_user():
    try:
        user_data = request.get_json()
        user_data['password'] = encrypt_password(user_data.get('password')).decode('utf-8')
    # request.get_data('password') esto esta buscando el dato que tenga este valor password
    # y en aca  user_data['password'] lo estamos sobreescribiendo

    # agregar un elemento a un array python es mediante .append
        users.append(user_data)

        return jsonify({
            "new_user": user_data
        })
    except Exception as e:
        return jsonify({
            "error": e,
            "linea": e.__traceback__.tb_lineno
        })


if __name__ == '__main__':
    app.run(port=7000, debug=True)
    # app.run(port=7000, debug=True)
    # si da error con 5000  meter port=7000 le cambiamos el portal en este caso
