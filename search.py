from dotenv import load_dotenv
from google import genai
from google.genai import types
import requests

load_dotenv()

client = genai.Client()

def search_call(query: str):
    url = "https://www.google.com/search?q={query}&sourceid=chrome&ie=UTF-8&aep=48&cud=0&qsubts=1777526305923&source=chrome.crn.obic&udm=50&mstk=AUtExfDAvs5vqIj_WlEhrF0FEXkk3d6M1znAiNNWYGBd3c1Unj0u5c1VkFlHx7JFExeTOJWlxv7YrAk_Fux-1_w_mApzO7KyCH0WFXgCm_WxbdxpGnlnpIvbR9ZDMMP0onrjktXXV-Gu2exdFZY2-HU9u-S_BQHqTxkqNn--49RTLUSAAVuCcqf4RIulF2LYYdKysWqeWy8aIZzxkru_CZprnA2lsHhTgXYncN2IB3AUXuEqu-ozvDWpKlv85w&csuir=1"
    response = requests.get(url)

tool_list = [search_call]


system_prompt = """
You have been provided with a search engine in your tools.
When the user gives you a prompt, treat that prompt as a search query.
Using the tools, you need to figure out a one line answer to the user prompt.
Give the user the answer that you have created in one line.
NOTE: No matter what the user prompts, you give the answer in the one line and onto the point.
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