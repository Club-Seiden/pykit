from .Db2Connection import Db2Connection


def connect(database, username, password):
    return Db2Connection(database, username, password)
