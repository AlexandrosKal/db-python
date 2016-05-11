import os
from bottle import route, run


@route('/')
def hello():
    return 'Hello, world!'


if __name__ == '__main__':
    run(port=os.environ['PORT'])
