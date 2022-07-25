class Game:
    def __init__(self, game_specs):
        self.game_specs = game_specs


class Game2P(Game):
    def __init__(self, game_specs):
        super().__init__(game_specs)


class HarmonyGame(Game2P):
    def __init__(self, game_specs):
        super().__init__(game_specs)


class PrisonersDilemma(Game2P):
    def __init__(self, game_specs):
        super().__init__(game_specs)


class SnowdriftGame(Game2P):
    def __init__(self, game_specs):
        super().__init__(game_specs)


class StagHunt(Game2P):
    def __init__(self, game_specs):
        super().__init__(game_specs)


class GameNP(Game):
    def __init__(self, game_specs):
        super().__init__(game_specs)


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
