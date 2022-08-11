"""
Evolutionary Game Theory

Project: EGT-Sim
Package: framework
Filename: game2p.py
Description: defines the 2-person game framework
"""


from engine.framework.game import Game
from scipy.special import comb as binom


class GameNP(Game):
    def __init__(self, game_specs):
        """Initialize the general game class"""
        super().__init__(game_specs)
        self.N = self.configs["N"]

    def payoffC(self, i: int) -> float:
        """Returns the payoff for cooperators"""
        pass

    def payoffD(self, i: int) -> float:
        """Returns the payoff for defectors"""
        pass

    def fitnessC(self, i: int) -> float:
        """Returns the fitness for cooperators"""
        return 1 / binom(self.Z - 1, self.N - 1) * sum(
            [binom(i - 1, j) * binom(self.Z - i, self.N - j - 1) * self.payoffC(j + 1)
             for j in range(0, self.N, 1)])

    def fitnessD(self, i: int):
        """Returns the fitness for defectors"""
        return 1 / binom(self.Z - 1, self.N - 1) * sum(
            [binom(i, j) * binom(self.Z - i - 1, self.N - j - 1) * self.payoffD(j)
             for j in range(0, self.N, 1)])


class NSnowdriftGame(GameNP):
    def __init__(self, game_specs):
        super().__init__(game_specs)


class NStagHunt(GameNP):
    def __init__(self, game_specs):
        super().__init__(game_specs)


class PublicGoodGames(GameNP):
    def __init__(self, game_specs):
        super().__init__(game_specs)


class CollectiveRiskDilemma(GameNP):
    def __init__(self, game_specs):
        super().__init__(game_specs)