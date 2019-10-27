def print_params(*params):
    '''Variable parameters'''
    print(params)


def print_params2(**params):
    '''Variable parameters'''
    print(params)


print_params('Testing')

print_params('x:1', 'y:2', 'z:3')


def with_stars(**kwds):
    print(kwds['name'], 'is', kwds['age'], 'years old')


def without_stars(kwds):
    print(kwds['name'], 'is', kwds['age'], 'years old')


args = {'name': 'Bao', 'age': 31}
with_stars(**args)

without_stars(args)


def story(**kwds):
    return 'Once upon a time, there was a %(job)s called %(name)s.' % kwds


print(story(job='king', name='Bob'))

# print(story(job='Other', name='Mike'))

python = {'job': 'language', 'name': 'Python'}

print(story(**python))

del python['job']

print(story(job='stroke of genius', **python))


def power(x, y, *others):
    if others:
        print('Received redundant parameters', others)
    return pow(x, y)


print(power(3, 2))
print(power(x=3, y=2))

print(power(2, 3))
print(power(y=3, x=2))

nums = (5,) * 3
print(nums)

print(type(nums))

print(power(*nums))

print(power(3, 3, 'Hello World'))

print


def interval(start, stop=None, step=1):
    '''Imitates range() fro step > 0'''
    if stop is None:
        start, stop = 0, start
    results = []
    i = start

    while i < stop:
        results.append(i)
        i += step
    return results


print(interval(10))

print(interval(3, 8, 2))

print(interval(10, step=2))

print(interval(10, 12))

print(power(*interval(3, 8, 2)))

print(interval(3, 8))

print(power(*interval(3, 8)))

print(power(3, 8))
