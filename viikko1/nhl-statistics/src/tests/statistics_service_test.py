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
            Player("Coffey",  "PIT", 30, 83), # 30+83 = 113
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_search_name(self):
        name = "Gilmour"
        
        self.assertEqual(self.stats.search(name), Player("Gilmour", "CGY", 26, 59))

    def test_search_no_results(self):
        name = "Crosby"
        
        self.assertEqual(self.stats.search(name), None)

    def test_team_players(self):
        edmonton = [
            Player("Semenko", "EDM", 4, 12),
            Player("Kurri",   "EDM", 37, 53),
            Player("Gretzky", "EDM", 35, 89)
        ]

        self.assertCountEqual(self.stats.team("EDM"), edmonton)

    def test_top_points(self):
        top_list = [
            Player("Gretzky", "EDM", 35, 89),
            Player("Coffey",  "PIT", 30, 83),
            Player("Lemieux", "PIT", 45, 54),
            Player("Yzerman", "DET", 42, 56),
            Player("Kurri",   "EDM", 37, 53)
        ]

        self.assertEqual(self.stats.top(4), top_list)
