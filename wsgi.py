# wsgi.py
from flask import Flask, jsonify, request

app = Flask(__name__)



PRODUCTS = [
    { 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' },
    { 'id': 3, 'name': 'third.tv' },
    { 'id': 4, 'name': 'fourth.tv' }
]

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products')
def products():
    return jsonify (PRODUCTS)


@app.route('/api/v1/products/<int:id>', methods=['GET', 'DELETE'])
def product(id):
    if request.method == 'GET':
        for product in PRODUCTS:
            if product['id']==id:
                return jsonify(product)
        else:
            return "",404
    else:
        for product in PRODUCTS:
            if product['id']==id:
                PRODUCTS.remove(product)
                return "",204
        else:
            return "",404









