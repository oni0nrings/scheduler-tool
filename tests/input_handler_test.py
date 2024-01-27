import os
import sys
import unittest
from unittest.mock import patch

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(sys.argv[0]))))


class TestInputHandler(unittest.TestCase):
    @patch("input_handler.get_fiscal_year_and_quarter", return_value="2022")
    def test_get_year_and_quarter(self, get_fiscal_year_and_quarter):
        result = get_fiscal_year_and_quarter("Enter a year: ")
        self.assertEqual(result, "2022")


if __name__ == "__main__":
    unittest.main()
