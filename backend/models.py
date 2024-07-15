from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
#from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)


# User Model
class User(db.Model, SerializerMixin):

    serialize_rules = ('-reviews.user', '-orders.user',)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    email = db.Column(db.String(50), unique=True)
    # phone_number = db.Column(db.String(20))
    password = db.Column(db.String(60), nullable=False)
    reviews = db.relationship('Review', back_populates='user', lazy=True)
    orders = db.relationship('Order', back_populates='user', lazy=True)

    def __repr__(self):
        return f"<User ${self.name}>"

# Review Model
class Review(db.Model, SerializerMixin):

    serialize_rules = ('-user.reviews','-product.reviews',)
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    user = db.relationship('User', back_populates='reviews')
    product = db.relationship('Product', back_populates='reviews')
    def __repr__(self):
        return f"<Review ${self.body}>"

# Product Model
class Product(db.Model, SerializerMixin):

    serialize_rules = ('-reviews.product', '-category.products', '-orders.products',)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    price = db.Column(db.Float)
    image_url = db.Column(db.String(2000))
    description = db.Column(db.Text)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    reviews = db.relationship('Review', back_populates='product', lazy=True)
    #orders = db.relationship('OrderItem', back_populates='product', lazy=True)
    category = db.relationship('Category', back_populates='products')
    order_items = db.relationship('OrderItem', back_populates='product')

    def __repr__(self):
        return f"<Product ${self.name}, {self.price}, {self.description}>"

# Category Model
class Category(db.Model, SerializerMixin):

    serialize_rules = ('-products.category',)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    products = db.relationship('Product', back_populates='category', lazy=True)


    def __repr__(self):
        return f"<Category ${self.name}>"

# Order Model
class Order(db.Model, SerializerMixin):

    serialize_rules = ('-user.orders', '-order_items.order',)
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    total_price = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='orders')
    order_items = db.relationship('OrderItem', back_populates='order')
    def __repr__(self):
        return f"<Order ${self.quantity}, {self.total_price}>"

# OrderItem Model (to handle many-to-many relationship between Order and Product)
class OrderItem(db.Model, SerializerMixin):

    serialize_rules = ('-order.order_items',)
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    order = db.relationship('Order', back_populates='order_items')
    product = db.relationship('Product',back_populates="order_items")
    
# add validation
    @validates('price')
    def validate_price(self, key, price):
        if not (price > 0):
            raise ValueError("Price must be more than 0")
        return price

