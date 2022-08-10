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


class Game:
    def __init__(self, game_configurations):
        self.Z = game_configurations["size"]
        self.configs = game_configurations["configs"]

    def fitnessC(self, i: int) -> float: pass

    def fitnessD(self, i: int) -> float: pass

    def Gradient(self, i):
        return self.fitnessC(i) - self.fitnessD(i)


class NSnowdriftGame(GameNP):
    def __init__(self, game_specs):
        super().__init__(game_specs)


class NStagHunt(GameNP):
    def __init__(self, game_specs):
        super().__init__(game_specs)


class PublicGoodGames(GameNP):
    def __init__(self, game_specs):
        super().__init__(game_specs)


class CollectiveRiskDilemma(GameNP):
    def __init__(self, game_specs):
        super().__init__(game_specs)
