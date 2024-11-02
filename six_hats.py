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

six_hats_ideas_prompt = ChatPromptTemplate.from_template("""
You are a perceptive brainstorming assistant that helps people analyze an idea using the Six Thinking Hats method, developed by Edward de Bono. This method involves examining a topic from six distinct perspectives, each represented by a colored hat. Here’s how each hat works:

- White Hat: Focuses on objective data and factual information related to the idea.
- Red Hat: Considers emotions and intuition, exploring gut feelings and subjective reactions to the idea.
- Black Hat: Identifies potential problems, risks, and negative outcomes associated with the idea.
- Yellow Hat: Explores benefits, advantages, and optimistic aspects of the idea.
- Green Hat: Encourages creativity, alternative ideas, and innovative possibilities around the topic.
- Blue Hat: Manages the thinking process, providing structure and ensuring a balanced perspective.

For each hat, generate one distinct perspective based on the topic provided. Present the perspectives in bullet points without titles and without bold text.

Topic to analyze: {idea}
List of Six Thinking Hats perspectives:
""")
six_hats_gen_ideas_prompt = ChatPromptTemplate.from_template("""You are a clever work assistant that helps people generate ideas for their project, reasearch, paper or any other creative work. You'll be having a query from the user and you need to generate 5 (five) diverse, detailed, developed, precise and significant ideas related to the context of the query. The ideas should not be redundant and repetitive, be creative and unique. The ideas must be formatted in the form of bullet points without titles and without bold text.
Query:{query}
List of 5 bullet points ideas:""")
six_hats_ideas_chain = six_hats_ideas_prompt | llm | parse_bullet_points
six_hats_gen_ideas_chain = six_hats_gen_ideas_prompt | llm | parse_bullet_points

user_query = "I am searching for ideas to automate hard tasks in any company using AI agents powered by LLMs"
root_sh = TreeNode(user_query)

initial_ideas = six_hats_gen_ideas_chain.invoke({"query": user_query})

for idea in initial_ideas:
    child_node = TreeNode(idea)
    root_sh.add_child(child_node)

    six_hats_ideas = six_hats_ideas_chain.invoke({"idea": idea})

    for six_hats_idea in six_hats_ideas:
        grandchild_node = TreeNode(six_hats_idea)
        child_node.add_child(grandchild_node)

print_tree(root_sh)