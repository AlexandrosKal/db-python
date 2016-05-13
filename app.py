import os
from bottle import get, post, run, static_file, view


@get('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')


@get('/')
@view('index')
def index():
    return dict()


@get('/artists')
@view('artists/search')
def artist_search():
    return dict()


@get('/artists/create')
@view('artists/create')
def artist_create():
    return dict()


@post('/artists/create')
@view('artists/create')
def artist_do_create():
    return dict()


@post('/artists/list')
@view('artists/list')
def artist_list():
    return dict()


@get('/artists/<id:int>')
@view('artists/update')
def artist_update(id):
    return dict()


@post('/artists/<id:int>')
@view('artists/update')
def artist_do_update(id):
    return dict()


@get('/songs')
@view('songs/search')
def song_search():
    return dict()


@get('/songs/create')
@view('songs/create')
def song_create():
    return dict()


@post('/songs/create')
@view('songs/create')
def song_do_create():
    return dict()


@post('/songs/list')
@view('songs/list')
def song_list():
    return dict()


@get('/songs/<title>')
@view('songs/update')
def song_update(title):
    return dict()


@post('/songs/<title>')
@view('songs/update')
def song_do_update(title):
    return dict()


if __name__ == '__main__':
    run(host='0.0.0.0', port=os.environ.get('PORT', 8080))
