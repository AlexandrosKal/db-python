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
    return {'request': {}, 'results': {}}


@post('/artists')
@post('/artists/search')
@view('artists/search')
def artist_do_search():
    name = request.forms.getunicode('name', '').strip()
    surname = request.forms.getunicode('surname', '').strip()
    yearfrom = request.forms.getunicode('yearfrom', '').strip()
    yearto = request.forms.getunicode('yearto', '').strip()
    tp = request.forms.getunicode('type', '').strip()

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
    return {'request': {'name': name, 'surname': surname, 'yearfrom': yearfrom,
                        'yearto': yearto, 'type': tp}, 'results': results}


@get('/artists/create')
@view('artists/create')
def artist_create():
    return {}


@post('/artists/create')
@view('artists/create')
def artist_do_create():
    return {}


@get('/artists/<pid>')
@view('artists/update')
def artist_update(pid):
    sql = """
        SELECT
            ar_taut, onoma, epitheto, etos_gen
        FROM
            kalitexnis
        WHERE
            ar_taut = %s
    """

    cursor = db.cursor()
    cursor.execute(sql, (pid,))
    results = cursor.fetchall()
    return {'request': {}, 'results': results}


@post('/artists/<pid>')
@view('artists/update')
def artist_do_update(pid):
    name = request.forms.getunicode('name').strip()
    surname = request.forms.getunicode('surname').strip()
    year = request.forms.getunicode('year').strip()

    if name or surname or year:
        sql = """
            UPDATE
                kalitexnis
            SET
                onoma = %s, epitheto = %s, etos_gen = %s
            WHERE
                ar_taut = "%s"

        """
        print(name, surname, year, pid)
        print(sql)
        cursor = db.cursor()
        cursor.execute(sql, (name, surname, year, pid, ))
        results = cursor.fetchall()
        return {'results': results}
    return dict()


@get('/songs')
@view('songs/search')
def song_search():
    return {'request': {}, 'results': {}}


@post('/songs/search')
@view('songs/search')
def song_do_search():
    title = request.forms.getunicode('title').strip()
    year = request.forms.getunicode('year').strip()
    company = request.forms.getunicode('company').strip()
    sql = """
        SELECT
            title, etos_par, cd, tragoudistis, stixourgos, sinthetis
        FROM
           tragoudi CROSS JOIN singer_prod ON title = titlos
                    CROSS JOIN cd_production ON cd = code_cd
    """
    args = []
    filters = []
    if title:
        args.append(title)
        filters.append('title = %s')
    if year:
        args.append(year)
        filters.append(' etos_par = %s')
    if company:
        args.append(company)
        filters.append('etaireia = %s')

    if args:
        sql += ' WHERE ' + ' AND '.join(filters)

    cursor = db.cursor()
    cursor.execute(sql, args)
    results = cursor.fetchall()
    print(sql)
    print(results)
    return {'request': {'title': title, 'year': year, 'company': company},
            'results': results}


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
                         cursorclass=pymysql.cursors.DictCursor)

    run(host='0.0.0.0', port=os.environ.get('PORT', 8080), debug=True,
        reloader=True)
