#import pytest
import unittest

from Server import Server
from Table import Table
from Customer import Customer
from Restaurant import Restaurant
from Seating import Seating

class TestingClasses(unittest.TestCase):

    def setUp(self):
        self.server_obj = Server("Lisa", False)
        #create table object to test functionality
        self.table_obj = Table(6, "W", True)
        self.table_obj2 = Table(4, "N", True)
        #Create customer object ti test Functionality
        self.customer_obj = Customer("Jim", 6, "B", True, False, False)
        self.customer_obj2 = Customer("Joe", 4, "W", True, False, False)


        self.restaurant1 = Restaurant()
        self.restaurant2 = Restaurant()

        self.seating1 = Seating(self.server_obj, self.customer_obj, self.table_obj, 'W')
        self.seating2 = Seating(self.server_obj, self.customer_obj2, self.table_obj2, 'N')

    def tearDown(self) -> None:

        pass

    def test_seat_customer(self):
        self.server_obj.seat_customer()
        self.assertTrue(self.server_obj.get_is_busy())

    def test_is_busy(self):
        self.assertFalse(self.server_obj.get_is_busy())

    def test_get_name(self):
        self.assertTrue(self.server_obj.get_name() == "Lisa")
        self.assertFalse(self.server_obj.get_name() == "Joe")

    def test_set_name(self):
        self.server_obj.set_name("Ben")
        self.assertTrue(self.server_obj.get_name() == "Ben")
        self.assertFalse(self.server_obj.get_name() == "Jim")

    #-----------------------------------------------------------------------#

    #TABLE TESTING

    def test_get_num_seats(self):
        self.assertTrue(self.table_obj.get_num_seats() == 6)
        self.assertFalse(self.table_obj.get_num_seats() == 8)

    def test_get_is_free(self):
        self.assertTrue(self.table_obj.get_is_free())

    def test_get_location(self):
        self.assertTrue(self.table_obj.get_location() == "W")
        self.assertFalse(self.table_obj.get_location() == "N")

    def test_clear(self):
        self.table_obj.clear()
        self.assertTrue(self.table_obj.get_is_free())

    def test_set_num_seats(self):
        self.table_obj.set_num_seats(2)
        self.assertTrue(self.table_obj.get_num_seats() == 2)

    def test_set_location(self):
        self.table_obj.set_location("B")
        self.assertTrue(self.table_obj.get_location() == "B")
        self.assertFalse(self.table_obj.get_location() == "W")

    #def test_show_table_data(self):

    #--------------------------------------------------------------#
    #TEST CASES FOR CUSTOMER OBJ

    def test_get_party_name(self):
        self.assertTrue(self.customer_obj.get_party_name() == "Jim")
        self.assertFalse(self.customer_obj.get_party_name()== "Ben")

    def test_get_party_size(self):
        self.assertTrue(self.customer_obj.get_party_size() == 6)
        self.assertFalse(self.customer_obj.get_party_size() == 4)

    def test_get_location_pref(self):
        self.assertTrue(self.customer_obj.get_location_pref() == "B")
        self.assertFalse(self.customer_obj.get_location_pref() == "W")

    def test_get_is_waiting(self):
        self.assertTrue(self.customer_obj.get_is_waiting())

    def test_get_is_seated(self):
        self.assertFalse(self.customer_obj.get_is_seated())

    def test_get_is_finished(self):
        self.assertFalse(self.customer_obj.get_is_finsihed())

    #---------------------------------------------------------------------#
    # TESTING FUNCTIONALITY OF OPERATING RESTURANT
    def test_check_availability_is_avail(self):
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
        restaurant1 = Restaurant(servers, tables)
        self.assertTrue(restaurant1.check_availability(self.customer_obj))

    def test_check_availability_is_avail_bad(self):
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
        restaurant1 = Restaurant(servers, tables)
        self.assertTrue(restaurant1.check_availability_bad(self.customer_obj))

    def test_check_availability_is_not_avail(self):
        server1 = Server("Lisa", False)
        server2 = Server("Bob", False)
        server3 = Server("Joe", False)
        server4 = Server("Kate", False)
        server5 = Server("John", False)
        servers = [server1, server2, server3, server4, server5]
        table1 = Table(4, "W", False)
        table2 = Table(10, "B", False)
        table3 = Table(4, "N", False)
        table4 = Table(4, "N", False)
        table5 = Table(2, "W", False)
        table6 = Table(6, "N", False)
        table7 = Table(3, "O", False)
        table8 = Table(2, "N", False)
        table9 = Table(12, "O", False)
        table10 = Table(2, "N", False)
        tables = [table1, table2, table3, table4, table5, table6, table7, table8, table9, table10]
        restaurant2 = Restaurant(servers, tables)
        self.assertFalse(restaurant2.check_availability(self.customer_obj) == False , None)

    def test_finding_customer_is_seated(self):
        customer_found = False
        list_of_seatings = [self.seating1, self.seating2]
        seated_customers = [self.customer_obj, self.customer_obj2]
        if self.customer_obj in seated_customers:
            for seating in list_of_seatings:
                if seating.get_customer_name() == "Jim":
                    customer_found = True
        self.assertTrue(customer_found)


    def test_finding_customer_is_not_seated(self):
        customer_found = False
        list_of_seatings = [self.seating1, self.seating2]
        seated_customers = [self.customer_obj, self.customer_obj2]
        if self.customer_obj in seated_customers:
            for seating in list_of_seatings:
                if seating.get_customer_name() == "Jason":
                    customer_found = True
        self.assertFalse(customer_found)

    def test_customer_leaving(self):
        table = self.seating1.get_table()
        self.seating1.seat()
        self.seating1.clear()
        is_free = table.get_is_free()
        self.assertTrue(is_free)




if __name__ == '__main__':
    unittest.main()







    