# An interactive prompt for OpenAI that saves your prompts and responses to a log.

import openai, datetime
openai.api_key = "YOUR KEY HERE"

dt = datetime.datetime.now()
prompt = input("PROMPT: ")

response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=2000, temperature = 0.5)
with open("responses.txt", "a") as file:
    file.write(dt.strftime("\n" + "%Y-%m-%d::%H-%M") + " Prompt: " + prompt + "\n" + "Response: " + response.choices[0].text + "\n")

print("\n" + response.choices[0].text)
