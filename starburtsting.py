import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage
from langchain_core.output_parsers import StrOutputParser
from utils import parse_bullet_points, TreeNode



#import the OpenAI API key from the .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# LLMs
llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)

sb_gen_ideas_prompt = ChatPromptTemplate.from_template("""You are a clever work assistant that helps people generate ideas for their project, reasearch, paper or any other creative work. You'll be having a query from the user and you need to generate 5 (five) diverse, detailed, developed, precise and significant ideas related to the context of the query. The ideas should not be redundant and repetitive, be creative and unique. The ideas must be formatted in the form of bullet points without titles and without bold text.
Query:{query}
List of 5 bullet points ideas:""")

sb_questions_prompt = ChatPromptTemplate.from_template("""You are a clever question generator assistant that helps people in brainstorming and generating from one idea to 6 questions following the starbursting brainstorming principles: the 5 W's and 1 H (Who, What, Where, When, Why, How) to explore a topic comprehensively. The resulting questions should be diverse, detailed, developed, precise and significant. The questions must not be redundant and repetitive, be creative and unique. The question must be formatted in the form of bullet points without titles and without bold text.
Idea to brainstorm:{idea}
List of 6 bullet questions:""")

sb_answer_prompt = ChatPromptTemplate.from_template("""You are a clever answer assistant that helps people in answering questions related to a topic. You'll be having a question and you need to generate a detailed, developed, precise and significant answer to the question, according to a context given from the user. The answer should not be redundant and repetitive, be creative and unique. The answer must be formatted in the form of a paragraph.
Question:{question}
Context:{idea}
Answer:""")



sb_gen_ideas_chain = sb_gen_ideas_prompt | llm | parse_bullet_points
sb_questions_chain = sb_questions_prompt | llm | parse_bullet_points
sb_answer_chain = sb_answer_prompt | llm | StrOutputParser()


# wrapping up the starbursting chains

user_query = "I am searching for ideas to automate hard tasks in any company using AI agents powered by LLMs"
root_sb = TreeNode(user_query)

initial_ideas = sb_gen_ideas_chain.invoke({"query": user_query})

for idea in initial_ideas:
    child_node = TreeNode(idea)
    root_sb.add_child(child_node)

    questions = sb_questions_chain.invoke({"idea": idea})

    for question in questions:
        grandchild_node = TreeNode(question)
        child_node.add_child(grandchild_node)

        answer = sb_answer_chain.invoke({"question": question, "idea": idea})
        great_grandchild_node = TreeNode(answer)
        grandchild_node.add_child(great_grandchild_node)
# print the tree
def print_tree(node, indent=0):
    print('  ' * indent + node.idea)
    for child in node.children:
        print_tree(child, indent + 1)

print_tree(root_sb)


