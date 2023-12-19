"""自分自身のメソッドを呼び出す"""
class Person(object):

    def __init__(self, name, name2):
        self.name = name
        self.name2 = name2

    def run(self):
        print('run' * self.name2)

person = Person('Mike', 9)
person.say_something()