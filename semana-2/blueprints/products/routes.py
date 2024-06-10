from flask import Blueprint, jsonify, request
from extensions import db
from entities.product_model import Product


products_bp = Blueprint('products', __name__)

'''
Reto 1 : crear la ruta y la funcion para obtener todos los productos
'''

@products_bp.route('/api/v1/product')
def get_all_products():
    try:
        products = Product.query.all()
        dict_products =[]
        for product in products:
            dict_products.append(product.to_dict())

        return jsonify({
            "products": dict_products
        })

    except Exception as e:
        return jsonify({
            "error": e
        }), 500
    



"""
Retos 2: crear la ruta y la funcion la cual me permita crear un producto POST 
"""
# POST : crear
@products_bp.route('/api/v1/product', methods=['POST'])
def create_product():
    try:

        product_data = request.get_json()
        new_product = Product(
            name = product_data["name"],
            description = product_data["description"],
            price = product_data["price"],
            stock = product_data["stock"]
        )

        db.session.add(new_product) # se usa solo cuando se esta creando algo
        db.session.commit()  # COMMIT (SAVEPOINT)

        return jsonify({
            "message": new_product.to_dict()
        }), 201
    except Exception as e:
        return jsonify({
            "error": e
        }), 500

