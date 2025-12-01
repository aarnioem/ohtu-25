class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = player1_name
        self.player2 = player2_name
        self.score_player1 = 0
        self.score_player2 = 0

    def won_point(self, player_name):
        if player_name == self.player1:
            self.score_player1 += 1
        elif player_name == self.player2:
            self.score_player2 += 1

    def get_score(self):
        if self.score_player1 == self.score_player2:
            score = self.get_even_score()

        elif self.score_player1 >= 4 or self.score_player2 >= 4:
            score = self.get_endgame_score()

        else:
            score = self.get_normal_scores()

        return score

    def get_even_score(self):
        if self.score_player1 == 0 and self.score_player2 == 0:
            score = "Love-All"
        elif self.score_player1 == 1 and self.score_player2 == 1:
            score = "Fifteen-All"
        elif self.score_player1 == 2 and self.score_player2 == 2:
            score = "Thirty-All"
        else:
            score = "Deuce"
        return score

    def get_endgame_score(self):
        score_difference = self.score_player1 - self.score_player2

        if score_difference == 1:
            score = "Advantage player1"
        elif score_difference == -1:
            score = "Advantage player2"
        elif score_difference >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score

    def get_normal_scores(self):
        score_names = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }

        score_name1 = score_names[self.score_player1]
        score_name2 = score_names[self.score_player2]
        return f"{score_name1}-{score_name2}"
