import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89), # 35+89 = 124
            Player("Turgeon", "BUF", 28, 49), # 34+54 = 88
            Player("Gilmour", "CGY", 26, 59), # 26+59 = 85
            Player("Coffey", "PIT", 30, 83), # 30+83 = 113
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_search(self):
        name = "Gilmour"
        
        self.assertEqual(self.stats.search(name), Player("Gilmour", "CGY", 26, 59))