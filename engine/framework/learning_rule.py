from game import Game
from numpy import exp


class LearningRule:
    def __init__(self, configs):
        self.size = configs["size"]
        self.intensity = configs["intensity"]

    def fitnessC(self, k: int): pass

    def fitnessD(self, k: int): pass


class Conformity(LearningRule):
    def __init__(self, configs):
        super().__init__(configs)

    def fitnessC(self, k):
        return k / self.size

    def fitnessD(self, k):
        return (self.size - k) / self.size

    def Fermi(self, k):
        return (1 - exp(- self.intensity * (self.fitnessD(k) - self.fitnessC(k))))**(-1)


class SocialLearning(LearningRule):
    def __init__(self, configs):
        super().__init__(configs)
        self.game = Game(configs)

    def fitnessC(self, i: int) -> float:
        return self.game.fitnessC(i)

    def fitnessD(self, i: int) -> float:
        return self.game.fitnessD(i)

    def Fermi(self, k):
        return (1 - exp(- self.intensity * (self.fitnessD(k) - self.fitnessC(k))))**(-1)


class CounterfactualThinking(LearningRule):
    def __init__(self, configs):
        super().__init__(configs)
        self.game = Game(configs)

    def fitnessC(self, k: int): pass

    def fitnessD(self, k: int): pass

    def Fermi(self, k):
        return (1 - exp(- self.intensity * (self.fitnessD(k-1) - self.fitnessC(k))))**(-1)

