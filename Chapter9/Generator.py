nested = [[1, 2], [3, 4], [5]]
print nested


def flatten(n):
    for sublist in n:
        for element in sublist:
            yield element


for num in flatten(nested):
    print num
