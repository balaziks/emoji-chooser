emoji_dict = {}

with open("emoji/parsed_emojis") as f:
    for line in f:
        emoji, description = line.strip().split(maxsplit=1)
        emoji_dict[description] = emoji

print(emoji_dict[input()])