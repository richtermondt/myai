from openai import OpenAI

import os

def chat(message):
    client = OpenAI()
    messages = [ {"role": "system", "content": 
                  "You are a intelligent assistant."} ]
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
        reply = chat.choices[0].message.content
        print(f"ChatGPT: {reply}")
        return reply
        messages.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    while True:
        message = input("User : ")
        chat(message)





