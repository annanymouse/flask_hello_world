import os
class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://nitrous:nitrous@localhost:5432/mydate"
    DEBUG = True
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "")