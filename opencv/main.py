import cv2
import pytesseract
import os
from pathlib import Path

def extractDay(file_path):
   # 画像を読み込む
    img = cv2.imread(file_path)

    # グレースケールに変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray, lang='jpn')  # 日本語の場合
    print('gray scaled')
    print(text)

    # 二値化 (適宜閾値を調整)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    text = pytesseract.image_to_string(thresh, lang='jpn')  # 日本語の場合
    print('threshold')
    print(text)

    # 輪郭検出 (必要に応じて)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 輪郭から最小の外接矩形を取得し、その部分の画像を切り出す
    print('boundingRect')
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        roi = thresh[y:y+h, x:x+w]

        # OCRでテキストに変換
        text = pytesseract.image_to_string(roi, lang='jpn')  # 日本語の場合
        text = text.replace(' ','')
        if text != '':
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