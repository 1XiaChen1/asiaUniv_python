# 問題描述： 輸入兩個整數，計算其合、差及乘積。
# 輸入說明： 輸入兩個整數(int)。
# 輸出說明： 輸出兩個整數的合(int)、差(int)及乘積(int)，最後必須有換行字元。
x , y = map(int, input().split())       # map是將多筆數值導入Function，int表示整數型態，在input後面加一個split就可以將輸入多筆數值用空格來切割
print (x + y)
print (x - y)
print (x * y)