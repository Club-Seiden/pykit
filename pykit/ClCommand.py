class ClCommand:
    """
    Object for calling an IBM i CL command.
    """
    def __init__(self, command, screen_output=False):
        self.command = command
        self.screen_output = screen_output
        self.payload = {
            "cmd": {}
        }

    def get_payload(self):
        if self.screen_output:
            self.payload["cmd"]["qsh"] = self.command
        elif any(x in self.command for x in ["&", "?"]):
            self.payload["cmd"]["rexx"] = self.command
        else:
            self.payload["cmd"]["exec"] = self.command

        return self.payload
