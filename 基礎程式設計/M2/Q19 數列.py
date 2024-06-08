# 問題描述： 輸入一個正整數 N，列舉如下數列，直到數字超過 N 為止。 數列一：1 2 4 7 11 16 22 29… 數列二：1 2 2 3 3 3 4 4 4 4 5 5 5 5 5…
# 輸入說明： 輸入一個正整數 N。
# 輸出說明： 輸出數字超過 N 的數列，數字以 tab 間格，最後必須有換行字元。

# 下面為輸出等差數列的程式碼
N = int(input("請輸入一個正整數："))
sequence = []                       # 初始化列表來存儲數列
current_number = 1
for i in range(1, N):
    if i == 1:
        current_sum = 1             # 起始数為1
    else:
        current_sum += (i - 1)      # 從第二個數開始，將 (i - 1) 加到 current_sum 中
    sequence.append(current_sum)    # 將當前數列的和添加到列表中
for num in sequence:
    print(num, end=" ")
print()
# 下面為輸出順序數列的
result = ""
for i in range(1, N + 1):           # 使用 for 迴圈從 1 到 n
    result += (str(i)+' ')* i       # 將數字 i 重複 i 次並添加到結果字符串中，並在每一個數字加一個空格字元
print(result)  