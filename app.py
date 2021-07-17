from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

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

# Configuration flask-migrate
migrate = Migrate()
migrate.init_app(app, db)

# CLasses
class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(60))
    description = db.Column(db.String(60))
    price = db.Column(db.Integer)

    def __str__(self):
        return (
            f'Id: {self.id}, '
            f'Product: {self.product}, '
            f'Description: {self.description}, '
            f'Price: {self.price}'
        )

# @app.route('/')
# def index():
#         return "Hola Mundo bienvenidos JEJEJE"
#
# @app.route('/homepage')
# def index2():
#         return "Hola, mi nombre es Alex Luna Toledo"
