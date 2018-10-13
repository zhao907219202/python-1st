sentence = input("Sentence:")

screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
margin = (screen_width - box_width) // 2

print(' ' * margin + '+' + '-' * (box_width - 2) + '+')
print(' ' * margin + '| ' + ' ' * (text_width + 2) + ' |')
print(' ' * margin + '|  ' + sentence + '  |')
print(' ' * margin + '| ' + ' ' * (text_width + 2) + ' |')
print(' ' * margin + '+' + '-' * (box_width - 2) + '+')
