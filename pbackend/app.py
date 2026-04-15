"""
Main application entry point.
Sets up Flask app, database, JWT, and registers blueprints.
"""

from flask import Flask
from flask_migrate import Migrate
from services.db import db, bcrypt
from flask_jwt_extended import JWTManager
from routes.auth import auth_bp
from routes.notes import notes_bp
from cli import seed   # import the seed command

def create_app():
    app = Flask(__name__)

    # Configurations
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "super-secret-key"  # replace with env var in production

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt = JWTManager(app)
    Migrate(app, db)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(notes_bp, url_prefix="/notes")

    # Root route
    @app.route("/")
    def index():
        return {"message": "Backend is running!"}

    # Register CLI command
    app.cli.add_command(seed)

    return app
