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
    return {}


@get('/artists')
@get('/artists/search')
@view('artists/search')
def artist_search():
    name = request.query.getunicode('name', '').strip()
    surname = request.query.getunicode('surname', '').strip()
    yearfrom = request.query.getunicode('yearfrom', '').strip()
    yearto = request.query.getunicode('yearto', '').strip()
    tp = request.query.getunicode('type', '').strip()

    data = {}
    results = {}
    if request.query.dict:
        sql = """
            SELECT DISTINCT
                ar_taut AS id, onoma AS name, epitheto AS surname,
                etos_gen AS year
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
        data = {'name': name, 'surname': surname, 'yearfrom': yearfrom,
                'yearto': yearto}
        results = cursor.fetchall()

    return {'request': data, 'results': results}


@get('/artists/create')
@view('artists/create')
def artist_create():
    return {'results': {}}


@post('/artists/create')
@view('artists/create')
def artist_do_create():
    pid = request.forms.getunicode('id', '').strip()
    name = request.forms.getunicode('name', '').strip()
    surname = request.forms.getunicode('surname', '').strip()
    year = request.forms.getunicode('year', '').strip()

    success = False
    if pid:
        sql = """
            INSERT INTO
                kalitexnis
            SET
                ar_taut = %s, onoma = %s, epitheto = %s, etos_gen = %s
        """

        cursor = db.cursor()
        try:
            cursor.execute(sql, (pid, name, surname, year,))
            success = cursor.rowcount == 1
        except db.IntegrityError:
            pass

    return {'results': {'success': success, 'id': pid, 'name': name,
                        'surname': surname, 'year': year}}


@get('/artists/<pid>')
@view('artists/update')
def artist_update(pid):
    sql = """
        SELECT
            ar_taut AS id, onoma AS name, epitheto AS surname, etos_gen AS year
        FROM
            kalitexnis
        WHERE
            ar_taut = %s
    """

    cursor = db.cursor()
    cursor.execute(sql, (pid,))
    results = cursor.fetchone() or {}
    return {'results': results}


@post('/artists/<pid>')
@view('artists/update')
def artist_do_update(pid):
    name = request.forms.getunicode('name', '').strip()
    surname = request.forms.getunicode('surname', '').strip()
    year = request.forms.getunicode('year', '').strip()

    sql = """
        UPDATE
            kalitexnis
        SET
            onoma = %s, epitheto = %s, etos_gen = %s
        WHERE
            ar_taut = %s
    """

    cursor = db.cursor()
    cursor.execute(sql, (name, surname, year, pid,))
    success = cursor.rowcount == 1
    return {'results': {'success': success, 'id': pid, 'name': name,
                        'surname': surname, 'year': year}}


@get('/songs')
@get('/songs/search')
@view('songs/search')
def song_search():
    return {'request': {}, 'results': {}}


@post('/songs')
@post('/songs/search')
@view('songs/search')
def song_do_search():
    return {}


@get('/songs/create')
@view('songs/create')
def song_create():
    return {}


@post('/songs/create')
@view('songs/create')
def song_do_create():
    return {}


@get('/songs/<title>')
@view('songs/update')
def song_update(title):
    return {}


@post('/songs/<title>')
@view('songs/update')
def song_do_update(title):
    return {}


if __name__ == '__main__':
    url = urlparse(os.environ.get('DATABASE_URL'))
    db = pymysql.connect(host=url.hostname,
                         user=url.username,
                         password=url.password,
                         db=url.path[1:],
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor,
                         autocommit=True)

    run(host='0.0.0.0', port=os.environ.get('PORT', 8080))
