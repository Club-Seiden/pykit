class Parameter:
    def __init__(self, parameterType, direction='inout', byValue=False, isReturn=False):
        """
        :param name:
        :param value:
        """
        self.parameterType = parameterType
        self.direction = direction
        self.isReturn = isReturn
        self.byValue = False
        self.payload = {"name":self.name}
    
    def get_payload(self):
        self.payload = self.parameterType.get_payload()
        if self.isReturn:
            self.payload['by'] = 'return'    
        if self.byValue:
            self.payload['by'] = 'val'    
        
        return self.payload
    

class ParameterType:
    """
    Object for IBM i ParameterTypes.
    """
    def __init__(self, name, value):
        """
        :param name:
        :param value:
        """
        self.value = value
        self.name = str(name)
        self.payload = {"name":self.name}
            
            
    def get_payload(self):
        self.payload['value'] = self.value        
        return self.payload
    
class Float(ParameterType):
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
        :param precision:s
        :param value:
        """
        ParameterType.__init__(self, name, value)
        self.length = length
        self.precision = precision

    def get_payload(self):
        self.payload['type'] = str(self.length) + 'f' + str(self.precision)
        ParameterType.get_payload(self)
        return self.payload
    

class Integer(ParameterType):
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
        ParameterType.__init__(self, name, value)
        self.length = length
        self.signed = signed

    def get_payload(self):
        self.payload['type'] = str(self.length) + ('i' if self.signed else 'u') + '0'
        ParameterType.get_payload(self)
        
        return self.payload


class Character(ParameterType):
    """
    Object for IBM i Character.
    """
    def __init__(self, name, length, value, varying=''):
        """
        :param length:
        :param value:
        """
        ParameterType.__init__(self, name, value)
        self.length = length
        self.varying = varying

    def get_payload(self):
        self.payload['type'] = str(self.length) + 'a'
        if self.varying:
            self.payload['type'] = self.payload['type'] + 'v' + str(self.varying)
            
        ParameterType.get_payload(self)
        return self.payload


class Decimal(ParameterType):
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
        ParameterType.__init__(self, name, value)
        self.length = length
        self.signed = signed
        self.decimals = decimals

    def get_payload(self):
        self.payload['type'] = str(self.length) + ('s' if self.signed else 'p') + str(self.decimals)
        ParameterType.get_payload(self)
        
        return self.payload
    
    
class Binary(ParameterType):
    """
    Object for IBM i Binary.
    """
    def __init__(self, name, length, value):
        """
        
        :param length:
        :param value:
        """
        ParameterType.__init__(self, name, value)
        self.length = length

    def get_payload(self):
        self.payload['type'] = str(self.length) + 'b'
        ParameterType.get_payload(self)
        return self.payload    
    
    