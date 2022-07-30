from population import Population


class Framerwork:
    def __init__(self, pop_configs):
        self.pop_configs = pop_configs
        self.populations = self.build_populations()

    def build_populations(self):
        populations = []
        for pop in self.pop_configs:
            populations.append(Population(pop))
        return populations
