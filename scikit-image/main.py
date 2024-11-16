import cv2
import pytesseract
import os
from pathlib import Path
from skimage import io, filters, morphology


def extractDay(file_path):

    # 画像を読み込む
    img = io.imread(file_path)

    # グレースケール化
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 二値化
    thresh = filters.threshold_otsu(gray)
    binary = gray > thresh

    # 輪郭検出
    canny_img = cv2.Canny(gray, 50, 110)
    # OCRでテキストに変換
    text = pytesseract.image_to_string(canny_img, lang='jpn')  # 日本語の場合
    print(text)


# 処理したいディレクトリのパス
directory = "../sample"
# ディレクトリをPathオブジェクトで表現
path = Path(directory)

# ディレクトリ内のファイルを取得し、処理
for file in path.iterdir():
    if file.is_file():
        # 処理内容
        with open(file, 'r') as f:
            print(file)
            extractDay(f.name)
