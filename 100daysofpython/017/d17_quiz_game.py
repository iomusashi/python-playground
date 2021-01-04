from d17_question import Question
from d17_quiz_brain import QuestionBrain
from d17_quiz_game_data import question_data

question_bank = list(map(lambda dict: Question(dict["text"], dict["answer"]),
                         question_data))

quiz = QuestionBrain(question_bank)

while quiz.has_next_questions():
    quiz.next_question()

quiz.print_score()
