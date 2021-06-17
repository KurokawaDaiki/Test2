#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk#ウィンドウを表示するモジュール


# In[ ]:


import tkinter.filedialog as fd#ファイルダイアログを使うモジュール


# In[ ]:


import PIL.Image#画像を扱うモジュール


# In[ ]:


import PIL.ImageTk#tkinterで作った画像上に画像を表示させるモジュール


# 機械学習で使うモジュール↓

# In[5]:


import sklearn.datasets#手書き文字を学習して識別


# In[6]:


import sklearn.svm#


# In[7]:


import numpy#数値計算　配列など


# 画像ファイル数値リストに変換する

# In[8]:


def imageToData(filename):
    grayImage = PIL.Image.open(filename).convert("L")#グレースケールにして
    grayImage = grayImage.resize((8,8),(PIL.Image.ANTIALIAS)) #8x8にして画質をきれいにする
    #その画像を表示する
    dispImage = PIL.ImageTk.PhotoImage(grayImage.resize((300,300))) #PIL.ImageTk.PhotoImage(新たに300x300の画面を作成)
    imageLabel.configure(image=dispImage) #画像データを設定？
    imageLabel.image = dispImage #画像を結び付けておくため。消されないための決まり事
    #数値リストに変換
    numImage = numpy.asarray(grayImage, dtype = float) ##asarray(配列のもとになるオブジェクト,配列の型指定)
    numImage = numpy.floor(16-16*(numImage/256)) #floor(数字)　切り捨てで代入
    numImage = numImage.flatten() #flatten() 一次元配列に変換
    return numImage


# 数字を予測する

# In[9]:


def predictDigits(data):
    #学習用データを読込む 手書きデータを読み込む際に使う
    digits = sklearn.datasets.load_digits()
    #機械学習する
    clf = sklearn.svm.SVC(gamma = 0.001)
    clf.fit(digits.data, digits.target)
    #予測結果を表示する
    n = clf.predict([data])
    textLabel.configure(text = "この画像は"+str(n)+"です")


# ファイルダイアログ作成

# In[10]:


#ファイルダイアログを開く
def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        #画像ファイルを数値リストに変換する
        data = imageToData(fpath)
        predictDigits(data)


# In[11]:


#アプリウィンドウを作る
root = tk.Tk() #最初にウィンドウを作る


# In[12]:


root.title("タイトルつけてみた") #rootで作ったウィンドウにタイトルを付けられる


# In[13]:


root.geometry("400x1000")#400x400でrootウィンドウを作る。


# In[14]:


btn = tk.Button(root, text="ファイルを開く", command = openFile)#rootのウィンドウにファイルを開くボタンを設置, コマンドで関数を持ってくる


# In[15]:


imageLabel = tk.Label()#？？？？


# In[16]:


btn.pack()#ボタンの機能を使う


# In[17]:


imageLabel.pack()#imageLabelの機能を使う


# In[18]:


textLabel = tk.Label(text="手書きの数字を認識します") #textLabel変数にtk.Labelを代入


# In[19]:


textLabel.pack()#textLabel機能を使う


# In[20]:


tk.mainloop()#最後にループ

