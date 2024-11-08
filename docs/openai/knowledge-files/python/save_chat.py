import os
import re
import time
from datetime import datetime

def extract_conversation(input_text):
    """
    Extracts conversation exchanges between user and ChatGPT from the provided input text.
    
    :param input_text: Raw input text from the ChatGPT conversation.
    :return: List of conversation exchanges.
    """
    exchanges = re.findall(r'User: (.*?)\nAssistant: (.*?)\n', input_text, re.DOTALL)
    return exchanges

def format_as_markdown(exchanges):
    """
    Formats extracted conversation exchanges as markdown.
    
    :param exchanges: List of conversation exchanges.
    :return: Formatted markdown string.
    """
    md_text = ""
    for user, assistant in exchanges:
        md_text += f"### User:\n{user.strip()}\n\n### Assistant:\n{assistant.strip()}\n\n---\n\n"
    return md_text

def save_to_markdown(md_text, filename):
    """
    Saves markdown text to a .md file.
    
    :param md_text: Formatted markdown text.
    :param filename: Filename to save the markdown content.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(md_text)

def main(conversation_log):
    """
    Processes the current conversation log, formats it as markdown, and saves it to a markdown file.
    """
    # Extract and analyze conversation
    exchanges = extract_conversation(conversation_log)
    
    # Format conversation as markdown
    md_content = format_as_markdown(exchanges)
    
    # Define filename for saving markdown
    timestamp = time.strftime('%Y%m%d-%H%M%S')
    filename = f"/mnt/data/ChatGPT_Conversation_{timestamp}.md"
    
    # Save conversation as markdown
    save_to_markdown(md_content, filename)
    
    # Return the file path for download
    return filename

if __name__ == "__main__":
    # Example conversation log provided directly
    conversation_log = """
    User: An advantage of a personality test that is atheoretical in nature is that
    Group of answer choices

    the test will, in all likelihood, be more valid than a theory-based test.

    test users can interpret the test according to their own theoretical preferences.

    the test is much more likely to be "culture-specific" as well.

    the test is much more likely to be "culture-fair" as well.
    Assistant: The correct answer is: test users can interpret the test according to their own theoretical preferences.

    ---

    (Continue adding the rest of the conversation content here...)
    """

    # Run the function with the conversation log
    output_file = main(conversation_log)
    print(f"Download the conversation log: {output_file}")