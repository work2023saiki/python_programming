"""デコレーター"""
def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

#@print_more
def add_num(a, b):
    return a + b

f =print_more(add_num)
r = f(10, 20)

#r = add_num(10, 20)
print(r)
