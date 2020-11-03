class Server:

    def __init__(self, name, is_busy):
        self.name = name
        self.is_busy = is_busy


    def seat_customer(self):
        self.is_busy = True

    def clear_table(self, table):
        table.clear()

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_is_busy(self):
        return self.is_busy

