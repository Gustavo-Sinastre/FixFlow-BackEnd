from flask import Flask
from flask_cors import CORS
from config import Config
from routes.login.login import login
from routes.register.machines import registermachine
from routes.register.maintenances import registermaintenance

# Criação do aplicativo Flask
app = Flask(__name__)

# Configuração do CORS (permitindo requisições de qualquer origem)
CORS(app)

# Carregar as configurações do arquivo config.py
app.config.from_object(Config)

# Registrar os Blueprints para as rotas
# Login
app.register_blueprint(login)

# Registrar máquinas
app.register_blueprint(registermachine)

# Registrar manutenções
app.register_blueprint(registermaintenance)



if __name__ == "__main__":
    app.run(debug=True)