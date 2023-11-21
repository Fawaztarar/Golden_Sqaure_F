class GrammarStats:
    def __init__(self):
        self.total_texts = 0
        self.passed_texts = 0
        

    def check(self, text):
        if not text:
            return False

        self.total_texts += 1

        if text[0].isupper() and text[-1] in ".!?":
            self.passed_texts += 1
            return True
        return False

    def percentage_good(self):
        
        if self.total_texts == 0:
            return 0
        return int((self.passed_texts / self.total_texts) * 100)