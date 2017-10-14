# coding=utf-8

# #Sequence
# edward = ['Edward gumby',42]

# john=['John Smith',50]

# database=[edward,john]

# print database

# print [1,2,3]+[4,5,6]

sequence = [None] * 10
print sequence

sentence = r'He''s a very naughty boy!'
screen_width = 120
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width) // 2
# 结果应该不是书里的格式
# 每一行的开头位置是一样的，' ' * left_margin
print
print ' ' * left_margin + '+' + '-' * (box_width - 2) + '+'
print ' ' * left_margin + '|' + ' ' * text_width + '|'
print ' ' * left_margin + '|' + sentence + '|'
print ' ' * left_margin + '|' + ' ' * text_width + '|'
print ' ' * left_margin + '+' + '-' * (box_width - 2) + '+'
