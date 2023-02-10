"""
    sample tests

"""

from django.test import SimpleTestCase

from app import calc



class CalcTests(SimpleTestCase):
    """ test the calc module. """

    def test_add_numbers(self):
        """ test adding number together """

        res = calc.add(5, 6)
        self.assertEqual(res, 11)
    def test_substract_number(self):
        """ test substracting number. """
        res = calc.substract(10, 15)
        self.assertEqual(res, 5)
