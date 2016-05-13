import os
from urllib.parse import urlparse
from bottle import get, post, request, run, static_file, view
import pymysql.cursors


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
    name = request.forms.getunicode('name').strip()
    surname = request.forms.getunicode('surname').strip()
    yearfrom = request.forms.getunicode('yearfrom').strip()
    yearto = request.forms.getunicode('yearto').strip()
    tp = request.forms.getunicode('type').strip()

    sql = """
        SELECT DISTINCT
            ar_taut, onoma, epitheto, etos_gen
        FROM
            kalitexnis
    """
    if tp == 'singer':
        sql += ' CROSS JOIN singer_prod ON ar_taut = tragoudistis '
    elif tp == 'songwriter':
        sql += ' CROSS JOIN tragoudi ON ar_taut = stixourgos '
    elif tp == 'composer':
        sql += ' CROSS JOIN tragoudi ON ar_taut = sinthetis '

    args = []
    filters = []
    if name:
        args.append(name)
        filters.append('onoma = %s')
    if surname:
        args.append(surname)
        filters.append('epitheto = %s')
    if yearfrom:
        args.append(yearfrom)
        filters.append('etos_gen >= %s')
    if yearto:
        args.append(yearto)
        filters.append('etos_gen <= %s')

    if args:
        sql += ' WHERE ' + ' AND '.join(filters)

    cursor = db.cursor()
    cursor.execute(sql, args)
    results = cursor.fetchall()
    return {'results': results}


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
    url = urlparse(os.environ.get('DATABASE_URL'))
    db = pymysql.connect(host=url.hostname,
                         user=url.username,
                         password=url.password,
                         db=url.path[1:],
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)

    run(host='0.0.0.0', port=os.environ.get('PORT', 8080))
