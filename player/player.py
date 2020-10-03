class Player:
    def __init__(self, number):
        self.number = number
        self.score = 0
        self.won = False
        self.prev_score = 0

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def get_won(self):
        return self.won

    def set_won(self, won):
        self.won = won

    def get_number(self):
        return self.number

    def set_prev_score(self, score):
        self.prev_score = score

    def get_prev_score(self):
        return self.prev_score

    def __str__(self):
        self.number

