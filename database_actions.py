
def create_record(self, connection, vals):
    try:
        create_id = connection.object.execute_kw(connection.db, connection.uid, connection.password, self.model, 'create', [vals])
    except Exception as e:
        print("%s Error Occurred while Creating %s a Record" % (e, self.model))
        return False
    if create_id:
        self.ids.append(create_id)
        return create_id

def create_record_multi(self, connection, vals):
    for val in vals:
        create_record(self, connection, val)

def update_record(self, connection, vals):
    try:
        update_result = connection.object.execute_kw(connection.db, connection.uid, connection.password,
                                                     self.model, 'write', [self.id, vals])
    except Exception as e:
        print("%s Error Occurred while Writing %s a Record" % (e, self.model))
        return False
    return update_result

def find_record(self, connection, domain, fields):
    search_values = [domain] if not fields else [domain, fields]
    try:
        update_result = connection.object.execute_kw(connection.db, connection.uid, connection.password,
                                                     self.model, 'search_read', search_values)
    except Exception as e:
        print("%s Error Occurred while Searching a Record in %s" % (e, self.model))
        return False
    return update_result

def unlink_record(self, connection):
    try:
        unlink_result = connection.object.execute_kw(connection.db, connection.uid, connection.password,
                                                     self.model, 'unlink', [self.id])
    except Exception as e:
        print("%s Error Occurred while Deleting a Record in %s" % (e, self.model))
        return False
    return unlink_result