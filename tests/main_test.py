import os
import sys
import unittest
from unittest.mock import patch

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from main import main

class TestMain(unittest.TestCase):
    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data='Alice\nBob\nCharlie\n')
    @patch('main.get_fiscal_year_and_quarter', return_value=(2022, 1))
    def test_main(self, mock_get_fiscal_year_and_quarter, mock_open):
        schedule = main()
        
        # Check that the schedule has the correct number of entries
        self.assertEqual(len(schedule), 3)
        
        # Check that each name appears in the schedule
        for name in ['Alice', 'Bob', 'Charlie']:
            self.assertIn(name, schedule.values())

if __name__ == '__main__':
    unittest.main()
