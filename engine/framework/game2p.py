"""
Evolutionary Game Theory

Project: EGT-Sim
Package: framework
Filename: game2p.py
Description: defines the 2-person game framework
"""

from engine.framework.game import Game


class Game2P(Game):
    def __init__(self, game_configurations):
        """Initialize the general game class"""
        super().__init__(game_configurations)
        self.R, self.S, self.T, self.P = self.configs["R", "S", "T", "P"]

    def fitnessC(self, i):
        """Returns the fitness for cooperators"""
        return ((i - 1) * self.R + (self.Z - i) * self.S) / (self.Z - 1)

    def fitnessD(self, i):
        """Returns the fitness for defectors"""
        return (i * self.T + (self.Z - i - 1) * self.P) / (self.Z - 1)