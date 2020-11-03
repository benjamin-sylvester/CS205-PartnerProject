from Server import Server
from Table import Table
from Customer import Customer

class Seating:

    def __init__(self, server , customer, table, location):
        self.server = server
        self.customer = customer
        self.table = table
        self.location = location


    def seat(self):
        self.server.seat_customer()
        self.customer.is_waiting = False
        self.customer.is_seated = True
        self.table.is_free = False

    def show_seating(self):
        outputString = "Customer: " + self.customer.get_party_name() + " has been seated by "
        outputString += self.server.get_name() + " at a " + str(self.table.get_num_seats()) + " person table"
        print(outputString)

    def get_location(self):
        return self.location

    def get_server_name(self):
        return self.server.get_name()


    def get_customer_name(self):
        return self.customer.get_party_name()

    def get_table(self):
        return self.table


    def set_server(self, server_obj):
        self.server = server_obj

    def set_table(self, table_obj):
        self.table = table_obj

    def set_customer(self, customer_obj):
        self.customer = customer_obj

    def set_location(self, location_str):
        self.location = location_str
