import fileinput

for line in fileinput.input(inplace=False):
    line = line.rstrip()
    num = fileinput.lineno()
    '''asdfasdfasdf'''
    print(line)
    # print '%-80s # %2i' % (line, num)
