from Seating import Seating
from Table import Table
from Server import Server
from Restuarant import Restuarant
from Customer import Customer

def opening_menu():
    choices = [1,2,3,4,5]
    print("Welcome to Ben and Jimmy's Shrimp Shack by the Sea")
    choice = int(input("\nPlease select an option from the following list\n"
                   "Enter '1' to be seated\n"
                   "Enter '2' to order\n"
                   "Enter '3' to get the check\n"
                   "Enter '4' to leave the restaurant\n"
                   "Enter '5' to exit program\n"
                   "Enter your choice: "))

    while choice not in choices:
        print("Invalid input, please enter 1, 2, 3, 4 or 5")

    return choice

def seating_menu():

    print("Please fill in the following information, and we will have you seated right away")
    party_name = input("What is the name of your party: ")
    party_size = int(input("How many people are in your party: "))
    location = input("Do you have a location preference ('W' for window, 'B' for bar, 'O' for outside, 'I' for inside, 'N' for no preference): ")
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

        if table.get_is_free() and customer1.get_location_pref() == table.get_location() and table.get_num_seats() >= customer1.get_party_size():
            #print("FOUND")
            table_found = True
            #table.show_table_data()
            valid_table = table

    if not table_found:
        print("Hold on we dont have anything available at this time")
        customer1.is_waiting = True
        return False, None

    else:
        customer1.is_seated = True
        print("The hostess will be seating you shortly")
        return True, valid_table

def customer_leaves(restaurant, list_of_seatings):
    all_tables = restaurant.get_tables()
    for table in all_tables:
        for seating in list_of_seatings:
            if seating.get_table() == table:
                table.clear()

def main():
    seated_customers = []
    waiting_customers = []

    list_of_seatings = []
    theRestuarant = initialize_restuarant()

    choice = opening_menu()

    while choice != 5:
        # if customer wants to be seated
        if choice == 1:
            customer_name, customer_size, location = seating_menu()
            customer1 = Customer(customer_name, customer_size, location)

            customer_seated, open_table = check_availability(customer1, theRestuarant)

            # if we have a table open, need to have a server seat the customer
            seated = False
            if customer_seated:
                for server in theRestuarant.get_servers():
                    if not server.is_busy:
                        print("Our server " + server.get_name() + " is ready to seat you now")
                        seating = Seating(server, customer1, open_table, customer1.get_location_pref())
                        seating.seat()
                        seating.show_seating()
                        seated_customers.append(customer1.get_party_name())
                        list_of_seatings.append(seating)
                        seated = True
                        break
                    if server.is_busy and not seated:
                        print("Please continue waiting. We have no servers available to seat you at this moment. You should be seated briefly")

        if choice == 2:
            name_customer = input("What is the name of your party so we can send of your server: ")
            if name_customer in seated_customers:
                for seating in list_of_seatings:
                    print("SEATED CUSTOMER: " + seating.get_customer_name())
                    if seating.get_customer_name() == name_customer:
                        print("Your sever, " + seating.get_server_name() + " will be over to take your order soon. Thanks!")

        if choice == 3:
            name_customer = input("What is the name of your party so we can send of your server: ")
            if name_customer in seated_customers:
                for seating in list_of_seatings:
                    print("SEATED CUSTOMER: " + seating.get_customer_name())
                    if seating.get_customer_name() == name_customer:
                        print("Your sever, " + seating.get_server_name() + " will be over with your check shortly. Thanks!")
        if choice == 4:
            name_customer = input("What is the name of your party so we can send of your server: ")
            if name_customer in seated_customers:
                for seating in list_of_seatings:
                    print("SEATED CUSTOMER: " + seating.get_customer_name())
                    if seating.get_customer_name() == name_customer:
                        for table in theRestuarant.get_tables():
                            if table.get_location() == seating.get_location():
                                table.clear()
            else:
                print("You do not have a table at this time. Therefore, you're unable to leave :)")


        theRestuarant.show_tables()

        choice = opening_menu()



    





main()

