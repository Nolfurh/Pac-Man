class Statistics:
    """
    Class keeps track of game statistics such as the player's score, number of lives, and number of PacDots collected
    """
    score = 0
    lives = 3
    collectedPacDots = 0
    allPacDots = 0
    activatedBonuses = []
    win = False
    lose = False

    @staticmethod
    def check_win():
        """
        Check whether the player has won the game by collecting all PacDots and not losing.
        """
        if Statistics.collectedPacDots >= Statistics.allPacDots and not Statistics.lose:
            Statistics.win = True
