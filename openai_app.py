from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo")

result = model.invoke("What is a car?")
print("Result: ")
print(result)
print("Content only:")
print(result.content)