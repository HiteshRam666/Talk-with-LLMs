from dotenv import load_dotenv, find_dotenv
import os 
from langchain_openai import OpenAI

_ = load_dotenv(find_dotenv()) 
openai_api_key = os.environ["OPENAI_API_KEY"]

llmModel = OpenAI()

response = llmModel.invoke("Tell me fun fact about Quantum computers")

# print(response)

for chunk in llmModel.stream("Tell me fun fact about Quantum computers"):
    print(chunk, end = " ", flush=True)