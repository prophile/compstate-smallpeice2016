class Scorer:
    def __init__(self, scoresheet):
        self.scoresheet = scoresheet

    def calculate_score(self, data):
        moved = data.get('moved', False)
        poison = data.get('poison', False)
        num_tokens = data.get('tokens', 0)
        token_score = 0 if poison else num_tokens
        movement_score = 2 if moved else 0
        return token_score + movement_score

    def calculate_scores(self):
        return {
            tla: self.calculate_score(data)
            for tla, data in self.scoresheet.items()
        }
