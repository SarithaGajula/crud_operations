from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy object
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'  # Define a table name (optional, defaults to class name)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)  # Add uniqueness constraint

    def __repr__(self):
        return f'<User {self.name}>'
