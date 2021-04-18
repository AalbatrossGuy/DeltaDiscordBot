from os.path import isfile
from sqlite3 import connect

db_path = "./Data/db/database.db"

buildpath = "./Data/db/build.sql"

connectdb = connect(db_path, check_same_thread=False)

cursor = connectdb.cursor()


def with_commit(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        commit()

    return inner


@with_commit
def build():
    if isfile(buildpath):
        scriptexec(buildpath)


def commit():
    connectdb.commit()


def closedb():
    connectdb.close()


def field(command, *values):
    cursor.execute(command, tuple(values))
    if (fetch := cursor.fetchone()) is not None:
        return fetch[0]


def record(command, *values):
    cursor.execute(command, tuple(values))

    return cursor.fetchone()


def records(command, *values):
    cursor.execute(command, tuple(values))

    return cursor.fetchall()


def column(command, *values):
    cursor.execute(command, tuple(values))
    return [item[0] for item in cursor.fetchall()]


def execute(command, *values):
    cursor.execute(command, tuple(values))


def multiexec(command, value_s):
    cursor.executemany(command, value_s)


def scriptexec(path):
    with open(path, "r", encoding="utf-8") as file:
        cursor.executescript(file.read())
