import re
text = "Hello, world!"
match = re.search("world", text)
print(match.group())  # Output: world