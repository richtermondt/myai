from openai import OpenAI
import os

# gets API Key from environment variable OPENAI_API_KEY
client = OpenAI()

messages = [{"role": "system", "content":
             "You are a intelligent assistant."}]
while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )

    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=True,
    )
    for chunk in stream:
        if not chunk.choices:
            continue
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")

    print()
