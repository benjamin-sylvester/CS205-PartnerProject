class Table:


    def __init__(self, num_seats, location, is_free):
        self.num_seats = num_seats
        self.location = location
        self.is_free = is_free


    def get_is_free(self):
        return self.is_free

    def get_num_seats(self):
        return self.num_seats

    def get_location(self):
        return self.location

    def clear(self):
        self.is_free = True

    def set_num_seats(self, number_seats):
        self.num_seats = number_seats

    def set_location(self, new_location):
        self.location = new_location

    def show_table_data(self):
        outString = "Table data:\nNumber of Seats: " + str(self.get_num_seats()) + "\nLocation: " + self.get_location() + "\nIs free: " + str(self.get_is_free())
        print(outString)