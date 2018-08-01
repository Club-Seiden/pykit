import requests
from ...Toolkit import Toolkit


class Db2Connection:
    """
    Represents a REST HTTP connection that can be used to get the Python
    Toolkit object.
    """

    def __init__(self, db2sock_database, db2sock_auth):
        self.db2sock_auth = db2sock_auth
        self.db2sock_database = db2sock_database
        self.__test_connection()

    def toolkit(self):
        """
        Return an instance of the toolkit with a connection defined.

        :return: Toolkit
        """
        return Toolkit(self)

    def execute(self, payload):
        """
        Execute the payload and then clear the payload.

        :return: dict
        """
        response = requests.post(
            self.db2sock_rest_url, json=payload, auth=self.db2sock_auth)
        if not response.ok:
            raise TransportError("There was an error while executing the payload.")

        return response.json()

    def __test_connection(self):
        """
        Test that the DB2Sock REST transport exists and works properly
        with the given configuration. Raise an error if not.

        :return: void
        """
        toolkit = self.toolkit()
        toolkit.add({
            'pgm': [
                {'name': 'HELLO', 'lib': 'DB2JSON'},
                {'s': {'name': 'char', 'type': '128a', 'value': 'Hi there'}}
            ]
        })
        response = toolkit.execute()
