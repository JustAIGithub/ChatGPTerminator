import openai
from rich import print, inspect
import tomllib
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def complete_chat(prompt: str,chat_history: list[dict]) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= chat_history + {"role": "user", "content": prompt}
    )
    # return response
    return response['choices'][0]['message']['content']

with open("config.toml", "rb") as f:
    config = tomllib.load(f)

welcome_ascii = '''
   _____ _____ _______                  _             _             
  / ____|  __ \__   __|                (_)           | |            
 | |  __| |__) | | | ___ _ __ _ __ ___  _ _ __   __ _| |_ ___  _ __ 
 | | |_ |  ___/  | |/ _ \ '__| '_ ` _ \| | '_ \ / _` | __/ _ \| '__|
 | |__| | |      | |  __/ |  | | | | | | | | | | (_| | || (_) | |   
  \_____|_|      |_|\___|_|  |_| |_| |_|_|_| |_|\__,_|\__\___/|_|   
'''
print(f"[bold green]{welcome_ascii}[/bold green]")
print(f"[dark-green]Model: {config['model']}[/dark-green]")
