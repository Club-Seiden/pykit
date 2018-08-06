from .Db2Connection import Db2Connection


def connect(database='*LOCAL', username=None, password=None):
    return Db2Connection(database, username, password)
