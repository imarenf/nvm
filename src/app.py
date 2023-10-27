from flask import Flask, request
from pymongo import MongoClient

from constants import *

app = Flask(__name__)

client = MongoClient(MONGO_URI)
db = client.kv_db
values = db.values


def validate(kv):
    return {'key': kv['key'], 'value': kv['value']}


@app.route('/api/v1/', methods=['GET', 'POST'])
def post_router():
    if request.method == 'GET':
        return [validate(kv) for kv in values.find()]
    data = request.get_json()
    key = data.get('key')
    value = data.get('value')
    values.insert_one({'key': key, 'value': value})
    return {'Status': 200}


@app.route('/api/v1/<string:key>/', methods=['GET', 'PUT'])
def get_put_router(key):
    kv = values.find_one({'key': key})
    if not kv:
        return {'Status': 404, 'Error': 'Key not found'}
    if request.method == 'GET':
        return validate(kv)
    data = request.get_json()
    new_value = data.get('value')
    values.update_one({'key': key}, {'$set': {'value': new_value}})
    return {'Status': 200}
