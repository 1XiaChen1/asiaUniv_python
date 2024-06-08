# 問題描述： 印出邊長和小於等於 n 的所有可能的直角三角形三邊長。
# 輸入說明： 輸入一正整數 n。
# 輸出說明： 輸出邊長和小於等於 n 的所有可能的直角三角形三邊長，三邊邊長以 tab 間格，最後必須有換行字元。
n = int(input("請輸入一正整數："))
for a in range(1, n):               # 尋找所有可能的三邊長 a, b, c
    for b in range(a, n):           # 保證 b >= a
        for c in range(b, n):       # 保證 c >= b
            if a * a + b * b == c * c and a + b + c <= n:
                print(f"{a}\t{b}\t{c}")
print()