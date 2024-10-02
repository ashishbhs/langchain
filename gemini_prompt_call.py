from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# part 1 : create a chatprompttempalte using a template string
# print("-----Prompt from Template-----")
# template = "tell me a joke about {topic}."
# prompt_template = ChatPromptTemplate.from_template(template)


# prompt = prompt_template.invoke({"topic": "cats"})
# result = model.invoke(prompt)
# print(result.content)

# part 2: prompt with multiple placeholders
# print("-----Prompt with multiple placeholders-----")
# template_multiple = """You are a helpful assistant.
# Human: Tell me a {adjective} story about a {animal}.
# Assistant:"""

# prompt_multiple = ChatPromptTemplate.from_template(template_multiple)
# prompt = prompt_multiple.invoke({"adjective": "funny", "animal":"Dog"})
# result = model.invoke(prompt)
# print(result.content)

# part 3: prompt with system and human messages (using tuples)
print("\n -----Propmpt with system and human messages(Tuple)-----\n")
messages = [
    ("system", "you are a comedian who tells jokes about {topic}."),#tuple format
    ("human", "tell me {joke_count} jokes."),
]

prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "lawyers", "joke_count": 3})
result = model.invoke(prompt)
print(result.content)

