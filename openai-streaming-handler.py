from openai import OpenAI
import os

class OpenAIStreamer:
    def __init__(self):
        self.messages = [{"role": "system", "content": "You are a intelligent assistant."}]
        self.client = OpenAI()

    def chat(self, message):
        if message:
            self.messages.append({"role": "user", "content": message})
            stream = self.client.chat.completions.create(model="gpt-3.5-turbo", messages=self.messages, stream=True)
            for chunk in stream:
                if not chunk.choices:
                    continue
                if chunk.choices[0].delta.content is not None:
                    print(chunk.choices[0].delta.content, end="")
            print()

def main():
    openai_streamer = OpenAIStreamer()
    while True:
        message = input("User : ")
        if message:
            openai_streamer.chat(message)
