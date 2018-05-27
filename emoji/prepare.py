with open("emoji/parsed_emojis") as f:
    for line in f:
        print(line.split(maxsplit=1)[1].strip())