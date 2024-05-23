# 問題描述： 輸入一正整數，判斷其奇偶數。
# 輸入說明： 輸入一正整數 (int)。
# 輸出說明： 判斷其奇偶數，最後必須有換行字元。
num = int(input("請輸入一個正整數："))
if num % 2 == 0:        # 判斷是否整除二就好
    result = "Even"
else:
    result = "Odd"
print(result)
