import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage
from utils import parse_bullet_points, TreeNode, print_tree

#import the OpenAI API key from the .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# LLMs
llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)

reverse_brainstorming_gen_ideas_prompt = ChatPromptTemplate.from_template("""You are a clever work assistant that helps people generate ideas for their project, reasearch, paper or any other creative work. You'll be having a query from the user and you need to generate 5 (five) diverse, detailed, developed, precise and significant ideas related to the context of the query. The ideas should not be redundant and repetitive, be creative and unique. The ideas must be formatted in the form of bullet points without titles and without bold text.
Query:{query}
List of 5 bullet points ideas:""")
reverse_brainstorming_prompt = ChatPromptTemplate.from_template("""
You are a perceptive problem-identification assistant that helps people analyze an idea by uncovering 5 potential issues or challenges it may encounter. The identified problems should be diverse, detailed, well-developed, precise, and significant. Avoid redundancy and repetition; ensure the problems are creative and unique. Present the problems in bullet points without titles and without bold text.

Idea to analyze: {idea}
List of 5 potential problems:
""")
reverse_brainstorming_gen_ideas_chain = reverse_brainstorming_gen_ideas_prompt | llm | parse_bullet_points
reverse_brainstorming_chain = reverse_brainstorming_prompt | llm | parse_bullet_points


user_query = "I am searching for ideas to automate hard tasks in any company using AI agents powered by LLMs"
root_rb = TreeNode(user_query)

initial_ideas = reverse_brainstorming_gen_ideas_chain.invoke({"query": user_query})

for idea in initial_ideas:
    child_node = TreeNode(idea)
    root_rb.add_child(child_node)

    reverse_brainstorming_ideas = reverse_brainstorming_chain.invoke({"idea": idea})

    for reverse_brainstorming_idea in reverse_brainstorming_ideas:
        grandchild_node = TreeNode(reverse_brainstorming_idea)
        child_node.add_child(grandchild_node)

print_tree(root_rb)