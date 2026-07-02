import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = 'moon-sql-server-2026.database.windows.net'
    SQL_DATABASE = 'database-west'
    SQL_USER_NAME = 'YOUR_SQL_ADMIN_USERNAME'
    SQL_PASSWORD = 'Guruji@123'

    SQLALCHEMY_DATABASE_URI = (
        'mssql+pyodbc://'
        + SQL_USER_NAME
        + '@'
        + SQL_SERVER
        + ':'
        + SQL_PASSWORD
        + '@'
        + SQL_SERVER
        + ':1433/'
        + SQL_DATABASE
        + '?driver=ODBC+Driver+18+for+SQL+Server'
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = 'moonstorage2026'
    BLOB_STORAGE_KEY = 'nbX6Rxcy1d1lI3sk6XuQBOFs3n8iv+U9ontW1vAgJ/Z9ewJkZbrev6KbFVDxnwJscCoKqrXORO3H+AStrGxMng=='
    BLOB_CONTAINER = 'images'
