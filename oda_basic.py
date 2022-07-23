from .connect import *

class ConnectOdoo:

    def __init__(self, url, user_name, db, password):
        self.url = url
        self.user_name = user_name
        self.db = db
        self.password = password
        self.uid = None
        self.object = None
        self.connection = server_connect

    def connection(self):
        return self.connection(self)
