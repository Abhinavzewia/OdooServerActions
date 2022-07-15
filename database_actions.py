
def create_record(self, connection, vals):
    pass

def create_record_multi(self, connection, vals):
    for val in vals:
        create_record(self, connection, val)

def update_record(self, connection, vals):
    pass

def find_record(self, domain):
    pass