import sklearn.datasets
import matplotlib.pyplot as plt

#スキットラーンオブジェクト化
digits = sklearn.datasets.load_digits()

for i in range(60):
    plt.subplot(6,10, i+1)  #subplot(行、列,表示回数)
    plt.axis("off")
    plt.title(digits.target[i]) #上に数字を表示()　1～
    plt.imshow(digits.images[i], cmap="hot") #画像データをグレーの濃淡データにする
plt.show()  #作ったがぞうを表示する
