# text = sys.stdin.read()
# byj19@DESKTOP-KTH31QC /cygdrive/c/Projects/Python/LearningPython/Chapter11
# $ cat sometext.txt | python wordcount.py
# WordCount:  13

text = 'hello, world!\nYour mother was a hamster and your father smelled of elderberries.'
words = text.split()
wordcount = len(words)
print 'WordCount: ', wordcount
