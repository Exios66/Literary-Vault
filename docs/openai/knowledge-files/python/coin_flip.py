import pandas as pd
import random
import re
import os

def flip_coin():
    """
    Returns True or False based on a 50/50 coin flip.
    """
    # Randomly select between True and False to simulate a fair coin flip
    return random.choice([True, False])

def alter_fact(fact):
    """
    Alters the provided fact to create a false version of it.
    The alteration is naive and works by switching words or values.
    """
    # This function takes a simple approach of altering keywords like verbs to create uncertainty.
    # Example: "is" might be replaced by "might" to cast doubt on the statement.
    altered_fact = re.sub(r'\b(is|are|was|were|has|have|had|can|could|will|would)\b', 'might', fact, count=1)
    # If no substitution was made (e.g., if the fact doesn't contain any of these words), append misleading text
    if altered_fact == fact:
        altered_fact += " (This might not be entirely accurate.)"
    return altered_fact

def present_facts(df, num_facts):
    """
    Presents a specified number of facts from the DataFrame.
    
    Args:
    - df (DataFrame): The DataFrame containing the facts.
    - num_facts (int): The number of facts to present.
    """
    # Randomly select the specified number of facts from the DataFrame
    selected_facts = df.sample(n=num_facts)
    for index, row in selected_facts.iterrows():
        fact = row['fact']
        
        # Flip a coin to decide whether to present the fact truthfully or falsely
        if flip_coin():
            # Present the true fact
            presented_fact = fact
            truthfulness = "TRUE"
        else:
            # Present a false version of the fact
            presented_fact = alter_fact(fact)
            truthfulness = "FALSE"
        
        # Print the result for evaluation, indicating whether the fact is true or false
        print(f"Fact #{index + 1}: {presented_fact} (Truthfulness: {truthfulness})")

def load_questions_file():
    """
    Loads the appropriate questions CSV file based on user input.
    
    Returns:
    - str: The filename of the chosen questions CSV file.
    """
    # Predefined list of available files
    available_files = [
        'psychology_questions.csv',
        'literature_questions.csv',
        'politics_questions.csv',
        'american_history_questions.csv',
        'chemistry_questions.csv'
    ]
    
    # Add any other CSV files in the current directory to the available files list
    for file in os.listdir():
        if file.endswith('.csv') and file not in available_files:
            available_files.append(file)
    
    # Display available files to the user
    print("Available question files:")
    for i, file in enumerate(available_files, start=1):
        print(f"{i}. {file}")
    
    # Prompt the user to choose a file
    try:
        file_choice = int(input("Enter the number corresponding to the file you want to use: "))
        # Ensure the user's choice is valid
        if 1 <= file_choice <= len(available_files):
            return available_files[file_choice - 1]
        else:
            print("Invalid choice. Please try again.")
            return load_questions_file()
    except ValueError:
        # Handle the case where the user does not enter a valid integer
        print("Invalid input. Please enter a number.")
        return load_questions_file()

def main():
    # Load the chosen questions CSV file
    questions_file = load_questions_file()
    try:
        # Read the selected CSV file into a DataFrame
        df = pd.read_csv(questions_file)
    except FileNotFoundError:
        # Handle the case where the file cannot be found
        print(f"Error: '{questions_file}' file not found.")
        return
    
    # Ensure the CSV has a 'fact' column
    if 'fact' not in df.columns:
        # If the 'fact' column is missing, display an error message and exit
        print("Error: The CSV file must contain a 'fact' column.")
        return
    
    # Prompt user for input to select the number of facts to present
    user_input = input("Enter 'one' for 1 fact, 'five' for 5 facts, or 'ten' for 10 facts: ").strip().lower()
    
    # Determine how many facts to present based on user input
    if user_input == 'one':
        present_facts(df, 1)
    elif user_input == 'five':
        present_facts(df, 5)
    elif user_input == 'ten':
        present_facts(df, 10)
    else:
        # Handle invalid input
        print("Invalid input. Please enter 'one', 'five', or 'ten'.")

if __name__ == "__main__":
    main()
