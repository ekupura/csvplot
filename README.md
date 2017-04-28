# csvplot
CSVデータをグラフにプロットする低機能cilクライアントツール

## Setting
```
  pip3 install -r requirements.txt
```
で必要なパッケージをすべてインストールしましょう

## Options
|モード|効果|
|--------|---|
|plot    |グラフを描画し保存するモード|

|オプション|効果|備考|
|-|-|-|
|--input_file|入力CSV名を指定する||
|--output_file|出力画像ファイル名を指定する||
|--xc|X軸として使用するCSV系列を指定する||
|--yc|Y軸として使用するCSV系列を指定する||
|--fontsize|ラベルのフォントサイズを指定する||
|--color|グラフの色を指定する|パラメータはmatplotlib準拠|
|--xmax|描画するX軸の最大値を指定する||
|--xmin|描画するX軸の最小値を指定する||
|--ymax|描画するY軸の最大値を指定する||
|--ymin|描画するY軸の最小値を指定する||   

## Usage
入力CSVの0列目がX軸系列，1列目がY軸系列としてグラフを適当に出力する
```
  python3 csvplot.py plot --input_file input.csv --output_file output.png
```
入力CSVの1列目がX軸系列，3列目がY軸系列としてグラフを適当に出力する
```
  python3 csvplot.py plot --input_file input.csv --output_file output.png --xc 1 --yc 3
  
```
X軸に"foo"，Y軸に"bar"というラベルをつけ，赤色で描画
```
  python3 csvplot.py plot --input_file input.csv --output_file output.png --color r --xlabel foo --ylabel bar
  
```
X軸の範囲が-10〜10，Y軸の範囲が1〜-1として描画
```
  python3 csvplot.py plot --input_file input.csv --output_file output.png --xmax 10 --xmin -10 --ymax 1 --ymin -1
  
```
