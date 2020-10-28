import Table
import Server
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
    servers = [server1, server2]

    table1 = Table(4, "W", True)
    table2 = Table(10, "B", True)
    table3 = Table(4, "N", True)
    tables = [table1, table2, table3]

    ourRestuarant = Restuarant(servers, tables)
    return ourRestuarant

def main():


    theRestuarant = initialize_restuarant()

    all_tables = theRestuarant.get_tables()

    customer_name, customer_size, location = welcome_menu()

    customer1 = Customer(customer_name, customer_size, location)

    table_found = False

    for table in all_tables:
        print("TABLE DATA: ", table.get_is_free(), table.get_location(), table.get_num_seats())
        print("CUSTOMER DATA: ", customer1.get_location_pref(), customer1.get_party_size())


        if table.get_is_free() and customer1.get_location_pref() == table.get_location() and table.get_num_seats() == customer1.get_party_size():
            print("FOUND")
            table_found = True
            #table.is_free = False

    if not table_found:
        print("Hold on we dont have anything available at this time")
        customer1.is_waiting = True

    else:
        customer1.is_seated = True
        print("The hostess will be seating you shortly")

main()

