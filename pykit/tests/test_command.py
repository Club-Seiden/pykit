import unittest
import os
from pykit.transport.http import connect
from pykit import ClCommand


class TestClCommand(unittest.TestCase):
    def setUp(self):
        self.connection = connect(
            os.environ['PK_DB2SOCK_URL'],
            db2sock_auth=(
                os.environ['PK_DB2SOCK_USER'], os.environ['PK_DB2SOCK_PASS']))

    def test_execute_qsh_command(self):
        cmd = ClCommand("wrkactjob", True)
        toolkit = self.connection.toolkit()
        toolkit.add(cmd)
        response = toolkit.execute()
        self.assertTrue(response)

    def test_execute_rexx_command(self):
        cmd = ClCommand("RTVJOBA CCSID(?N) USRLIBL(?) SYSLIBL(?)")
        toolkit = self.connection.toolkit()
        toolkit.add(cmd)
        response = toolkit.execute()
        self.assertTrue(response)

    def test_execute_exec_command(self):
        cmd = ClCommand("CHGLIBL LIBL(DB2JSON QTEMP) CURLIB(DB2JSON)")
        toolkit = self.connection.toolkit()
        toolkit.add(cmd)
        response = toolkit.execute()
        self.assertTrue(response)


        self.assertTrue(response)
if __name__ == '__main__':
    unittest.main()
