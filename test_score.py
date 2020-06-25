import unittest 
from score import Score

class TestCar(unittest.TestCase): #test_score

    def setUp(self):
        self.my_score = Score("2015,전교상,70,80,50")

    def tearDown(self):
        del self.my_score

    def test_constructor(self):
        self.assertIsNotNone(self.my_score)


    def test_no_1(self):
        self.assertEqual("2015", self.my_score.no)

    def test_name(self):
        self.assertEqual("전교상", self.my_score.name)

    def test_kor(self):
        self.assertEqual(70, self.my_score.kor)

    def test_eng(self):
        self.assertEqual(80, self.my_score.eng)

    def test_math(self):
        self.assertEqual(50, self.my_score.math)

    def test_sum(self):
        self.assertEqual(200, self.my_score.sum)

    def test_avg(self):
        self.assertEqual(66, self.my_score.avg)


if __name__ == "__main__":
    pass