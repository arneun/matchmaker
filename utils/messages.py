


class Not_Finished_Error(Exception):
    def __init__(self, message):
        self.message = message

class Not_Playing_Error(Exception):
    def __init__(self, message):
        self.message = message
