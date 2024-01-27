import unittest
import os
import sys
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(sys.argv[0]))))

from date_calculator import get_quarter_start_end_dates, adjust_start_date, calculate_num_weeks

class TestDateCalculator(unittest.TestCase):
    def test_get_quarter_start_end_dates(self):
        start_date, end_date = get_quarter_start_end_dates(2022, 2)
        self.assertEqual(start_date.strftime('%Y-%m-%d'), '2022-02-01')
        self.assertEqual(end_date.strftime('%Y-%m-%d'), '2022-04-30')

    def test_adjust_start_date(self):
        start_date = adjust_start_date(datetime(2022, 2, 1))
        self.assertEqual(start_date.strftime('%Y-%m-%d'), '2022-02-07')
    
    def test_calculate_num_weeks(self):
        num_weeks = calculate_num_weeks(datetime(2022, 2, 1), datetime(2022, 4, 30))
        self.assertEqual(num_weeks, 13)

if __name__ == '__main__':
    unittest.main()
