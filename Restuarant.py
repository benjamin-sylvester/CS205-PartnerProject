class Restuarant:

    def __init__(self, servers, tables):
        self.servers = servers
        self.tables = tables


    def get_tables(self):
        return self.tables

    def get_servers(self):
        return self.servers

    def free_table(self, table_in):
        for table in self.tables:
            if table == table_in:
                table.clear()


    def show_tables(self):
        for table in self.tables:
            print("TABLE DATA:\nNumber of Seats: " + str(table.get_num_seats()) + "\nLocation: " + table.get_location()
                  + "\nIs free: " + str(table.get_is_free()))
