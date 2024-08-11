
#TODO: asking the questions
#TODO: checking if the answer was correct
#TODO: checking if we're at the end of the quiz

class QuizBrain:
    question_number = 0
    question_list = []
    score = 0
    
    def __init__(self, question_list):
        ''' constructor '''
        self.question_list = question_list
    
    def next_question(self):
        ''' ask the next question '''
        answer = input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False): ")
        self.question_number += 1
        
        self.check_answer(answer, self.question_list[self.question_number - 1])
        
    def still_has_questions(self):
        ''' check if there are more questions '''
        return self.question_number < len(self.question_list)
    
    def check_answer(self, answer, question):
        ''' check if the answer is correct '''
        if answer.lower() == question.answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        
        print(f"The correct answer was: {question.answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")