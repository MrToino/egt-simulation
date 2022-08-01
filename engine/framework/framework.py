from population import Population


class Framework:
    def __init__(self, pop_configs):
        self.pop_configs = pop_configs
        self.framework_type = self.pop_configs["FrameworkType"]
        self.populations = self.build_populations()

    def build_populations(self):
        populations = []
        for pop in self.pop_configs:
            populations.append(Population(pop))
        return populations
