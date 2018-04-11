import requests
from ...Toolkit import Toolkit


class HttpConnection:
    """
    Represents a REST HTTP connection that can be used to get the Python
    Toolkit object.
    """

    def __init__(self, db2sock_rest_url, db2sock_auth):
        self.db2sock_auth = db2sock_auth
        self.db2sock_rest_url = db2sock_rest_url
        self.payload = []
        self.__test_connection()

    def toolkit(self):
        """
        Return an instance of the toolkit with a connection defined.

        :return: Toolkit
        """
        return Toolkit(self)

    def add(self, o):
        """
        Add an object to the payload that will be passed to DB2Sock.

        :param o: Object to be added
        :return: void
        """
        if isinstance(o, dict):
            self.payload.append(o)
        else:
            raise TypeError('Only dictionaries are supported right now.')

    def execute(self):
        """
        Execute the payload and then clear the payload.

        :return: Response
        """
        response = requests.post(
            self.db2sock_rest_url, json=self.payload, auth=self.db2sock_auth)
        self.payload = []
        return response

    def __test_connection(self):
        """
        Test that the DB2Sock REST transport exists and works properly
        with the given configuration. Raise an error if not.

        :return: void
        """
        self.add({
            'pgm': [
                {'name': 'HELLO', 'lib': 'DB2JSON'},
                {'s': {'name': 'char', 'type': '128a', 'value': 'Hi there'}}
            ]
        })
        response = self.execute()
        if not response.ok:
            raise ConnectionError("DB2Sock REST Transport failed to connect.")
