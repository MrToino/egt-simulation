from game import Game


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
        return - self.intensity * (self.fractionD(k) - self.fractionC(k))


class SocialLearning(LearningRule):
    def __init__(self, configs):
        super().__init__(configs)
        self.game = Game(configs)


class CounterfactualThinking(LearningRule):
    def __init__(self, configs):
        super().__init__(configs)
        self.game = Game(configs)

