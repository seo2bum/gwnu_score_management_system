import unittest
from score_management_system import ScoreManagementSystem
from unittest.mock import Mock
from unittest.mock import patch
from unittest.mock import mock_open

class TestScoreManagementSystem(unittest.TestCase):

    def setUp(self):
        self.m_open = mock_open(read_data="2015,전교상,70,80,50\n2017,박민성,85,90,95\n2017,서이범,80,70,60")

        self.m_write_open = mock_open()
        self.m_w = mock_open().return_value
        self.m_write_open.side_effect = [self.m_open.return_value, self.m_w]

    def test_constructor(self):
        cms = ScoreManagementSystem()
        self.assertIsNotNone(cms) # test_score_management_system

    def test_read(self): 
        with patch('score_management_system.open', self.m_open):
            cms = ScoreManagementSystem()
            self.assertEqual(3, cms.read('score.csv'))

        self.m_open.assert_called_with('score.csv', 'rt', encoding='utf-8')

    def test_sort_1(self):
        with patch('score_management_system.open', self.m_open):
            cms = ScoreManagementSystem()
            cms.read('score.csv')

            result = cms.sort(order_key="register", order_way="asc")
            self.assertEqual('1,2015,전교상,70,80,50,200,66\n2017,박민성,85,90,95,270,90\n2017,서이범,80,70,60,210,70', result)

    def test_sort_2(self):
        with patch('score_management_system.open', self.m_open):
            cms = ScoreManagementSystem()
            cms.read('score.csv')

            result = cms.sort(order_key="register", order_way="des")
            self.assertEqual('3,2017,서이범,80,70,60,210,70\n2017,박민성,85,90,95,270,90\n2015,전교상,70,80,50,200,66', result)

    def test_sort_3(self):      
        with patch('score_management_system.open', self.m_open):
            cms = ScoreManagementSystem()
            cms.read('score.csv')

            result = cms.sort("avg","asc")
            self.assertEqual('2,2017,박민성,85,90,95,270,90\n2017,서이범,80,70,60,210,70\n2015,전교상,70,80,50,200,66', result)

    def test_sort_4(self):      
        with patch('score_management_system.open', self.m_open):
            cms = ScoreManagementSystem()
            cms.read('score.csv')

            result = cms.sort("avg", "des")
            self.assertEqual('1,2015,전교상,70,80,50,200,66\n2017,서이범,80,70,60,210,70\n2017,박민성,85,90,95,270,90', result)

    def test_write_1(self):
        with patch('score_management_system.open', self.m_write_open):
            cms = ScoreManagementSystem()
            cms.read('score.csv')
            cms.write('result.csv')

        self.m_w.write.assert_called_with("1,2015,전교상,70,80,50,200,66\n2017,박민성,85,90,95,270,90\n2017,서이범,80,70,60,210,70")


    def test_write_2(self):
        with patch('score_management_system.open', self.m_write_open):
            cms = ScoreManagementSystem()
            cms.read('score.csv')
            cms.write('result.csv' , 'register', 'des')

        self.m_w.write.assert_called_with("3,2017,서이범,80,70,60,210,70\n2017,박민성,85,90,95,270,90\n2015,전교상,70,80,50,200,66")

    def test_write_3(self):
        with patch('score_management_system.open', self.m_write_open):
            cms = ScoreManagementSystem()
            cms.read('score.csv')
            cms.write('result.csv' , 'avg', 'asc')

        self.m_w.write.assert_called_with("2,2017,박민성,85,90,95,270,90\n2017,서이범,80,70,60,210,70\n2015,전교상,70,80,50,200,66")

    def test_write_4(self):
        with patch('score_management_system.open', self.m_write_open):
            cms = ScoreManagementSystem()
            cms.read('score.csv')
            cms.write('result.csv' , 'avg', 'des')

        self.m_w.write.assert_called_with("1,2015,전교상,70,80,50,200,66\n2017,서이범,80,70,60,210,70\n2017,박민성,85,90,95,270,90")


if __name__ == "__main__":
    unittest.main() 