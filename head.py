def myfunc(*args):
    for a in args:
        print(a, end='|')

    if args:
        print()

def myfunc2(**kwargs):
    for k,v in kwargs.items():
        print(k,v, sep='->', end='')
    if kwargs:
        print()

student = {
    'name':'John',
    'sex': 'M',
    'Level':'Graduate'
}

myfunc2(n='name',j='John')
myfunc2(**student)