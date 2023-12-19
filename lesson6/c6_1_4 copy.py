"""初期化処理"""
class Person(object):
    def __init__(self, name, name2):
        self.name = name
        self.name2 = name2
        print(name+name2)
    
person = Person(8, 2)