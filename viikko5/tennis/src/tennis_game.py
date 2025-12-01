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
        score_names = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All"
        }
        if self.score_player1 in score_names:
            return score_names[self.score_player1]
        else:
            return "Deuce"

    def get_endgame_score(self):
        score_difference = self.score_player1 - self.score_player2
        leader = self.player1 if score_difference > 0 else self.player2

        if abs(score_difference) == 1:
            return f"Advantage {leader}"
        elif abs(score_difference) >= 2:
            return f"Win for {leader}"

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
