from flask import jsonify
from datetime import datetime


def test_response(method='GET', data=None):
    return jsonify({
        'status': 200,
        'method': method,
        'data': data,
        'requested_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })


def to_response(data=''):
    return jsonify({
        'status': 200,
        'response': data,
    })
