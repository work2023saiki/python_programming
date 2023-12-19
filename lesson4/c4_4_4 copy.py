"""関数内でグローバル変数に値を入れる"""
ANIMAL= 'cat'

def f():
    animal = 'dog'
    print('after:', animal)

f()
print('global:', ANIMAL)