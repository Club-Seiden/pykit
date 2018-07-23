import Program

class ServiceProgram(Program):
    """
    Object for calling an IBM i Program.
    """
    def __init__(self, name, library='', function=''):
        self.name = name
        self.library = library
        self.parameters = []
        self.payload = {
            "pgm": [{"name": name, "lib": library, "func": function}]
        }

    def add_return(self, parameter):
        """

        :param parameter: Return parameter to be added
        :return:
        """
        parameter.isReturn = True
        self.parameters.append(parameter)
        
    