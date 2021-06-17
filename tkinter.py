#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk#ウィンドウを表示するモジュール


# In[2]:


import tkinter.filedialog as fd#ファイルダイアログを使うモジュール


# In[3]:


import PIL.Image#画像を扱うモジュール


# In[4]:


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
    grayImage = grayImage.resize((8,8),(PIL.Image.ANTIALIAS))
    #その画像を表示する
    dispImage = PIL.ImageTk.PhotoImage(grayImage.resize((300,300)))
    imageLabel.configure(image=dispImage)
    imageLabel.image = dispImage
    #数値リストに変換
    numImage = numpy.asarray(grayImage, dtype = float)
    numImage = numpy.floor(16-16*(numImage/256))
    numImage = numImage.flatten()
    return numImage


# 数字を予測する

# In[9]:


def predictDigits(data):
    #学習用データを読込む
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
root = tk.Tk()


# In[12]:


root.geometry("500x500")


# In[13]:


btn = tk.Button(root, text="ファイルを開く", command = openFile)


# In[14]:


imageLabel = tk.Label()


# In[15]:


btn.pack()


# In[16]:


imageLabel.pack()


# In[17]:


textLabel = tk.Label(text="手書きの数字を認識します")


# In[18]:


textLabel.pack()


# In[19]:


tk.mainloop()

