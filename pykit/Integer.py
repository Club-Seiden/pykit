class Integer:
    """
    Object for IBM i Integer.
    """
    def __init__(self, name, length, value, signed=True):
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
        self.name = str(name)
        self.signed = signed
        self.payload = {"name":self.name}

    def get_payload(self):
        self.payload['type'] = str(self.length) + ('i' if self.signed else 'u') + '0'
        self.payload['value'] = self.value
        return self.payload
