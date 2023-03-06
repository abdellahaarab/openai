import os
import openai

openai.api_key = ""


def generate(prompt):
    # Generate a response
    response =  openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    # Print the response
    print(response["choices"][0]["text"])



prompt = "What is the meaning of life?"
generate(prompt)