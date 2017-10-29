for n in range(100):
    a = float(n)
    b = a / 2
    c = a // 2
    print "n is %d, n/2 is %.2f, n//2 is %.2f, n/2 equals n//2 %s" % (a, b, c, b == c)
