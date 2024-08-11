# Question class for storing text and answer
class Question:
    
    def __init__(self, text, answer):
        ''' initializes the question with a text and answer '''
        self.text = text
        self.answer = answer