import pytest
import unittest

from Server import Server
from Table import Table



class TestSever(unittest.TestCase):

    def setUp(self):
        self.server_obj = Server("Lisa", False)

    def tearDown(self) -> None:

        pass

    def test_seat_customer(self):
        self.server_obj.seat_customer()
        assert (self.server_obj.get_is_busy() == True)

    def test_is_busy(self):
        assert (self.server_obj.get_is_busy() == False)

    def test_get_name(self):
        assert (self.server_obj.get_name() == "Lisa")

    