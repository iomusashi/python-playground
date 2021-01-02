from d17_question import Question
from d17_quiz_game_data import question_data


question_bank = list(map(lambda dict: Question(dict["text"], dict["answer"]),
                         question_data))
