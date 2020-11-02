from Server import Server
from Table import Table
from Customer import Customer

class Seating:

    def __init__(self, server , customer, table):
        self.server = server
        self.customer = customer
        self.table = table


    def seat(self):
        self.server.seat_customer()
        self.customer.is_waiting = False
        self.customer.is_seated = True
        self.table.is_free = False

    def show_seating(self):
        outputString = "Customer: " + self.customer.get_party_name() + " has been seated by "
        outputString += self.server.get_name() + " at a " + str(self.table.get_num_seats()) + " person table"
        print(outputString)

    #Function will be called when there is...
    # A Customer waiting
    # A table that fits the party
    #There is a party/customer waiting
