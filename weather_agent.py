from dotenv import load_dotenv
from google import genai
import requests
from google.genai import types

load_dotenv()

client = genai.Client()

def get_weather(city: str):
    url = ""
    response = requests.get(url)

tool_list = [get_weather]

system_prompt = """
You are an AI agent that uses the tool given to you to give the user the weather info of whichever city
the user has asked for. 
If the user has not given any city name and is something else, you respond with "Give a city name !"
"""

user_input = input("Your prompt: ")

response = client.models.generate_content(
    model="gemini-3-flash-preview", 
    contents=user_input,
    config=types.GenerateContentConfig(
        system_instruction=system_prompt,
        tools=tool_list,
    )
)
print(response.text)