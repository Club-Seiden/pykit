class Parameter:
    """
    Object for IBM i Parameters.
    """
    def __init__(self, name, value):
        """
        :param name:
        :param value:
        """
        self.value = value
        self.name = str(name)
        self.isReturn = False
        self.payload = {"name":self.name}
            
            
    def get_payload(self):
        self.payload['value'] = self.value
        if self.isReturn:
            self.payload['by'] = 'return'
        
        return self.payload