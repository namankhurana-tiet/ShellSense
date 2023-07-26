# from tkinter.ttk import Style
import openai
import os
import api

if "OPENAI_API_KEY" in os.environ:
    print("Using OpenAI")
    openai.api_key = os.environ["OPENAI_API_KEY"]
else:
    print('No openAI API Key found. Please create and set an API key before proceeding')

model_engine = "text-davinci-003"


def get_command_openai(prompt):

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.3,  # lower value of temperature provides similar responses
    )
    return completion.choices[0].text


def get_description_openai(prompt):
    results = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=["\n", "<|endoftext|>"],
        temperature=0.6
    )
    if results:
        return results['answers'][0]


def main(finalstatus, command):
    if finalstatus == 0:
        return
    elif finalstatus == -1:
        pre_prompt = "Write a command to "
    elif finalstatus > 0:
        pre_prompt = "Autocorrect this command: "
    elif finalstatus == -2:
        pre_prompt = "Tell me about this command"

    prompt = pre_prompt + command
    output = ""
    if finalstatus >= -1:
        output = get_command_openai(prompt)
    elif finalstatus == -2:
        output = get_description_openai(prompt)

    return output
