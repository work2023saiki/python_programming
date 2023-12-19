"""関数内でグローバル変数に値を入れる"""
ANIMAL = 'cat'

def f():
    print(ANIMAL)
    animal = 'dog'
    print('after:', animal)

f()