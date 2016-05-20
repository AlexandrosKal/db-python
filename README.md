# Design and Applications of Databases - [Python assignment](docs/Assignment.pdf)

## Requirements

- [MariaDB](https://mariadb.org/) >= 5.1 or [MySQL](https://www.mysql.com/) >=
  4.1
- [Python](https://www.python.org/) >= 2.6

## Installation

### Environment

```sh
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
```

### Database

```sh
mysql -u user -p -h host -P port
```

```sql
CREATE DATABASE database;
USE database;
source etc/dump.sql;
```

## Configuration

```sh
echo "DATABASE_URL='mysql://user:password@host/database'" >> .env
```

## Execution

```sh
./app.py
```

### Development

Change the `run()` call in `app.py` to:

```python
run(host='0.0.0.0', port=os.environ.get('PORT', 8080), debug=True,
    reloader=True)
```

## Authors

- Alexandros Kalimeris <kalimerisalx@gmail.com> <sdi1400056@di.uoa.gr>
- Mario Saldinger <mariosaldinger@gmail.com> <sdi1400177@di.uoa.gr>
