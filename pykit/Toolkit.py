class Toolkit:
    """
    Python Toolkit for interacting with the IBM i via different transports.
    """
    def __init__(self, connection):
        self.connection = connection
        self.payload = []

    def add(self, o):
        """
        Add an object to the payload that will be passed to the connection.

        :param o: Object to be added
        :return: void
        """
        if isinstance(o, dict):
            self.payload.append(o)
        else:
            raise TypeError('Only dictionaries are supported right now.')

    def execute(self):
        """
        Execute the transport's payload.

        :return: void
        """
        result = self.connection.execute(self.payload)
        self.payload = []
        return result
