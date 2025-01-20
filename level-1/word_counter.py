import re

f = open("python-nuggets\level-1\word_counter.txt")
content = f.read()
words = re.findall(r'\b\w+\b', content)
print(words)
word_count = len(words)

print(f"Total words: {word_count}")
f.close()