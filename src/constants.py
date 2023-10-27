from dotenv import load_dotenv
import os

load_dotenv()


HOST = os.environ.get('HOST', default='0.0.0.0')
APP_PORT = int(os.environ.get('APP_PORT', default=8000))
MONGODB_USER = os.environ.get('MONGO_INITDB_ROOT_USERNAME', default='admin')
MONGODB_PASSWD = os.environ.get('MONGO_INITDB_ROOT_PASSWORD', default='admin')
MONGO_URI = f'mongodb://{MONGODB_USER}:{MONGODB_PASSWD}@key-value-db'
