from xmlrpc import client

def server_connect(self):
    try:
        connection = client.ServerProxy("%s/xmlrpc/2/common" % self.url)
        self.uid = connection.authenticate(self.db, self.user_name, self.password, {})
        self.object = client.ServerProxy("%s/xmlrpc/2/object" % self.url)
    except Exception as e:
        raise Warning("Error %s Occurred" % e)
    return True
