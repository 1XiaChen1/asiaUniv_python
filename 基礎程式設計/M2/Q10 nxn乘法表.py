# 問題描述： 輸出 n×n 乘法表。
# 輸入說明： 輸入一正整數 n。
# 輸出說明： 輸出 n×n 乘法表(0<n<=9)，每個輸出數字皆以 tab 間格，最後必須有換行字元。
n = int(input("請輸入一個正整數："))
for i in range(1, n+1):
    for j in range(1, n+1):
        print (i*j,"",end = "")
    print ()