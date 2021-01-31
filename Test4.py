import tkinter as tk #画像読み込みモジュール
import random

#画面を作る
root = tk.Tk()
root.geometry("500x500")

def Disp():
    kuji = ["ガレン","オリアナ","アニー"]
    lbl.configure(text = random.choice(kuji))
lbl = tk.Label(text = "")
btn = tk.Button(text = "ぼたん！", command = Disp)

lbl.pack()
btn.pack()
tk.mainloop()
