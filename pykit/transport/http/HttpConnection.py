import requests


class HttpConnection:
    """
    Represents a REST HTTP connection that can be used to get the Python Toolkit object.
    """

    def __init__(self, db2sock_rest_url, db2sock_auth):
        """
        Test that the DB2Sock connection exists
        """
        self.db2sock_auth = db2sock_auth
        self.db2sock_rest_url = db2sock_rest_url

        payload = {
            'pgm': [{'name': 'HELLO', 'lib': 'DB2JSON'}, {'s': {'name': 'char', 'type': '128a', 'value': 'Hi there'}}]}

        response = requests.post(self.db2sock_rest_url, json=payload, auth=self.db2sock_auth)

        if not response.ok:
            raise ConnectionError("DB2Sock REST Transport failed to connect.")
