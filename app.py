from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app=Flask(__name__)

# Configuration Data base
USER_DB = 'postgres'
PASS_DB = 'axr12345'
URL_DB = 'localhost'
NAME_DB = 'techbuy'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'
print(FULL_URL_DB)

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialize Data Base
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Configuration flask-migrate
migrate = Migrate()
migrate.init_app(app, db)

# CLasses
class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(60))
    description = db.Column(db.String(200))
    price = db.Column (db.Float)

    def __init__(self, product, description, price):
        self.product = product
        self.description = description
        self.price = price

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'product', 'description', 'price')

# Init schema
productSchema = ProductSchema()
productsSchema = ProductSchema(many=True)

# Create a new Product
@app.route("/api/product", methods=["POST"])
def addProduct():
    product = request.json["product"]
    description = request.json["description"]
    price = request.json["price"]

    createdProduct = Products(product, description, price)

    db.session.add(createdProduct)
    db.session.commit()

    return jsonify(productSchema.dump(createdProduct))

# Get All Products List
@app.route('/api/products', methods=['GET'])
def sendProducts():
        getAllProducts = Products.query.all()
        return jsonify(productsSchema.dump(getAllProducts))

# Get individual data of product
@app.route('/api/product/<id>', methods=['GET'])
def sendProduct(id):
        getProduct = Products.query.get(id)
        return jsonify(productSchema.dump(getProduct))

# Not finished fuction
@app.route('/api/search/<search>', methods=['GET'])
def sendProductName(search):
        getProductByName = Products.query.filter_by(product=search).first()
        return jsonify(productSchema.dump(getProductByName))
