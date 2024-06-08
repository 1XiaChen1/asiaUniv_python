# 問題描述： 資源回收是一種美德，商店老闆想出一種鼓勵的方式：三個空罐可以換一罐新的。假設你有 N 罐汽水，試利用程式解出你最後可以喝到幾罐汽水？
# 輸入說明： 輸入一正整數 N。
# 輸出說明： 最多可以喝到的汽水數量，最後必須有換行字元。
def calculate_sodas(N):
    total_sodas = N
    empty_cans = N

    while empty_cans >= 3:
        new_sodas = empty_cans // 3
        total_sodas += new_sodas
        empty_cans = empty_cans % 3 + new_sodas

    return total_sodas

N = int(input("請輸入一個正整數："))
print(calculate_sodas(N))
