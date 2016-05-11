import os
from bottle import get, post, run, static_file, view


@get('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')


@get('/')
@view('index')
def index():
    return 'Hello, world!'


@get('/artists')
@view('artists/search')
def artist_search():
    return ''


@get('/artists/create')
@view('artists/create')
def artist_create():
    return ''


@post('/artists/create')
@view('artists/create')
def artist_do_create():
    return ''


@get('/artists/list')
@view('artists/list')
def artist_list():
    return ''


@get('/artists/<id:int>')
@view('artists/update')
def artist_update(id):
    return ''


@post('/artists/<id:int>')
@view('artists/update')
def artist_do_update(id):
    return ''


@get('/songs')
@view('songs/search')
def song_search():
    return ''


@get('/songs/create')
@view('songs/create')
def song_create():
    return ''


@post('/songs/create')
@view('songs/create')
def song_do_create():
    return ''


@get('/songs/list')
@view('songs/list')
def song_list():
    return ''


if __name__ == '__main__':
    run(host='0.0.0.0', port=os.environ.get('PORT', 8080))
