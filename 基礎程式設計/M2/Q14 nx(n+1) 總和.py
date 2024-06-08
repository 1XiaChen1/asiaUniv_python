# 問題描述：讓使用者輸入一正整數 n，計算 1*(1+1) + 2*(2+1) + 3*(3+1) + … + n*(n+1)並輸出結果。
# 輸入說明：輸入一正整數 n。
# 輸出說明：計算 1*(1+1) + 2*(2+1) + 3*(3+1) + … + n*(n+1)並輸出結果，最後必須有換行字元。
n = int(input("請輸入一個正整數："))
count = 0               # 初始化結果變數
for i in range(1, n+1):
    count += i*(i+1)
print (count,"\n")