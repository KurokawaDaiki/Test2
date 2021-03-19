import sklearn.datasets
import sklearn.svm
import PIL.Image
import numpy

#画像ファイルを数値リストに変換
def imageToData(filename):
    #ファイルを開いてグレースケールにする。
    grayImage = PIL.Image.open(filename).convert("L")
    #8x8(モザイク)に直し、アンチエイリアス(画像をきれいにする)
    grayImage = grayImage.resize((8,8),PIL.Image.ANTIALIAS)
    #asarray(配列のもとになるオブジェクト,配列の型指定)
    numImage = numpy.asarray(grayImage, dtype = float)
    print(numImage)
    #結果↓
    """
[[255. 255. 255. 243. 255. 255. 255. 255.]
 [254. 234. 128. 102. 120. 235. 254. 254.]
 [255. 220. 171. 246. 141. 102. 255. 252.]
 [255. 255. 255. 236.  73. 137. 253. 252.]
 [253. 255. 220.  57. 139. 255. 255. 255.]
 [254. 218.  29.  96. 206. 183. 214. 255.]
 [255. 205.  72.  88.  78.  66. 130. 255.]
 [255. 255. 255. 255. 255. 255. 255. 255.]]
     """
    #floor(数字)　切り捨てで代入
    numImage = numpy.floor(16 - 16 * (numImage / 256))
    print(numImage)
    #結果↓
    """
[[ 0.  0.  0.  0.  0.  0.  0.  0.]
[ 0.  1.  8.  9.  8.  1.  0.  0.]
 [ 0.  2.  5.  0.  7.  9.  0.  0.]
 [ 0.  0.  0.  1. 11.  7.  0.  0.]
 [ 0.  0.  2. 12.  7.  0.  0.  0.]
 [ 0.  2. 14. 10.  3.  4.  2.  0.]
 [ 0.  3. 11. 10. 11. 11.  7.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.  0.]]
     """
    #flatten() 一次元配列に変換
    numImage = numImage.flatten()
    print(numImage)
    #結果↓
    """
    [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  1.  8.  9.  8.  1.  0.  0.  0.  2.
  5.  0.  7.  9.  0.  0.  0.  0.  0.  1. 11.  7.  0.  0.  0.  0.  2. 12.
  7.  0.  0.  0.  0.  2. 14. 10.  3.  4.  2.  0.  0.  3. 11. 10. 11. 11.
  7.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
    """
    #(filename)にnumImageを返す。
    return numImage


def predictDigits(data):
    #学習用データを読み込む。　手書き数字読み込む際に使う
    digits = sklearn.datasets.load_digits()
    #学習の準備をする
    clf = sklearn.svm.SVC(gamma = 0.001)
    #
    clf.fit(digits.data, digits.target)
    #数字を渡してなんの数字か予測する
    n=clf.predict([data])
    print("予測=", n)
#画像は直接渡せないから0～16の濃淡でできた一列の数値リストを渡す。
data = imageToData("2.png")
#関数を実行
predictDigits(data)
