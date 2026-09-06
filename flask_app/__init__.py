from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_app.config import Config


db_ = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()




def create_app(config_class=Config):
    app_ = Flask(__name__)
    app_.config.from_object(Config)

    db_.init_app(app_)
    bcrypt.init_app(app_)
    login_manager.init_app(app_)
    mail.init_app(app_)

    from flask_app.users.routes import users
    from flask_app.posts.routes import posts
    from flask_app.main.routes import main
    from flask_app.errors.handlers import errors

    app_.register_blueprint(users)
    app_.register_blueprint(posts)
    app_.register_blueprint(main)
    app_.register_blueprint(errors)

    return app_




