"""
Evolutionary Game Theory

Project: EGT-Sim
Package: framework
Filename: game2p.py
Description: defines the N-person game framework
"""


from engine.framework.game import Game
from scipy.special import comb as binom


class GameNP(Game):
    """Define the attributes and methods specific for a N-person game"""

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

    def fitnessD(self, i: int) -> float:
        """Returns the fitness for defectors"""
        return 1 / binom(self.Z - 1, self.N - 1) * sum(
            [binom(i, j) * binom(self.Z - i - 1, self.N - j - 1) * self.payoffD(j)
             for j in range(0, self.N, 1)])


class NSnowdriftGame(GameNP):
    """Define the attributes and methods specific for a N-person Snowdrift Game"""

    def __init__(self, game_specs):
        """Initialize the general game class"""
        super().__init__(game_specs)
        self.M, self.b, self.c = self.configs["M", "b", "c"]

    def payoffC(self, i) -> float:
        """Computes the payoff for cooperators"""
        return (-self.c / self.M if i < self.M else self.b - self.c / i) if i > 0 else 0

    def payoffD(self, i) -> float:
        """Computes the payoff for defectors"""
        return 0 if i < self.M else self.b


class NStagHunt(GameNP):
    """Define the attributes and methods specific for a N-person Stag-Hunt Game"""

    def __init__(self, game_specs):
        """Initialize the general game class"""
        super().__init__(game_specs)
        self.M, self.b, self.c = self.configs["M", "b", "c"]

    def payoffC(self, i) -> float:
        """Computes the payoff for cooperators"""
        return (-self.c / self.M if i < self.M else self.b - self.c / i) if i > 0 else 0

    def payoffD(self, i) -> float:
        """Computes the payoff for defectors"""
        return 0 if i < self.M else self.b


class PublicGoodGames(GameNP):
    """Define the attributes and methods specific for a Public Good Game"""

    def __init__(self, game_specs):
        """Initialize the general game class"""
        super().__init__(game_specs)
        self.b, self.c = self.configs["b", "c"]

    def payoffC(self, i) -> float:
        """Computes the payoff for cooperators"""
        return (-self.c / self.M if i < self.M else self.b - self.c / i) if i > 0 else 0

    def payoffD(self, i) -> float:
        """Computes the payoff for defectors"""
        return 0 if i < self.M else self.b


class CollectiveRiskDilemma(GameNP):
    """Define the attributes and methods specific for a Collective Risk Dilemma"""

    def __init__(self, game_specs):
        """Initialize the general game class"""
        super().__init__(game_specs)
        self.M, self.b, self.c, self.r = self.configs["M", "b", "c", "r"]

    def payoffC(self, i) -> float:
        """Computes the payoff for cooperators"""
        return (-self.c / self.M if i < self.M else self.b - self.c / i) if i > 0 else 0

    def payoffD(self, i) -> float:
        """Computes the payoff for defectors"""
        return 0 if i < self.M else self.b

