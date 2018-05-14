class Character:
    """
    Object for IBM i Character.
    """
    def __init__(self, length, value):
        """
        How much error checking do we want here?
        Should we check that length is positive?
        Should we check if value matches length?
        Should we truncate the value to the length?

        :param length:
        :param value:
        """
        self.length = length
        self.value = value
        self.payload = {"s":{"name":"char"}}

    def get_payload(self):
        self.payload['s']['type'] = str(self.length) + 'a'
        self.payload['s']['value'] = self.value
        return self.payload
