import Table as table
class Server:

    def __init__(self, name, is_busy):
        self.name = name
        self.is_busy = is_busy


    #seats spceific customer in an available table
    #def seat_customer(Table t, Customer s):

    def seat_customer(self):
        self.is_busy = True

    def clear_table(self, table):
        table.clear()


    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name



