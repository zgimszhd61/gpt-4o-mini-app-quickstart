from openai import OpenAI
client = OpenAI(api_key="sk-",)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "你是一个有用的AI助手"},
    {"role": "user", "content": "用不超过10个字回答，你是谁"}
  ]
)

print(completion.choices[0].message.content)