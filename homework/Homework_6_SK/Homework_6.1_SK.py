# Задание 1

text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')

words = text.split()
fin_text = []
for word in words:
    if word[-1] in '.,':
        fin_word = word[:-1] + 'ing' + word[-1]
    else:
        fin_word = word + 'ing'
    fin_text.append(fin_word)

fin_texts = ' '.join(fin_text)

print(fin_texts)
