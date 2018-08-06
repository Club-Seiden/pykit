import requests
from ...Toolkit import Toolkit
import ibm_db_dbi as dbi




class Db2Connection:
    """
    Represents a REST HTTP connection that can be used to get the Python
    Toolkit object.
    """

    def __init__(self, database='*LOCAL', username=None, password=None):
        
        self.connection = dbi.connect(dsn=None, database=database, \
                       user=username, password=password)
        
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
        cur = self.connection.cursor()

        cur.execute("call DB2JSON.DB2PROCJ(?)", (payload))
        result = cur.fetchall()
        """
        if not response.ok:
            raise TransportError("There was an error while executing the payload.")
        """
        return result.json()

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
