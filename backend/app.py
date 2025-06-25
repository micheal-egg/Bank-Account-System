from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)

# 🔧 Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:<your_password>@localhost/banking_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 🔒 JWT Configuration
app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Change this to something secure
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)

# 🔌 Initialize Extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# 🧾 User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

# 🔐 Register Route
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "User already exists"}), 400

    hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")
    new_user = User(email=email, password=hashed_pw)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

# 🔐 Login Route
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()

    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity=email)
    return jsonify({"access_token": access_token}), 200

# Protected Route 
@app.route("/dashboard", methods=["GET"])
@jwt_required()
def dashboard():
    return jsonify({"message": "Welcome to your banking dashboard!"})

# ⚙️ Create Tables and Run App
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Creates tables if they don't exist yet
    app.run(debug=True)
