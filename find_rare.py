from collections import Counter

with open(file="input.txt",mode="rt",encoding="utf-8") as f:
	s = list(f.read())
f.close()


for index, val in enumerate(s):
	if val.islower():
		if not s[index -4].isupper() and s[index - 1].isupper() and s[index - 2].isupper() and s[index - 3].isupper() and s[index + 1].isupper() and s[index + 2].isupper() and s[index + 3].isupper() and not s[index + 4].isupper():
			print(val, end="")
	