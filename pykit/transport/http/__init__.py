from .HttpConnection import *


def connect(db2sock_rest_url, db2sock_auth):
    return HttpConnection(db2sock_rest_url, db2sock_auth)
