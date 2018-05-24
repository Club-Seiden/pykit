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

    def addParameter(self, parameter):
        """

        :param parameter: Parameter to be added
        :return:
        """
        self.parameters.append(parameter)

    def get_payload(self):
        for p in self.parameters:
            self.payload["pgm"].append(p.get_payload())

        return self.payload
