import os
from bottle import route, run


@route('/')
def hello():
    return 'Hello, world!'


if __name__ == '__main__':
    run(host='0.0.0.0', port=os.environ.get('PORT', 8080))
