import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage
from utils import parse_bullet_points, TreeNode

#import the OpenAI API key from the .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# LLMs
llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)

# Prompts
mm_gen_ideas_prompt = ChatPromptTemplate.from_template("""You are a clever work assistant that helps people generate ideas for their project, reasearch, paper or any other creative work. You'll be having a query from the user and you need to generate 5 (five) diverse, detailed, developed, precise and significant ideas related to the context of the query. The ideas should not be redundant and repetitive, be creative and unique. The ideas must be formatted in the form of bullet points without titles and without bold text.
Query:{query}
List of 5 bullet points ideas:""")

mm_expand_idea_prompt = ChatPromptTemplate.from_template("""You are a clever idea expansion assistant that helps people expand one idea into 5 other related ideas. The resulting ideas should be diverse, detailed, developed, precise and significant. The ideas should not be redundant and repetitive, be creative and unique. The ideas must be formatted in the form of bullet points without titles and without bold text.
Idea to expand:{idea}
List of 5 bullet points ideas:""")


# chains

mm_gen_ideas_chain = mm_gen_ideas_prompt | llm | parse_bullet_points 
mm_expand_idea_chain = mm_expand_idea_prompt | llm | parse_bullet_points


# Main loop
# Initialize the root node with the user's query
user_query = "I am searching for ideas to automate hard tasks in any company using AI agents powered by LLMs"

root = TreeNode(user_query)

# Generate 10 initial ideas
initial_ideas = mm_gen_ideas_chain.invoke({"query": user_query})

# Add each initial idea as a child of the root
for idea in initial_ideas:
    child_node = TreeNode(idea)
    root.add_child(child_node)

    # Expand each initial idea into 10 more ideas
    expanded_ideas = mm_expand_idea_chain.invoke({"idea": idea})

    # Add each expanded idea as a child of the current initial idea
    for expanded_idea in expanded_ideas:
        grandchild_node = TreeNode(expanded_idea)
        child_node.add_child(grandchild_node)

        # Expand each expanded idea into 10 more ideas
        further_expanded_ideas = mm_expand_idea_chain.invoke({"idea": expanded_idea})
        
        # Add each further expanded idea as a child of the current expanded idea
        for further_expanded_idea in further_expanded_ideas:
            great_grandchild_node = TreeNode(further_expanded_idea)
            grandchild_node.add_child(great_grandchild_node)
