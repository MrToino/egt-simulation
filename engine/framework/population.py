from learning_rule import LearningRule


class Population:
    def __init__(self, population_configs):
        self.configs = population_configs
        self.learning_rule = LearningRule(self.configs["Learning Rule"])
