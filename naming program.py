words = []

while True:
    word = input()
    if word == 'end':
        break
    word = word.split()
    ind = 0
    for i in word:
        word[ind] = i.lower()
        ind += 1
    word = '_'.join(word)
    words.append(word)

for i in words:
    print(i)
