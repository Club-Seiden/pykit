import Parameter
class Float(Parameter):
    """
    Object for IBM i Float.
    """
    def __init__(self, name, length, precision, value):
        """
        How much error checking do we want here?
        Should we check that length is positive?
        Should we check if value matches length?
        Should we truncate the value to the length?

        :param length:
        :param precision:
        :param value:
        """
        self.length = length
        self.precision = precision
        self.value = value
        self.name = str(name)
        self.payload = {"name":self.name}

    def get_payload(self):
        self.payload['type'] = str(self.length) + 'f' + str(self.precision)
        Parameter.get_payload(self);
        return self.payload
