import os

class Config:
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', 'False') == 'True'
    FLASK_ENV = os.getenv('FLASK_ENV', 'Production')  
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://api_full_user:SsRzf8WjXTmyff2a2EPSQ8e7THnrctFf@dpg-cs5u5i2j1k6c739u9t70-a/api_full')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
