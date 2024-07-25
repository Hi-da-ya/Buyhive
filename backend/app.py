from flask import Flask, request, make_response, jsonify, current_app
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS
import jwt
from datetime import datetime, timedelta
from functools import wraps
import os
from flask_bcrypt import Bcrypt

from models import db, Product, User, Order, OrderItem, Category, Review

app = Flask(__name__)
api = Api(app) 

# Configuring db connection with app.db file
CORS(app)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)
bcrypt = Bcrypt(app)

CORS(app)
class Home(Resource):
    def get(self):
        return "<h1>Welcome to Buy Hive</h1>"

# Products resource
class Products(Resource):
    def get(self):
        products = [product.to_dict() for product in Product.query.all()]
        return make_response(jsonify(products), 200)

class ProductById(Resource):
    def get(self, id):
        product = Product.query.filter_by(id=id).first()
        if product:
            return make_response(jsonify(product.to_dict()), 200)
        else:
            return make_response(jsonify({"error": "Product not found"}), 404)

# Categories resource
class Categories(Resource):
    def get(self):
        categories = [category.to_dict() for category in Category.query.all()]
        return make_response(jsonify(categories), 200)

class CategoryById(Resource):
    def get(self, id):
        category = Category.query.filter_by(id=id).first()
        if category:
            return make_response(jsonify([category.to_dict()]), 200)
        else:
            return make_response(jsonify({"error": "Category not found"}), 404)

# Reviews resource
class Reviews(Resource):
    def get(self):
        reviews = [review.to_dict() for review in Review.query.all()]
        return make_response(jsonify(reviews), 200)

    def post(self):
        pass

class ReviewById(Resource):
    def get(self, id):
        review = Review.query.filter_by(id=id).first()
        if review:
            return make_response(jsonify(review.to_dict()), 200)
        else:
            return make_response(jsonify({"error":"Review not found"}), 404)

    def delete(self, id):
        review = Review.query.filter_by(id=id).first()
        if review:
            db.session.delete(review)
            db.session.commit()
            response_dict = {"message": "Record successfully deleted"}
            return make_response(jsonify(response_dict), 204)
        else:
            return make_response(jsonify({"error": "Review not found"}), 404)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.filter_by(username=data['user']).first()
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 403
        except (jwt.InvalidTokenError, jwt.DecodeError):
            return jsonify({'message': 'Token is invalid!'}), 403
        if not current_user:
            return jsonify({'message': 'User not found!'}), 404
        return f(current_user, *args, **kwargs)
    return decorated

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    if 'username' not in data or 'password' not in data or 'email' not in data:
        return jsonify({'message': 'Missing username, password, or email!'}), 400
    
    existing_user = User.query.filter_by(username=data['username']).first()
    if existing_user:
        return jsonify({'message': 'Username already exists!'}), 409
    
    existing_email = User.query.filter_by(email=data['email']).first()
    if existing_email:
        return jsonify({'message': 'Email already exists!'}), 409
    
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], email=data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully!'})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if 'email' not in data or 'password' not in data:
        return jsonify({'message': 'Missing email or password!'}), 400

    user = User.query.filter_by(email=data['email']).first()
    if not user or not bcrypt.check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Invalid credentials!'}), 401
    
    token = jwt.encode({
        'user': user.username,
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }, current_app.config['SECRET_KEY'], algorithm="HS256")
    return jsonify({'token': token})

@app.route('/protected', methods=['GET'])
@token_required
def protected(current_user):
    return jsonify({'message': f'Welcome {current_user.username}!'})

@app.route('/logout', methods=['POST'])
@token_required
def logout(current_user):
    # Implement logout functionality here if needed (e.g., token blacklist)
    return jsonify({'message': 'User logged out successfully!'})

def init_db():
    with app.app_context():
        db.create_all()

# Users resource
class Users(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        return make_response(jsonify(users), 200)

class UserById(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if user:
            return make_response(jsonify(user.to_dict()), 200)
        else:
            return make_response(jsonify({"error": "User not found"}), 404)

    def delete(self, id):
        user = User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            response = {"message": "User successfully deleted"}
            return make_response(jsonify(response), 204)
        else:
            return make_response(jsonify({"error": "User not found"}), 404)

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
            return make_response(jsonify({"error": "User not found"}), 404)

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
    init_db()
    app.run(port=5555, debug=True)
