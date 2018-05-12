import unittest
import os
from pykit.transport.http import connect
from pykit import Command


class TestCommand(unittest.TestCase):
    def setUp(self):
        self.connection = connect(
            os.environ['PK_DB2SOCK_URL'],
            db2sock_auth=(
                os.environ['PK_DB2SOCK_USER'], os.environ['PK_DB2SOCK_PASS']))

    def test_execute_qsh_command(self):
        cmd = Command("ls -1 /QOpenSys", True)
        toolkit = self.connection.toolkit()
        toolkit.add(cmd)
        response = toolkit.execute()
        self.assertTrue(response)

    def test_execute_rexx_command(self):
        cmd = Command("RTVJOBA CCSID(?N) USRLIBL(?) SYSLIBL(?)")
        toolkit = self.connection.toolkit()
        toolkit.add(cmd)
        response = toolkit.execute()
        self.assertTrue(response)

    def test_execute_exec_command(self):
        cmd = Command("CHGLIBL LIBL(DB2JSON QTEMP) CURLIB(DB2JSON)")
        toolkit = self.connection.toolkit()
        toolkit.add(cmd)
        response = toolkit.execute()
        self.assertTrue(response)


        self.assertTrue(response)
if __name__ == '__main__':
    unittest.main()
