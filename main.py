from Seating import Seating
from Table import Table
from Server import Server
from Restuarant import Restuarant
from Customer import Customer

def welcome_menu():
    print("Welcome to Ben and Jimmy's Shrimp Shack by the Sea")
    print("Please fill in the following information, and we will have you seated right away")
    party_name = input("What is the name of your party: ")
    party_size = int(input("How many people are in your party: "))
    location = input("Do you have a location preference ('W' for window, 'B' for bar, 'O' for outside, 'I' for inside, 'N' for no preference")
    print("Please wait while we check our availability ")

    return party_name, party_size, location

def initialize_restuarant():
    server1 = Server("Lisa", False)
    server2 = Server("Bob", False)
    server3 = Server("Joe", False)
    server4 = Server("Kate", False)
    server5 = Server("John", False)
    servers = [server1, server2, server3, server4, server5]

    table1 = Table(4, "W", True)
    table2 = Table(10, "B", True)
    table3 = Table(4, "N", True)
    table4 = Table(4, "N", True)
    table5 = Table(2, "W", True)
    table6 = Table(6, "N", True)
    table7 = Table(3, "O", True)
    table8 = Table(2, "N", True)
    table9 = Table(12, "O", True)
    table10 = Table(2, "N", True)

    tables = [table1, table2, table3, table4, table5, table6, table7, table8, table9, table10]

    ourRestuarant = Restuarant(servers, tables)
    return ourRestuarant

def check_availability(customer1, restuarant):
    all_tables = restuarant.get_tables()
    table_found = False

    for table in all_tables:

        if table.get_is_free() and customer1.get_location_pref() == table.get_location() and table.get_num_seats() == customer1.get_party_size():
            print("FOUND")
            table_found = True
            table.show_table_data()
            valid_table = table

    if not table_found:
        print("Hold on we dont have anything available at this time")
        customer1.is_waiting = True
        return False, None

    else:
        customer1.is_seated = True
        print("The hostess will be seating you shortly")
        return True, valid_table


def main():


    theRestuarant = initialize_restuarant()


    customer_name, customer_size, location = welcome_menu()

    customer1 = Customer(customer_name, customer_size, location)

    customer_seated, open_table = check_availability(customer1, theRestuarant)

    # if we have a table open, need to have a server seat the customer
    seated = False
    if customer_seated:
        for server in theRestuarant.get_servers():
            if not server.is_busy:
                print("Our server " + server.get_name() + " will be seating you shortly")
                seating = Seating(server, customer1, open_table)
                seating.seat()
                seating.show_seating()
                seated = True
                break
            if server.is_busy and not seated:
                print("Please continue waiting. We have no servers available to seat you at this moment. You should be seated briefly")

    





main()

