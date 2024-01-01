from openai import OpenAI
import configparser
config = configparser.ConfigParser()
config.read('C:/GitHub/projectCathy/env2/main/config.ini')
keybox = config['DEFAULT']['OPENAI_API_KEY']
client = OpenAI()
print(client)
print(config['DEFAULT']['OPENAI_API_KEY'])
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "you are a cheerful assistant."},
    {"role": "user", "content": "aZling4"}
  ]
)

print(completion.choices[0].message)