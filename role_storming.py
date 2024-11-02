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

role_storming_gen_ideas_prompt = ChatPromptTemplate.from_template("""You are a clever work assistant that helps people generate ideas for their project, reasearch, paper or any other creative work. You'll be having a query from the user and you need to generate 5 (five) diverse, detailed, developed, precise and significant ideas related to the context of the query. The ideas should not be redundant and repetitive, be creative and unique. The ideas must be formatted in the form of bullet points without titles and without bold text.
Query:{query}
List of 5 bullet points ideas:""")
role_storming_prompt = ChatPromptTemplate.from_template("""
You are a clever idea generator assistant that helps people brainstorm and generate ideas using the Role Storming method. This involves adopting various personas to generate diverse perspectives and enrich the brainstorming process. Each persona brings a unique approach, exploring different angles and highlighting creative possibilities.

Here’s an explanation of each persona's perspective:

- Overly Positive Persona: Enthusiastically embraces every aspect of the topic, looking for the best-case scenarios and highlighting optimistic outcomes. They encourage unbridled creativity and focus on the potential for success.
  
- Overly Negative Persona: Views the topic critically, focusing on potential pitfalls, risks, and drawbacks. This persona helps in identifying challenges and preparing solutions for potential failures or issues.

- Curious Child: Approaches the topic with pure curiosity, asking "why" and "what if" questions. They explore without limitations, bringing fresh, out-of-the-box ideas that challenge existing assumptions.

- Skeptical Analyst: Takes a detailed, logical approach, questioning every part of the topic to uncover weaknesses or risks. This persona brings depth to the analysis, ensuring that ideas are well thought out and practical.

- Visionary Futurist: Considers the long-term implications and future possibilities of the topic, imagining how it could evolve. They focus on innovative, forward-thinking perspectives, pushing boundaries and considering future trends.

Generate 5 unique ideas based on the topic provided, with each idea presented in a bullet point and link each idea to its persona’s distinct approach, exploring the topic comprehensively. Format the list in bullet points without titles or bold text.

Topic to brainstorm: {idea}
List of Role Storming ideas by persona bullet points:
""")
role_storming_gen_ideas_chain = role_storming_gen_ideas_prompt | llm | parse_bullet_points
role_storming_chain = role_storming_prompt | llm | parse_bullet_points


user_query = "I am searching for ideas to automate hard tasks in any company using AI agents powered by LLMs"
root_rs = TreeNode(user_query)

initial_ideas = role_storming_gen_ideas_chain.invoke({"query": user_query})

for idea in initial_ideas:
    child_node = TreeNode(idea)
    root_rs.add_child(child_node)

    role_storming_ideas = role_storming_chain.invoke({"idea": idea})

    for role_storming_idea in role_storming_ideas:
        grandchild_node = TreeNode(role_storming_idea)
        child_node.add_child(grandchild_node)

print_tree(root_rs)