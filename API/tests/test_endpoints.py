"""
This file holds the tests for endpoints.py.
"""

from unittest import TestCase, skip
import API.endpoints as ep
from flask_restx import Resource, Api

class EndpointTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hello(self):
        hello = ep.HelloWorld(Resource)
        ret = hello.get()
        self.assertIsInstance(ret, dict)
        self.assertIn(ep.HELLO, ret)

    def test_list_rooms1(self):
        """
        Post-condition 1: return is a dictionary.
        """
        lr = ep.ListRooms(Resource)
        ret = lr.get()
        self.assertIsInstance(ret, dict)

    def test_list_rooms2(self):
        """
        Post-condition 2: keys to the dict are strings
        """
        lr = ep.ListRooms(Resource)
        ret = lr.get()
        for key in ret:
            self.assertIsInstance(key, str)

    def test_list_rooms3(self):
        """
        Post-condition 3: the values in the dict are themselves dicts
        """
        lr = ep.ListRooms(Resource)
        ret = lr.get()
        for val in ret.values():
            self.assertIsInstance(val, dict)

    def test_CreateUser(self):
        """
        Returns the name
        """
        name = "username"
        user = ep.CreateUser(Resource)
        ret = user.post(name)
        self.assertEquals(name, ret)

    def test_ice_cream_flavors1(self):
        """
        Post-condition 1: return is a dictionary.
        """
        flavors = ep.ListIceCream(Resource)
        ret = flavors.get()
        for val in ret.values():
            self.assertIsInstance(val, dict)

    def test_ice_cream_flavors2(self):
        """
        Post-condition 2: keys to the dict are strings
        """
        flavors = ep.ListIceCream(Resource)
        ret = flavors.get()
        for key in ret:
            self.assertIsInstance(key, str)

    def test_ice_cream_flavors3(self):
        """
        Post-condition 3: the values in the dict are themselves dicts
        """
        flavors = ep.ListIceCream(Resource)
        ret = flavors.get()
        for val in ret.values():
            self.assertIsInstance(val, dict)

    def test_price(self):
        flavors = ep.ListIceCream(Resource)
        price = flavors.get_price("Vanilla")
        self.assertIsInstance(price, int)
