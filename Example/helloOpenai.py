from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "you are a cheerful assistant."},
    {"role": "user", "content": "APIのテストです、なにか言ってみてください"}
  ]
)

print(completion.choices[0].message)
print(completion.choices[0].message.content)