import unittest

from myagro import get_days_of_power


class TestDaysOfPower(unittest.TestCase):
    def test_days_of_power_with_3_distinct_days(self):
        days_of_power = get_days_of_power(
            R1=3000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=700000)
        self.assertEqual(days_of_power, 141)

    def test_days_of_power_with_3_distinct_days_2(self):
        days_of_power = get_days_of_power(
            R1=500, D1=3, R2=500, D2=10, R3=500, D3=7, K=21000)
        self.assertEqual(days_of_power, 17)

    def test_days_of_power_with_2_distinct_days_same_min(self):
        days_of_power = get_days_of_power(
            R1=1300, D1=2, R2=500, D2=2, R3=1500, D3=7, K=10000)
        self.assertEqual(days_of_power, 5)

    def test_days_of_power_for_one_day_amount(self):
        days_of_power = get_days_of_power(
            R1=10000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=11000)
        self.assertEqual(days_of_power, 1)

    def test_days_of_power_with_2_distinct_days_same_max(self):
            days_of_power = get_days_of_power(
                R1=1300, D1=2, R2=500, D2=7, R3=1500, D3=7, K=10000)
            self.assertEqual(days_of_power, 6)

    def test_days_of_power_same_start_days(self):
            days_of_power = get_days_of_power(
                R1=1300, D1=2, R2=500, D2=2, R3=1500, D3=2, K=10000)
            self.assertEqual(days_of_power, 3)