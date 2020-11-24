# get text
text = input("Text: ")

# split text
text_split = text.split(" ")

i = 0
for word in text_split:
    if len(word) > 5:
        text_split[i] = text_split[i][0] + text_split[i][1] + '-' + text_split[i][-1] + text_split[i][-2]
    i += 1

print(" ".join(text_split))
