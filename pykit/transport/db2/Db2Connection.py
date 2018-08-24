import requests
from ...Toolkit import Toolkit
import ibm_db_dbi as dbi
import ibm_db as db2




class Db2Connection:
    """
    Represents a REST HTTP connection that can be used to get the Python
    Toolkit object.
    """

    def __init__(self, database, username, password):
        
        self.connection = dbi.connect(database=database, \
                       user=username, password=password)
        self.connection_two = db2.connect('*LOCAL', 'alan', 'wiscon1')
        
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
        print(payload_string)
        payload_string = """
        {
            'pgm': [
                {'name': 'HELLO', 'lib': 'DB2JSON'},
                {'s': {'name': 'char', 'type': '128a', 'value': 'Hi there'}}
            ]
        }  
        """
        
        cur = self.connection.cursor()
        sql = "call DB2JSON.DB2PROCJ(?)"
        cur.callproc('DB2JSON.DB2PROCJ', (payload_string,))
        stmt = db2.prepare(self.connection_two, sql)
        db2.bind_param(stmt, 1, payload_string)
        db2.execute(stmt)
        result = db2.fetch_tuple(stmt)
        print(result[0])
        #print(db2.result(stmt, 0))
        
        
        
        
        
        result = cur.fetchone()
        #cur.execute("call DB2JSON.DB2PROCJ(?)", (str(payload),))
        #result = cur.fetchall()
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
