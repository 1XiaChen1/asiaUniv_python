# 問題描述： 使用者輸入一正整數 n，找出小於等於 n 中，其質因數只有 2 或 3 或 5 的數字總和。
# 輸入說明： 輸入一正整數 n。
# 輸出說明： 找出小於等於 n 中，其質因數只有 2 或 3 或 5 的數字總和，最後必須有換行字
def is_special_number(num):
    while num % 2 == 0:
        num //= 2
    while num % 3 == 0:
        num //= 3
    while num % 5 == 0:
        num //= 5
    return num == 1

def sum_special_numbers(n):
    total = 0
    for i in range(1, n + 1):
        if is_special_number(i):
            total += i
    return total

n = int(input("請輸入一個正整數："))

# 輸出符合條件的數字總和
print(sum_special_numbers(n))
