from game import Game
from numpy import exp


class LearningRule:
    def __init__(self, configs):
        self.size = configs["size"]
        self.intensity = configs["intensity"]


class Conformity(LearningRule):
    def __init__(self, configs):
        super().__init__(configs)

    def fractionC(self, k):
        return k / self.size

    def fractionD(self, k):
        return (self.size - k) / self.size

    def Fermi(self, k):
        return (1 - exp(- self.intensity * (self.fractionD(k) - self.fractionC(k))))**(-1)


class SocialLearning(LearningRule):
    def __init__(self, configs):
        super().__init__(configs)
        self.game = Game(configs)

    def fitnessC(self, k: int): pass

    def fitnessD(self, k: int): pass

    def Fermi(self, k):
        return (1 - exp(- self.intensity * (self.fitnessD(k) - self.fitnessC(k))))**(-1)


class CounterfactualThinking(LearningRule):
    def __init__(self, configs):
        super().__init__(configs)
        self.game = Game(configs)

    def fitnessC(self, k: int): pass

    def fitnessD(self, k: int): pass

    def Fermi(self, k):
        return (1 - exp(- self.intensity * (self.fitnessD(k) - self.fitnessC(k))))**(-1)

