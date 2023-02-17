class Statistics:
    score = 0
    lives = 3
    collectedPacDots = 0
    allPacDots = 0
    activatedBonuses = []
    win = False
    lose = False

    @staticmethod
    def check_win():
        if Statistics.collectedPacDots >= Statistics.allPacDots:
            Statistics.win = True
