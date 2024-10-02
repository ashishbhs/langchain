from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_google_genai import ChatAnthopic
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
chat_history = []

system_message = SystemMessage(content="You are a helpful AI Assistant.")
chat_history.append(system_message)

while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query))

    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))

    print(f"AI: {response}")

print("--Message History--")
print(chat_history)




