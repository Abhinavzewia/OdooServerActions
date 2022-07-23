from .database_actions import *

def get_domain(domain):
    if isinstance(domain, str):
        return get_domain(domain.split(','))
    if isinstance(domain, list):
        main_domain = []
        for dom in domain:
            operation = [n for n in ["=", '!=', ' not in '] if dom.find(n) != -1]
            if not operation:
                raise ValueError("Given Domain is incorrect")
            temp_dom = dom.split(operation[0])
            main_domain.append((temp_dom[0], operation[0], temp_dom[1]))
        return main_domain


class DatabaseAction:

    def __init__(self, model, connection, ids=None):
        self.model = model
        self.connection = connection
        self.ids = [ids]
        self.id = self.ids[-1]
        self.create_record = create_record
        self.create_record_multi = create_record_multi
        self.update_record = update_record
        self.find_record = find_record
        self.unlink_record = unlink_record

    def create(self, vals):
        if not vals:
            raise UserWarning("Data for Record not Given!")
        if isinstance(vals, dict):
            return self.create_record(self, self.connection, vals)
        elif isinstance(vals, list):
            return self.create_record_multi(self, self.connection, vals)

    def update(self, vals):
        if not self.ids or not vals:
            raise UserWarning("Enter The id of the record and data to Update")
        return self.update_record(self, self.connection, vals)

    def find(self, domain, fields=False):
        self.domain = domain
        return self.find_record(self, self.connection, get_domain, fields)

    def unlink(self, vals):
        if not self.ids or not vals:
            raise UserWarning("Enter The id of the record and data to Update")
        return self.unlink_record(self, self.connection)

    def custom_function(self, function_name):
        pass
