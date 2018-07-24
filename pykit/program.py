class Program:
    """
    Object for calling an IBM i Program.
    """
    def __init__(self, name, library=''):
        self.name = name
        self.library = library
        self.parameters = []
        self.payload = {
            "pgm": [{"name": name, "lib": library}]
        }

    def add_parameter(self, parameter):
        """

        :param parameter: Parameter to be added
        :return:
        """
        self.parameters.append(parameter)

    def add_parameter_by_value(self, parameter):
        """

        :param parameter: Parameter to be added
        :return:
        """
        parameter.byValue = True
        self.parameters.append(parameter)


    def get_payload(self):
        if len(self.parameters) is 1:
            self.payload["pgm"].append({"s": self.parameters[0].get_payload()})
        else:
            self.payload["pgm"].append({"s":[]})
            for p in self.parameters:
                self.payload["pgm"][-1]["s"].append(p.get_payload())

        return self.payload


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
        
    