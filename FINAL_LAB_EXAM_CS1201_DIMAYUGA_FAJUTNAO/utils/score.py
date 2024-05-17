class Score:
    def __init__(self):
        self.scores = []

    def load_scores(self):
        try:
            with open('scores.txt', 'r') as file:
                for line in file:
                    username, score = line.strip().split(',')
                    self.scores.append((username, int(score)))
        except FileNotFoundError:
            pass

    def save_scores(self):
        with open('scores.txt', 'w') as file:
            for username, score in self.scores:
                file.write(f"{username},{score}\n")

    def update_scores(self, user, score):
        self.scores.append((user.username, score))

    def get_top_scores(self):
        sorted_scores = sorted(self.scores, key=lambda x: x[1], reverse=True)
        return sorted_scores[:10]
