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
        
#Reviews resource
class Reviews(Resource):
    def get(self):
        reviews = [review.to_dict() for review in Review.query.all()]
        return make_response(jsonify(reviews), 200)
    
    def post(self):
        pass

class ReviewById(Resource):
    def get(self, id):
        review = Review.query.filter_by(id = id).first()
        if review:
            return make_response(jsonify(review.to_dict()), 200)
        else:
            return make_response(jsonify({"error":"review not found"}), 404)

    def delete(self, id):
        review = Review.query.filter_by(id = id).first()
        if review:
            db.session.delete(review)
            db.session.commit()
            response_dict = {"message": "Record successfully deleted"}
            return make_response(jsonify(response_dict), 204)
        else:
            return make_response(jsonify({"error": "Review not found"}), 404) 

#Users resource
class Users(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        return make_response(jsonify(users), 200)

    def post(self):
        pass 

class UserById(Resource):
    def get(self, id):
        user = User.query.filter_by(id = id).first()
        if user:
            return make_response(jsonify(user.to_dict()), 200)
        else:
            return make_response(jsonify({"error": "user not found"}), 404)

    def delete(self, id):
        user = User.query.filter_by(id = id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            response = {"message": "User successfully deleted"}
            return make_response(jsonify(response), 204)
        else:
            return make_response(jsonify({"error": "user not found"}), 404)

    #edit an attribute in user profile
    def patch(self, id):
        record = User.query.filter_by(id=id).first()
        if record:
            for attr in request.form:
                setattr(record, attr, request.form[attr])

            db.session.add(record)
            db.session.commit()

            response_dict = record.to_dict()

            response = make_response(jsonify(response_dict), 200)
            return response

        else:
            return make_response(jsonify({"error": "user not found"}), 404) 

api.add_resource(Home, '/')
api.add_resource(Products, '/products')
api.add_resource(ProductById, '/products/<int:id>')
api.add_resource(Reviews, '/reviews')
api.add_resource(ReviewById, '/reviews/<int:id>')
api.add_resource(Users, '/users')
api.add_resource(UserById, '/users/<int:id>')
api.add_resource(Categories, '/categories')
api.add_resource(CategoryById, '/categories/<int:id>')


@app.errorhandler(404)
def not_found_error(error):
    return make_response(jsonify({"error": "Not Found"}), 404)


if __name__ == '__main__':
    app.run(port=5555, debug=True)               
    