import unittest
import re
from datetime import datetime

def validate_symbol(symbol):
    return bool(re.fullmatch(r'[A-Z]{1,7}', symbol))

def validate_chart_type(chart_type):
    return chart_type in ('1', '2')

def validate_time_series(time_series):
    return time_series in ('1', '2', '3', '4')

def validate_date(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

class TestStockVisualizerInputs(unittest.TestCase):

    def test_symbol(self):
        self.assertTrue(validate_symbol("AAPL"))
        self.assertTrue(validate_symbol("TSLA"))
        self.assertFalse(validate_symbol("appl"))
        self.assertFalse(validate_symbol("TOOLONGSYMBOL"))
        self.assertFalse(validate_symbol("AAPL1"))

    def test_chart_type(self):
        self.assertTrue(validate_chart_type('1'))
        self.assertTrue(validate_chart_type('2'))
        self.assertFalse(validate_chart_type('3'))
        self.assertFalse(validate_chart_type('a'))
        self.assertFalse(validate_chart_type(''))

    def test_time_series(self):
        self.assertTrue(validate_time_series('1'))
        self.assertTrue(validate_time_series('4'))
        self.assertFalse(validate_time_series('5'))
        self.assertFalse(validate_time_series('0'))
        self.assertFalse(validate_time_series('x'))

    def test_start_date(self):
        self.assertTrue(validate_date("2024-01-01"))
        self.assertTrue(validate_date("1999-12-31"))
        self.assertFalse(validate_date("01-01-2024"))
        self.assertFalse(validate_date("2024/01/01"))
        self.assertFalse(validate_date("Jan 1 2024"))

    def test_end_date(self):
        self.assertTrue(validate_date("2024-12-31"))
        self.assertTrue(validate_date("2025-05-05"))
        self.assertFalse(validate_date("12-31-2024"))
        self.assertFalse(validate_date("2024/12/31"))
        self.assertFalse(validate_date("Dec 31 2024"))

if __name__ == '__main__':
    unittest.main()
