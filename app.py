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
            args.append(name + '%')
            filters.append('onoma LIKE %s')
        if surname:
            args.append(surname + '%')
            filters.append('epitheto LIKE %s')
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
    title = request.query.getunicode('title', '').strip()
    year = request.query.getunicode('year', '').strip()
    company = request.query.getunicode('company', '').strip()

    data = {}
    results = {}
    if request.query.dict:
        sql = """
            SELECT DISTINCT
                title, etaireia AS company, etos_par AS year
            FROM
                cd_production CROSS JOIN singer_prod ON code_cd = cd
                              CROSS JOIN tragoudi ON title = titlos
        """
        args = []
        filters = []
        if title:
            args.append(title + '%')
            filters.append('title LIKE %s')
        if year:
            args.append(year)
            filters.append('etos_par = %s')
        if company:
            args.append(company + '%')
            filters.append('etaireia LIKE %s')

        if args:
            sql += ' WHERE ' + ' AND '.join(filters)

        cursor = db.cursor()
        cursor.execute(sql, args)
        results = cursor.fetchall()
        data = {'title': title, 'year': year, 'company': company}

    return {'request': data, 'results': results}


@get('/songs/create')
@view('songs/create')
def song_create():
    cursor = db.cursor()
    cursor.execute("""
        SELECT
            cd
        FROM
            singer_prod
    """)
    cds = cursor.fetchall()

    cursor.execute("""
        SELECT
            ar_taut AS id
        FROM
            kalitexnis
    """)
    artists = cursor.fetchall()

    return {'results': {'cds': cds, 'artists': artists}}


@post('/songs/create')
@view('songs/create')
def song_do_create():
    title = request.forms.getunicode('title', '').strip()
    year = request.forms.getunicode('year', '').strip()
    cd = request.forms.getunicode('cd', '').strip()
    singer = request.forms.getunicode('singer', '').strip()
    songwriter = request.forms.getunicode('songwriter', '').strip()
    composer = request.forms.getunicode('composer', '').strip()

    cursor = db.cursor()
    cursor.execute("""
        SELECT
            cd
        FROM
            singer_prod
    """)
    cds = cursor.fetchall()

    cursor.execute("""
        SELECT
            ar_taut AS id
        FROM
            kalitexnis
    """)
    artists = cursor.fetchall()

    success = False
    if title:
        sql = """
            INSERT INTO
                tragoudi
            SET
                titlos = %s, sinthetis = %s, etos_par = %s, stixourgos = %s
        """

        try:
            cursor.execute(sql, (title, composer, year, songwriter,))
        except db.IntegrityError:
            pass

        sql = """
            INSERT INTO
                singer_prod
            SET
                cd = %s, tragoudistis = %s, title = %s
        """

        try:
            cursor.execute(sql, (cd, singer, title,))
            success = cursor.rowcount == 1
        except db.IntegrityError:
            pass

    return {'results': {'cds': cds, 'artists': artists, 'success': success}}


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
