import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1/codigo_18_backend'
    SQLALCHEMY_TRACK_MODIFICATIONS = True