---
icon: python
---

# Randomized Selection. py \[v1]

```python
import random

class QuizEngine:
    def __init__(self, questions_df):
        """
        Initialize the quiz engine with a dataframe of questions.
        """
        self.questions_df = questions_df
        self.asked_questions = []

    def get_next_question(self, user_previous_answer=None, user_correct=None):
        """
        Select the next question based on the user's previous answer and difficulty level.
        If the user answered correctly, increase difficulty; otherwise, decrease.
        If no previous answer, select a random question.
        """
        if user_previous_answer is None:
            # First question: Select a random question from the entire pool
            available_questions = self.questions_df[~self.questions_df['id'].isin(self.asked_questions)]
        else:
            if user_correct:
                # If the user answered correctly, increase the difficulty (if possible)
                current_difficulty = min(self.get_difficulty_of_last_question() + 1, 2)
            else:
                # If the user answered incorrectly, decrease the difficulty (if possible)
                current_difficulty = max(self.get_difficulty_of_last_question() - 1, 0)
                
            # Select from the questions with the new difficulty level
            available_questions = self.questions_df[
                (~self.questions_df['id'].isin(self.asked_questions)) &
                (self.questions_df['difficulty'] == current_difficulty)
            ]

        # If no questions are available for that difficulty, fallback to a random question
        if available_questions.empty:
            available_questions = self.questions_df[~self.questions_df['id'].isin(self.asked_questions)]

        # Select and return a random question
        selected_question = available_questions.sample().iloc[0]
        self.asked_questions.append(selected_question['id'])
        
        return {
            'question': selected_question['question'],
            'choices': self.randomize_choices(selected_question),
            'correct_answer': selected_question['correct_answer'],
            'difficulty': selected_question['difficulty']
        }

    def randomize_choices(self, question_row):
        """
        Randomize the order of choices (correct_answer + choice_1 + choice_2 + choice_3).
        """
        choices = [question_row['correct_answer'], question_row['choice_1'], question_row['choice_2'], question_row['choice_3']]
        random.shuffle(choices)
        return choices

    def get_difficulty_of_last_question(self):
        """
        Get the difficulty level of the last asked question.
        """
        if self.asked_questions:
            last_question_id = self.asked_questions[-1]
            last_question_row = self.questions_df[self.questions_df['id'] == last_question_id]
            return int(last_question_row['difficulty'].values[0])
        else:
            return 0  # Default difficulty for the first question

```
