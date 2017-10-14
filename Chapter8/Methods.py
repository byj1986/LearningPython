def faulty():
    raise Exception('sth went wrong')


def ignore_exception():
    faulty()


def handle_exception():
    try:
        faulty()
    except:
        print 'Error handled'


handle_exception()

ignore_exception()
