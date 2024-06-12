from flask import Flask
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint
from app.controllers.libro_controller import libro_bp
from app.controllers.user_controller import user_bp
from app.database import db

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "tu_clave_secreta_aqui"
SWAGGER_URL = "/api/docs"
API_URL = "/static/swagger.json"
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Bliblioteca API"}
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)
#Configuracion de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///libro.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Inicializa la base de datos
db.init_app(app)
#Iniciaza la extension JWTManager
jwt = JWTManager(app)

#Registra el blueprint de libros y usuarios en la aplicaion
app.register_blueprint(libro_bp, url_prefix="/api")
app.register_blueprint(user_bp, url_prefix="/api")

#Crea las tablas si no existen
with app.app_context():
    #Crea las tablas
    db.create_all()

#Ejecuta la aplicacion
# Ejecuta la aplicación
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)