import pandas as pd
import random

class QuizEngine:
    def __init__(self, questions_df):
        """
        Initialize the quiz engine with a dataframe of questions.
        """
        self.questions_df = questions_df
        self.asked_questions = []
        self.correct_streak = 0
        self.incorrect_streak = 0
    
    def get_next_question(self, user_previous_answer=None, user_correct=None):
        """
        Select the next question based on the user's previous answer and difficulty level.
        If the user answered correctly, increase difficulty based on streaks; otherwise, decrease.
        """
        if user_previous_answer is None:
            available_questions = self.questions_df[~self.questions_df['id'].isin(self.asked_questions)]
        else:
            if user_correct:
                self.correct_streak += 1
                self.incorrect_streak = 0
                current_difficulty = min(self.get_difficulty_of_last_question() + (1 if self.correct_streak < 3 else 2), 2)
            else:
                self.incorrect_streak += 1
                self.correct_streak = 0
                current_difficulty = max(self.get_difficulty_of_last_question() - (1 if self.incorrect_streak < 3 else 2), 0)

            available_questions = self.questions_df[
                (~self.questions_df['id'].isin(self.asked_questions)) &
                (self.questions_df['difficulty'] == current_difficulty)
            ]

        if available_questions.empty:
            available_questions = self.questions_df[~self.questions_df['id'].isin(self.asked_questions)]

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
        Randomize the order of choices (correct_answer + choice_1 + choice_2 + choice_3 + choice_4).
        """
        choices = [question_row['choice_1'], question_row['choice_2'], question_row['choice_3'], question_row['choice_4']]
        random.shuffle(choices)
        return choices

    def get_difficulty_of_last_question(self):
        if self.asked_questions:
            last_question_id = self.asked_questions[-1]
            last_question_row = self.questions_df[self.questions_df['id'] == last_question_id]
            return int(last_question_row['difficulty'].values[0])
        else:
            return 0  # Default difficulty for the first question


def load_questions_from_csv(file_path):
    """
    Load questions from a CSV file into a pandas DataFrame. Ensure that the columns are properly structured.
    """
    questions_df = pd.read_csv(file_path)
    return questions_df


# Example usage (this would be called in your GPT process):
questions_file = 'Questions.csv'
questions_df = load_questions_from_csv(questions_file)

# Initialize the QuizEngine with the loaded DataFrame
quiz_engine = QuizEngine(questions_df)

# Example function call for a GPT-like environment
def administer_quiz(quiz_engine, user_responses=None):
    """
    Administer the quiz in a GPT-compatible format. Instead of using input(), responses are passed as arguments.
    :param user_responses: A list of tuples where each tuple is (user_answer, correct) for the corresponding question.
    """
    if user_responses is None:
        user_responses = []

    results = []
    for i, response in enumerate(user_responses):
        user_answer, user_correct = response
        
        # Get the next question based on user's previous answer
        question_data = quiz_engine.get_next_question(user_previous_answer=user_answer, user_correct=user_correct)
        
        # Log the question and the choices (replace print statements with a return of data for GPTs)
        question_text = f"Question: {question_data['question']}\nChoices: {question_data['choices']}"
        
        # Check if the answer is correct (this would normally be checked dynamically)
        correct = question_data['choices'][user_answer] == question_data['correct_answer']
        
        # Record the result
        results.append({
            'question': question_data['question'],
            'correct_answer': question_data['correct_answer'],
            'user_answer': question_data['choices'][user_answer],
            'correct': correct
        })

    # Return the results for this session (which can be returned to the GPT user)
    return results