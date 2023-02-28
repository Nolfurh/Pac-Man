class Statistics:
    """
    Class keeps track of game statistics such as the player's score, number of lives, and number of PacDots collected

    Attributes
    ----------
    score : int
        Score of current game.
    lives : int
        Game lives of Pac-man
    collectedPacDots : int
        Number of dots that pac-man already collected
    allPacDots : int
        The total number of Pac-Dots on the map.
    activatedBonuses:
        Array of activated bonuses
    win: boolean
        Current state of game.
    lose: boolean
        Current state of game.
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
