from d17_question import Question


class QuestionBrain:
    """
    Organizes and randomizes quiz questions per attempt
    """

    def __init__(self, questions_list: [Question]):
        """
        Creates an instance of QuestionBrain
        question_number - int
        questions_list - [Question]
        """
        self.score = 0
        self.question_number = 0
        self.questions_list = questions_list

    def has_next_questions(self) -> bool:
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        answer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False): ")
        if self.check_answer(answer, current_question.answer):
            self.score += 1

    def check_answer(self, answer: str, correct_answer: str) -> bool:
        return answer.lower() == correct_answer.lower()

    def print_score(self):
        print(
            f"Your final score is: {self.score} of {len(self.questions_list)}")
