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
        self.byValue = False
        self.payload = {"name":self.name}
            
            
    def get_payload(self):
        self.payload['value'] = self.value
        if self.isReturn:
            self.payload['by'] = 'return'    
        if self.byValue:
            self.payload['by'] = 'val'    
        
        return self.payload
    
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
        self.isReturn = False
        self.payload = {"name":self.name}

    def get_payload(self):
        self.payload['type'] = str(self.length) + 'f' + str(self.precision)
        Parameter.get_payload(self);
        return self.payload
    

class Integer(Parameter):
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
        self.isReturn = False
        self.payload = {"name":self.name}

    def get_payload(self):
        self.payload['type'] = str(self.length) + ('i' if self.signed else 'u') + '0'
        Parameter.get_payload(self);
        
        return self.payload


class Character(Parameter):
    """
    Object for IBM i Character.
    """
    def __init__(self, name, length, value, varying=''):
        """
        :param length:
        :param value:
        """
        self.length = length
        self.value = value
        self.name = name
        self.isReturn = False
        self.varying = varying
        self.payload = {"name":name}

    def get_payload(self):
        self.payload['type'] = str(self.length) + 'a'
        if (self.varying > ''):
            self.payload['type'] = self.payload['type'] + varying + 'v'
            
        Parameter.get_payload(self);
        return self.payload


class Decimal(Parameter):
    """
    Object for IBM i Decimal.
    """
    def __init__(self, name, length, decimals, value, signed=False):
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
        self.decimals = decimals
        self.isReturn = False
        self.payload = {"name":self.name}

    def get_payload(self):
        self.payload['type'] = str(self.length) + ('s' if self.signed else 'p') + str(self.decimals)
        Parameter.get_payload(self);
        
        return self.payload
    
    
class Binary(Parameter):
    """
    Object for IBM i Binary.
    """
    def __init__(self, name, length, value):
        """
        
        :param length:
        :param value:
        """
        self.length = length
        self.value = value
        self.name = name
        self.isReturn = False
        self.payload = {"name":name}

    def get_payload(self):
        self.payload['type'] = str(self.length) + 'b'
        Parameter.get_payload(self);
        return self.payload    
    
    