"""キーワード引数の辞書化"""
def menu(**fumis):
    for k, v in fumis.items():
        print(k, v)

menu(entree='beef', drink='coffee')