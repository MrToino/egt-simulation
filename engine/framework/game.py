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


from numpy import exp


class Game:
    """Define the attributes and methods for a general game"""

    def __init__(self, game_configurations):
        """Initialize the general game parameters"""
        self.Z, self.B, self.mu = game_configurations["Z", "B", "mu"]
        self.configs = game_configurations["configs"]

    def fitnessC(self, i: int) -> float:
        """Compute the fitness for cooperators"""
        pass

    def fitnessD(self, i: int) -> float:
        """Compute the fitness for cooperators"""
        pass

    def fermiCD(self, i):
        """Compute the negative Fermi probability"""
        return (1 + exp(-self.B * (self.fitnessD(i) - self.fitnessC(i)))) ** (-1)

    def fermiDC(self, i):
        """Compute the positive Fermi probability"""
        return (1 + exp(-self.B * (self.fitnessC(i) - self.fitnessD(i)))) ** (-1)

    def TransitionCD(self, i):
        """Compute the negative transition probability"""
        return i / self.Z * (self.Z - i) / self.Z * self.fermiCD(i)

    def TransitionDC(self, i):
        """Compute the positive transition probability"""
        return i / self.Z * (self.Z - i) / self.Z * self.fermiDC(i)

    def Gradient(self, i):
        """Compute the gradient of selection"""
        return self.TransitionDC(i) - self.TransitionDC(i)

