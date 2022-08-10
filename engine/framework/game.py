"""
configurations = {
    "size": int,
    "intensity": float,
    "configs": {
        # for 2P games
        "R" : float,
        "S" : float,
        "T" : float,
        "P" : float
    }
}
"""

from scipy.special import comb as binom


class Game:
    def __init__(self, game_configurations):
        self.Z = game_configurations["size"]
        self.configs = game_configurations["configs"]

    def fitnessC(self, i: int): pass

    def fitnessD(self, i: int): pass

    def Gradient(self, i):
        return self.fitnessC(i) - self.fitnessD(i)


class Game2P(Game):
    def __init__(self, game_configurations):
        super().__init__(game_configurations)
        self.R = self.configs["R"]
        self.S = self.configs["S"]
        self.T = self.configs["T"]
        self.P = self.configs["P"]

    def fitnessC(self, i):
        """Returns the fitness for cooperators"""
        return ((i - 1) * self.R + (self.Z - i) * self.S) / (self.Z - 1)

    def fitnessD(self, i):
        """Returns the fitness for defectors"""
        return (i * self.T + (self.Z - i - 1) * self.P) / (self.Z - 1)


class GameNP(Game):
    def __init__(self, game_specs):
        super().__init__(game_specs)
        self.N = self.configs["N"]

    def payoffC(self, i: int):
        """Returns the payoff for cooperators"""
        pass

    def payoffD(self, i: int):
        """Returns the payoff for defectors"""
        pass

    def fitnessC(self, i: int):
        return 1 / binom(self.Z - 1, self.N - 1) * sum(
            [binom(i - 1, j) * binom(self.Z - i, self.N - j - 1) * self.payoffC(j + 1)
             for j in range(0, self.N, 1)])

    def fitnessD(self, i: int):
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
