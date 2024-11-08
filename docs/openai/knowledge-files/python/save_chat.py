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

def main(conversation_file):
    # Load conversation from file
    with open(conversation_file, 'r', encoding='utf-8') as f:
        raw_text = f.read()
    
    # Extract and analyze conversation
    exchanges = extract_conversation(raw_text)
    
    # Format conversation as markdown
    md_content = format_as_markdown(exchanges)
    
    # Define filename for saving markdown
    timestamp = time.strftime('%Y%m%d-%H%M%S')
    filename = f"ChatGPT_Conversation_{timestamp}.md"
    
    # Save conversation as markdown
    save_to_markdown(md_content, filename)
    
    # Provide download link (example output for local context)
    download_url = f"./{filename}"
    print(f"Download the conversation: {download_url}")

if __name__ == "__main__":
    # Example usage with a sample file
    conversation_log = "chat_history.txt"
    main(conversation_log)
