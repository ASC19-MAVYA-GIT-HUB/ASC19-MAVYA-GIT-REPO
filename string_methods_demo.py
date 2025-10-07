text = "  Python is Powerful  "

print(text[0])  # Indexing: ' '
print('Python' in text)  # Membership: True
print(len(text))  # Length: 23
print(text.find("is"))  # find(): 9
print(text == "Python is Powerful")  # Equality: False
print(text.lower() == "python is powerful")  # Case-insensitive equality: True
print("-".join(["Python", "is", "fun"]))  # join(): Python-is-fun
print(text.rfind("P"))  # rfind(): 17
print(text[2:8])  # Slicing: 'Python'
print(text.lower())  # lower(): '  python is powerful  '
print(text.upper())  # upper(): '  PYTHON IS POWERFUL  '
print(text.strip())  # strip(): 'Python is Powerful'