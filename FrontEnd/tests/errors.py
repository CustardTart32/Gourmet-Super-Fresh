class OrderError(Exception):

    def __init__(self,msg):
        self.msg = msg

    def get_message(self):
    	return self.msg

class InvalidID(Exception):

    def __init__(self, msg):
        self.msg = msg

    def get_message(self):
    	return self.msg