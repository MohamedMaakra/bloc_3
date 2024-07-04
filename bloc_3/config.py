from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis .env
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    API_KEY = os.getenv('API_KEY')
    DEFAULT_ADMIN_EMAIL = os.getenv('default_admin_email')
    DEFAULT_ADMIN_PASSWORD = os.getenv('default_admin_password')

# Instancier la configuration
config = Config()
