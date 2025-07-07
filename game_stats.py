class GameStats:
    """track statistics for Alien Invasion."""

    def __init__(self , ai_game):
        """intialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        self.game_active = False

        self.high_score = 0

    def reset_stats(self):
        """intialize that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0