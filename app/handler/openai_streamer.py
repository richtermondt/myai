from openai import OpenAI

from app.models import create_post

class OpenAIStreamer:
    def __init__(self):
        self.messages = [{"role": "system", "content": "You are a intelligent assistant."}]
        self.client = OpenAI()

    def chat(self, message):
        if message:
            collected_chunks = []
            self.messages.append({"role": "user", "content": message})
            stream = self.client.chat.completions.create(
                model="gpt-3.5-turbo", 
                messages=self.messages, 
                stream=True
            )
            for chunk in stream:
                if not chunk.choices:
                    continue
                if chunk.choices[0].delta.content is not None:
                    collected_chunks.append(chunk.choices[0].delta.content)
                    yield(chunk.choices[0].delta.content)
                    #print(chunk.choices[0].delta.content, end="")
            #print()
        collected_string = ''.join(collected_chunks)
        post = create_post(message, collected_string)

if __name__ == "__main__":
    openai_streamer = OpenAIStreamer()
    while True:
        message = input("User : ")
        if message:
            openai_streamer.chat(message)
