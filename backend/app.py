from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Product,User, Order, OrderItem, Category, Review

app = Flask(__name__)
api = Api(app)

#configuring db connection with app.db file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)


class Home(Resource):
    def get(self):
        return "<h1>Welcome to Buy Hive</h1>"

#Products resource
class Products(Resource):
    def get(self):
        products = [product.to_dict() for product in Product.query.all()]
        return make_response(jsonify(products), 200)

class ProductById(Resource):
    def get(self, id):
        product = Product.query.filter_by(id = id).first()
        if product:
            return make_response(jsonify(product.to_dict()), 200)
        else:
            return make_response(jsonify({"error": "product not found"}), 404)

#Categories resource
class Categories(Resource):
    def get(self):
        categories = [category.to_dict() for category in Category.query.all()]
        return make_response(jsonify(categories), 200)
    

class CategoryById(Resource):
    def get(self, id):
        category = Category.query.filter_by(id = id).first()
        if category:
            return make_response(jsonify([category.to_dict()]), 200)
        else:
            return make_response(jsonify({"error": "category not found"}), 404)
    