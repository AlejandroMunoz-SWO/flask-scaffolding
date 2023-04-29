from flask import Flask
from flasgger import Swagger
from flask_jwt_extended import JWTManager
from envs.dev.dev_env import config, get_database_config
from database.db import init_app
from flask_cors import CORS

from users.routes.user_route import users_routes


app = Flask(__name__)

# Cors config
app.config['JSON_AS_ASCII'] = False
CORS(app)


# Swagger config
app.config['SWAGGER'] = {
    "swagger_version": "2.0",
    "info": {
        "title": "One Welfare API",
        "description": "API for One Welfare project",
        "version": "1.0"
    },
    "basePath": "/",
    "schemes": [
        "http",
    ]
}


# Database config
user = get_database_config().get('MYSQL_USER')
host = get_database_config().get('MYSQL_HOST')
password = get_database_config().get('MYSQL_PASSWORD')
database = get_database_config().get('DATABASE_NAME')
sql_track_modifications = get_database_config().get('SQLALCHEMY_TRACK_MODIFICATIONS')

# Database config: my database has password, so I have to use the last of these lines
# If you have a denied access to the database, uncomment the following line and comment the next one
# app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql+pymysql://{user}@{host}/{database}'
app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql+pymysql://{user}:{password}@{host}/{database}'

# JWT config
app.config['SECRET_KEY'] = config['SECRET_KEY']
jwt = JWTManager(app)

# Blueprints
app.register_blueprint(users_routes)

init_app(app)

# TEST DATABASE DEV ENVIRONMENT
print('User:', user)
print('Database:', database)
print('Server:', host)


# Main
if __name__ == '__main__':
    app.config.from_object(config['dev'])
    app.run()
