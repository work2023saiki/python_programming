import tkinter as tk   #デスクトップアプリ作成のため
import random as rd    #問題の選択、文字列のシャッフルに使用
a = ["ふくやままさはる", "すだまさき", "あらがきゆい", "あやせはるか", "まつもとひとし", "いしはらさとみ","しむらけん"]  #問題に出す元々の文字列
fnt = ("Times New Roman", 20)    #文字のフォント設定
  
def riset1(): #正解して問題を変える処理 
  global lb
  lb2.destroy() #「正解」ラベルを削除
  lb.destroy()  #「人名」ラベルを削除
  entry.delete(0, tk.END)
  q_make()     #問題を作る関数を呼び出す
  lb = tk.Label(frame, text=list2, font=fnt)     #「人名」ラベルを設定
  lb.pack(side="top", pady=20)    #「人名」ラベルを設置

def riset2(): #不正解のときの処理
  lb2.destroy()  #「不正解」のラベルを削除
def test(e):
  print(e.keysym)
def info(e):
  global lb2
  if e.keysym == "Return":
    if ans == b:     #正解だったら
      lb2 = tk.Label(frame, text="正解!!", font=fnt)     #ラベルをフレーム上に配置
      lb2.pack(side="bottom")
      root.after(1500, riset1)
    else: #不正解だったら
      lb2 = tk.Label(frame, text="不正解", font=fnt)     #ラベルをフレーム上に配置
      lb2.pack(side="bottom")
      root.after(1500, riset2)

def q_make():
  global b, c, list2 
  b = rd.choice(a)     #問題に出す文字列を選択
  c = b               #cは問題作成、bは正解一致判定に使用
  list2 =list(c)       #文字列bを１文字ずつリストlist2に格納する
  rd.shuffle(list2)    #リストの要素の順番をシャッフルする   

q_make()
root = tk.Tk()       #Tkオブジェクトを作成
root.geometry("600x300")  #横600,縦400のウィンドウ
root.title("文字当てゲーム")    #タイトル設定

frame = tk.Frame(root, pady=20, padx=5)    #フレーム設定。padyは上端と下端からそれぞれ20px分離している
frame.pack()      #フレーム配置
lb = tk.Label(frame, text=list2, font=fnt)     #人名ラベルをフレーム上に配置
lb.pack(side="top", pady=20)                             #ラベル配置

entry = tk.Entry(frame, font=fnt)       #入力欄をフレーム上に配置
entry.focus_set()     #入力欄のカーソルを最初から表示
entry.pack(side="bottom")     #入力欄の配置
root.bind("<KeyPress>", test)


root.mainloop()    #実行