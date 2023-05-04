# A program intended to save ChatGPT responses from clipboard.

import pyperclip

clip = pyperclip.paste()

with open("responses.txt", "a") as file:
    file.write("\n\n---------- \n\n")
    file.write(clip)
print("Success.")