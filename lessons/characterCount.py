message = 'It was a bright cold day in april, and the clocks were stricking thirteen'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

print(count)