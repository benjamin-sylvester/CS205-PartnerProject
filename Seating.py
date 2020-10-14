import Table as table
import Customer as customer
import Server as server

class Seating:

    def __init__(self, server , customer, table):
        self.server = server
        self.customer = customer
        self.table = table

    #Function will be called when there is...
    # A Customer waiting
    # A table that fits the party
    #There is a party/customer waiting 
