from Table import Table
from Server import Server
class Restaurant:

    def __init__(self, servers=None, tables=None):
        if servers is None:
            server1 = Server("Lisa", False)
            server2 = Server("Bob", False)
            server3 = Server("Joe", False)
            server4 = Server("Kate", False)
            server5 = Server("John", False)
            servers = [server1, server2, server3, server4, server5]
            self.servers = servers
        else:
            self.servers = servers
        if tables is None:
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
            self.tables = [table1, table2, table3, table4, table5, table6, table7, table8, table9, table10]
        else:
            self.tables = tables

    def get_tables(self):
        return self.tables

    def get_servers(self):
        return self.servers

    # def free_table(self, table_in):
    #     for table in self.tables:
    #         if table == table_in:
    #             table.clear()

    def check_availability(self, customer1):
        all_tables = self.get_tables()
        table_found = False

        for table in all_tables:

            if table.get_is_free() and customer1.get_location_pref() == table.get_location() and table.get_num_seats() >= customer1.get_party_size():
                table_found = True
                valid_table = table

        if not table_found:
            #print("Hold on we dont have anything available at this time")
            customer1.is_waiting = True
            return False, None

        else:
            customer1.is_seated = True
            #print("The hostess will be seating you shortly")
            return True, valid_table

    def show_tables(self):

        for table in self.tables:
            print("TABLE DATA:\nNumber of Seats: " + str(table.get_num_seats()) + "\nLocation: " + table.get_location()
                  + "\nIs free: " + str(table.get_is_free()))






