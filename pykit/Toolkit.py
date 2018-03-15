class Toolkit:
    """
    Python Toolkit for interacting with the IBM i via different transports.
    """
    def __init__(self, connection):
        self.connection = connection
        self.payload = ''

    def add(self, o):
        """
        Add object to the transport's payload.

        :param o: Object to be added to the transport
        :return: void
        """
        self.connection.add(o)

    def execute(self):
        """
        Execute the transport's payload.

        :return: void
        """
        return self.connection.execute()
