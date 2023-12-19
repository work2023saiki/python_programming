"""ファイルを用意する"""
s = """おはよう
こんにちはこんばんは"""


with open('test2.txt', 'w') as f:
    f.write(s)