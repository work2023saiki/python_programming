"""位置引数のタプル化"""
def say_something(neko,*fumi):
    print ('にゃん＝',neko)
    for fff in fumi:
        print(fff)

say_something('ねこ','ひげまんじゅう', '肉球', 'ねこパンチ','いかみみ')