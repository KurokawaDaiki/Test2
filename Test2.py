import tkinter as tk #画像読み込みモジュール
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispPhoto(path):
    #画像読み込み
    newImage = PIL.Image.open(path).resize((300,300))
    #そのイメージをラベルに表示
    imageDate=PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image=imageDate)
    imageLabel.image=imageDate

def openFile():
    fpath = fd.askopenfilename()

    if fpath:
        dispPhoto(fpath)

#画面を作る
root = tk.Tk()
root.geometry("500x500")

btn = tk.Button(text="ファイルを開く", command = openFile)
imageLabel = tk.Label()
btn.pack()
imageLabel.pack()
tk.mainloop()
