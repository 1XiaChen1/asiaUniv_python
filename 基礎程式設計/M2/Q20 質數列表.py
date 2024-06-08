# 問題描述： 讓使用者輸入一正整數 n，並輸出小於 n 的所有質數。
# 輸入說明： 輸入一正整數 n。
# 輸出說明： 輸出小於 n 的所有質數 (1 不是質數)，最後必須有換行字元。

def is_prime(num):                      # 檢查數字是否為質數
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("請輸入一個正整數："))
primes = []
for num in range(2, n):                 # 找出小於 n 的所有質數
    if is_prime(num):
        primes.append(num)
result = '\n'.join(map(str, primes))    # 將質數列表轉換為字串，並用空格連接
print(result)
