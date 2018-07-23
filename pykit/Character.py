import Parameter
class Character(Parameter):
    """
    Object for IBM i Character.
    """
    def __init__(self, name, length, value):
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
        self.name = name
        self.payload = {"name":name}

    def get_payload(self):
        self.payload['type'] = str(self.length) + 'a'
        Parameter.get_payload(self);
        return self.payload
