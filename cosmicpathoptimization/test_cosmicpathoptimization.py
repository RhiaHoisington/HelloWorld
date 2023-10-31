import unittest
from cosmicpathoptimization import average


class TestCPO(unittest.TestCase):
    def setUp(self) -> None:
        self.planet_count1 = 1
        self.planet_count2 = 2
        self.planet_count3 = 4
        self.planet_count4 = 8
        self.planet_count5 = 16
        self.planet_count6 = 32
        self.temps1 = [31]
        self.temps2 = [8, 30]
        self.temps3 = [7196, 2748, 9637, 6359]
        self.temps4 = [5265, 3593, 368, 4773, 2724, 9207, 8483, 3147]
        self.temps5 = [608, 392, 470, 26, 634, 786, 516,
                       630, 811, 253, 762, 332, 4, 296, 299, 846]
        self.temps6 = [
            746,
            558,
            176,
            844,
            814,
            924,
            1000,
            717,
            551,
            125,
            687,
            929,
            15,
            34,
            622,
            460,
            651,
            479,
            659,
            956,
            821,
            523,
            35,
            432,
            619,
            793,
            422,
            874,
            139,
            368,
            319,
            6]

    def test_avg1(self) -> None:
        actual_ans = average(self.planet_count1, self.temps1)
        expected_ans = 31
        self.assertEqual(
            actual_ans, expected_ans, f'{
                actual_ans=} != {
                expected_ans=}')

    def test_avg2(self) -> None:
        actual_ans = average(self.planet_count2, self.temps2)
        expected_ans = 19
        self.assertEqual(
            actual_ans, expected_ans, f'{
                actual_ans=} != {
                expected_ans=}')

    def test_avg3(self) -> None:
        actual_ans = average(self.planet_count3, self.temps3)
        expected_ans = 6485
        self.assertEqual(
            actual_ans, expected_ans, f'{
                actual_ans=} != {
                expected_ans=}')

    def test_avg4(self) -> None:
        actual_ans = average(self.planet_count4, self.temps4)
        expected_ans = 4695
        self.assertEqual(
            actual_ans, expected_ans, f'{
                actual_ans=} != {
                expected_ans=}')

    def test_avg5(self) -> None:
        actual_ans = average(self.planet_count5, self.temps5)
        expected_ans = 479
        self.assertEqual(
            actual_ans, expected_ans, f'{
                actual_ans=} != {
                expected_ans=}')

    def test_avg6(self) -> None:
        actual_ans = average(self.planet_count6, self.temps6)
        expected_ans = 540
        self.assertEqual(
            actual_ans, expected_ans, f'{
                actual_ans=} != {
                expected_ans=}')
