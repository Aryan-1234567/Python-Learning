class ScoreBoard:
    def __init__(self, scores):
        self.__scores = scores

    def get_scores(self):
        print(self.__scores)

s1 = ScoreBoard(0)
print(s1.get_scores())