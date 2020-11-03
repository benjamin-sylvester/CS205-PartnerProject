#import pytest
import unittest

from Server import Server
from Table import Table
from Customer import Customer



class TestSever(unittest.TestCase):

    def setUp(self):
        self.server_obj = Server("Lisa", False)
        #create table object to test functionality
        self.table_obj = Table(6, "W", False)
        #Create customer object ti test Functionality
        self.customer_obj = Customer("Jim", 6, "B", True, False, False)

    def tearDown(self) -> None:

        pass

    def test_seat_customer(self):
        self.server_obj.seat_customer()
        self.assertTrue(self.server_obj.get_is_busy() == True)

    def test_is_busy(self):
        self.assertTrue(self.server_obj.get_is_busy() == False)

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
        self.assertTrue(self.table_obj.get_is_free() == False)
        self.assertFalse(self.table_obj.get_is_free()== True)

    def test_get_location(self):
        self.assertTrue(self.table_obj.get_location() == "W")
        self.assertFalse(self.table_obj.get_location() == "N")

    def test_clear(self):
        self.table_obj.clear()
        self.assertTrue(self.table_obj.get_is_free() == True)

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
        self.assertTrue(self.customer_obj.get_is_waiting() == True)
        self.assertFalse(self.customer_obj.get_is_waiting() == False)

    def test_get_is_seated(self):
        self.assertTrue(self.customer_obj.get_is_seated() == False)
        self.assertFalse(self.customer_obj.get_is_seated() == True)

    def test_get_is_finished(self):
        self.assertTrue(self.customer_obj.get_is_finsihed() == False)
        self.assertFalse(self.customer_obj.get_is_finsihed() == True)

    #---------------------------------------------------------------------#

    








    