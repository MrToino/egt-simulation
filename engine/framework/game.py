"""
Evolutionary Game Theory

Project: EGT-Sim
Package: framework
Filename: game.py
Description: defines the general game framework
"""


from numpy import exp


class Game:
    """Define the attributes and methods for a general game"""

    def __init__(self, game_configurations):
        """Initialize the general game parameters"""
        self.Z, self.B, self.U = game_configurations["Z", "B", "U"]
        self.configs = game_configurations["configs"]

    def fitnessC(self, i: int) -> float:
        """Compute the fitness for cooperators"""
        pass

    def fitnessD(self, i: int) -> float:
        """Compute the fitness for cooperators"""
        pass

    def fermiCD(self, i: int) -> float:
        """Compute the negative Fermi probability"""
        return (1 + exp(-self.B * (self.fitnessD(i) - self.fitnessC(i)))) ** (-1)

    def fermiDC(self, i: int) -> float:
        """Compute the positive Fermi probability"""
        return (1 + exp(-self.B * (self.fitnessC(i) - self.fitnessD(i)))) ** (-1)

    def TransitionCD(self, i: int) -> float:
        """Compute the negative transition probability"""
        return i / self.Z * (self.Z - i) / self.Z * self.fermiCD(i)

    def TransitionDC(self, i: int) -> float:
        """Compute the positive transition probability"""
        return i / self.Z * (self.Z - i) / self.Z * self.fermiDC(i)

    def Gradient(self, i: int) -> float:
        """Compute the gradient of selection"""
        return self.TransitionDC(i) - self.TransitionDC(i)

