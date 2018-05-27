import re

with open("emoji-test.txt") as f:
	for line in f:
		if line[0] == "#":
			continue
		line = re.split(";|#", line.strip(), maxsplit=2)
		line = [p.strip() for p in line]
		if not line[0]:
			continue
		codepoints, status, description = line
		if status != "fully-qualified":
			continue
		emoji =  ''.join([chr(int(c, base=16)) for c in codepoints.strip().split()])
		description = description.split(maxsplit=1)[1]
		print(emoji, description)