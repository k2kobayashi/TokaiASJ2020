# 使い方

## ファイルの説明

- ```top.md```
    - HPの上部に表示される内容
    - 手修正により内容を編集
- ```middle.md```
    - HPの中央に表示される内容
    - 発表者の情報やURL
    - ```sheet1.csv```から自動で生成される
- ```bottom.md```
    - HPの下部に表示される内容
    - 手修正により内容を編集する
- ```sheet1.csv```
    - 発表者の情報が記載されたcsv
    - 事前に準備しておく


## 実行方法

- ```README.md```を生成する
    - ```parse_csv.py```により```sheet1.csv```から```middle.md```を生成する
    - ```top.md```, ```middle.md```, ```bottom.md```を```cat```して```README.md```を生成する
    - ```run.sh```を実行すれば上記の処理が行われる
    - repositoryに```README.md```をpushしてHPを更新する

- HPの公開方法
    - github pageを利用
