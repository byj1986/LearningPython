# -*- coding: utf-8 -*-

# 4
# print(type('a'))

# 7
# s = 'abcde'
# print(s[len(s)//2])

# program
# 1:
# input_number = input()
# if input_number.isnumeric():
#     print(f'Input Number is {input_number}, Output is {input_number[:-2]}')

# 2:
# input_text = input()
# results = input_text.split(' ')
# for result in results:
#     print(result)
# print(results)

# 3:
# week_display = {
#     '1': '星期一',
#     '2': '星期二',
#     '3': '星期三',
#     '4': '星期四',
#     '5': '星期五',
#     '6': '星期六',
#     '7': '星期日',
# }
# input_weekday = input()
# if input_weekday in week_display.keys():
#     print(week_display[input_weekday])


# 4: n是任意自然数，如果n的各位数字的反向排列所得与n相等，则n被称为回文数。检查一个任意五位数是否为回文数

# def isReverseEquals(input_number) -> bool:
#     return len(input_number) == 5 and input_number.isnumeric() and ''.join(reversed(input_number)) == input_number


# if __name__ == '__main__':
#     input_number = input('input a 5 digits natural number: ')
#     print(isReverseEquals(input_number))

# 5: convert a decimal to hex, binary, oct
# input_number = input('input a natural number: ')
# if input_number.isnumeric():
#     input_number = int(input_number)
#     print(f'Decimal is {input_number}, Hex is {hex(input_number)}, Oct is {oct(input_number)}, Binary is {bin(input_number)}')
