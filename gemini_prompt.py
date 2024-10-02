from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage


# part 1 : create a chatprompttempalte using a template string
# template = "tell me a joke about {topic}."
# prompt_template = ChatPromptTemplate.from_template(template)

# print("-----Prompt from Template-----")
# prompt = prompt_template.invoke({"topic": "cats"})
# print(prompt)

# part 2: prompt with multiple placeholders

# template_multiple = """You are a helpful assistant.
# Human: Tell me a {adjective} story about a {animal}.
# Assistant:"""

# prompt_multiple = ChatPromptTemplate.from_template(template_multiple)
# prompt = prompt_multiple.invoke({"adjective": "funny", "animal":"Dog"})
# print("-----Prompt with multiple placeholders-----")
# print(prompt)

# part 3: prompt with system and human messages (using tuples)
messages = [
    ("system", "you are a comedian who tells jokes about {topic}."),#tuple format
    ("human", "tell me {joke_count} jokes."),
]

prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "lawyers", "joke_count": 3})
print("\n -----Propmpt with system and human messages(Tuple)-----\n")
print(prompt)

