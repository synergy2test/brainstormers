import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage
from langchain_core.output_parsers import StrOutputParser



# parsers
def parse_bullet_points(ai_message: AIMessage) -> list:
    # Extract the content from the AIMessage object
    content = ai_message.content

    # Split the content into lines
    lines = content.split('\n')

    # Initialize an empty list to hold the parsed bullet points
    bullet_points = []

    # Iterate over each line
    for line in lines:
        # Strip leading and trailing whitespace
        stripped_line = line.strip()

        # Check if the line starts with a bullet point indicator
        if stripped_line.startswith('- '):
            # Remove the bullet point indicator and any leading/trailing whitespace
            bullet_point = stripped_line[2:].strip()
            # Append the cleaned bullet point to the list
            bullet_points.append(bullet_point)
        elif stripped_line.startswith('-'):
            # Handle cases where there's no space after the bullet point indicator
            bullet_point = stripped_line[1:].strip()
            bullet_points.append(bullet_point)
        elif stripped_line:
            # Handle lines that are part of a bullet point but don't start with '-'
            if bullet_points:
                # Append this line to the last bullet point, adding a space
                bullet_points[-1] += ' ' + stripped_line

    return bullet_points


class TreeNode:
    def __init__(self, idea):
        self.idea = idea
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)