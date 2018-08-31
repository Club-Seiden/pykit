import requests
import json
from ...Toolkit import Toolkit
import ibm_db_dbi as dbi




class Db2Connection:
    """
    Represents a REST HTTP connection that can be used to get the Python
    Toolkit object.
    """

    def __init__(self, database, username, password):
        
        self.connection = dbi.connect(database=database, \
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
        payload_string = str(payload)
        
        cur = self.connection.cursor()
        cur.callproc('DB2JSON.DB2PROCJR', (payload_string,))
        
        result = cur.fetchone()
        
        """
        if not response.ok:
            raise TransportError("There was an error while executing the payload.")
        """
        return json.loads(result[0])

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
