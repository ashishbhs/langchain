from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")


prompt_template =ChatPromptTemplate.from_messages(
    [
        ("system", "you are a comedian who tells jokes about {topic},"),
        ("human","Tell me {joke_count} jokes."),
    ]
)
chain = prompt_template | model | StrOutputParser()

result = chain.invoke({"topic":"lawyers", "joke_count":4})
print(result)