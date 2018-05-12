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
        self.payload.append(o)

    def execute(self):
        """
        Execute the transport's payload.

        :return: object
        """
        payload = []
        for p in self.payload:
            try:
                payload.append(p.get_payload())
            except AttributeError:
                """
                p does not have get_payload
                assume that the payload is raw json to be sent straight to the transport
                """
                payload = self.payload

        try:
            result = self.connection.execute(payload)
        except TypeError:
            print("The payload was not structured properly.")
            return {}

        self.payload = []
        return result
