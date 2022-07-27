from game import Game


class LearningRule:
    def __init__(self):
        pass


class Conformity(LearningRule):
    def __init__(self):
        super().__init__()


class SocialLearning(LearningRule):
    def __init__(self, configs):
        super().__init__()
        self.game = Game(configs)


class CounterfactualThinking(LearningRule):
    def __init__(self, configs):
        super().__init__()
        self.game = Game(configs)

