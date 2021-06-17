import sklearn.datasets

#スキットラーンオブジェクト化
digits = sklearn.datasets.load_digits()

#データの個数を表示
print("データの個数=",len(digits.images))
#画像データを表示
print("画像データ=",digits.images[0])
#数字を表示
print("何の数字か=",digits.target[0])
