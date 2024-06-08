# 問題描述： 讓使用者輸入一正整數 n，用迴圈計算 n!數值後輸出。
# 輸入說明： 輸入一正整數 n ( n <= 20 )。
# 輸出說明： 以迴圈計算 n!數值(long)後輸出，最後必須有換行字元。
n = int(input("請輸入一個正整數："))
count = 1
for i in range(1, n+1):
    count *= i
print(count,"\n")