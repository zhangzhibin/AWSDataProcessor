# About 关于
This a python script for AWS (=Automatic Weather Station) data processing written for my lovely wife.

气象自动站数据处理脚本

# Usage 使用方法
```
python3 readr-1.0.py -i <inputFolder> -o <outputFolder> -t <threshhold> -r <override> -d
```

* "-i", "--input" 数据文件夹

folder for source data

* "-o", "--output" 输出文件夹

folder for output

* "-t", "--threshhold" 输出阈值

threshhold, default: 500

* "-r", "--override" 是否覆盖旧文件，默认True
Value: True or False 

override the output files, default is Ture

* "-d", "--debug" 开启详细日志，调试用

enable debug output

# Example 示例
```
python3 ./readr1-1.0.py  -i ./2019\@aws
======================================================
data folder: ./2019@aws
output folder: ./out
threshhold: 500
override output files: True
Debug mode: False
==== total files or dirs: 45 ====
./2019@aws/AI201905161900.EFZ => 0
./2019@aws/AI201905170400.EFZ => 0
./2019@aws/AI201905172000.EFZ => 0
./2019@aws/AI201905160000.EFZ => 0
./2019@aws/AI201905160200.EFZ => 0
./2019@aws/AI201905170600.EFZ => 0
./2019@aws/AI201905170200.EFZ => 0
./2019@aws/AI201905162200.EFZ => ./out/AI201905162200.EFZ.txt : 4
./2019@aws/AI201905160600.EFZ => 0
./2019@aws/AI201905160400.EFZ => 0
./2019@aws/AI201905171900.EFZ => 0
./2019@aws/AI201905162000.EFZ => 0
./2019@aws/AI201905170000.EFZ => 0
./2019@aws/AI201905160300.EFZ => 0
./2019@aws/AI201905170700.EFZ => 0
./2019@aws/AI201905170500.EFZ => 0
./2019@aws/AI201905161800.EFZ => 0
./2019@aws/AI201905160100.EFZ => 0
./2019@aws/AI201905171800.EFZ => 0
./2019@aws/AI201905160500.EFZ => 0
./2019@aws/AI201905170100.EFZ => 0
./2019@aws/AI201905162100.EFZ => ./out/AI201905162100.EFZ.txt : 1
./2019@aws/AI201905162300.EFZ => 0
./2019@aws/AI201905170300.EFZ => 0
./2019@aws/AI201905160700.EFZ => 0
./2019@aws/AI201905171600.EFZ => 0
./2019@aws/AI201905161200.EFZ => 0
./2019@aws/AI201905161000.EFZ => 0
./2019@aws/AI201905171400.EFZ => 0
./2019@aws/AI201905160900.EFZ => ./out/AI201905160900.EFZ.txt : 2
./2019@aws/AI201905171000.EFZ => ./out/AI201905171000.EFZ.txt : 1
./2019@aws/AI201905170900.EFZ => ./out/AI201905170900.EFZ.txt : 6
./2019@aws/AI201905161400.EFZ => 0
./2019@aws/AI201905161600.EFZ => 0
./2019@aws/AI201905171200.EFZ => 0
./2019@aws/AI201905161100.EFZ => 0
./2019@aws/AI201905160800.EFZ => ./out/AI201905160800.EFZ.txt : 1
./2019@aws/AI201905171500.EFZ => 0
./2019@aws/AI201905171700.EFZ => 0
./2019@aws/AI201905161300.EFZ => 0
./2019@aws/AI201905161700.EFZ => 0
./2019@aws/AI201905171300.EFZ => 0
./2019@aws/AI201905171100.EFZ => 0
./2019@aws/AI201905161500.EFZ => 0
./2019@aws/AI201905170800.EFZ => ./out/AI201905170800.EFZ.txt : 12
total output files: 7
====================== done ==========================
```