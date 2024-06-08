# 問題描述： 讓使用者輸入一正整數 n，判斷並輸出該整數為幾位數與每一位數之總和。 例如：輸入 12345，輸出為 15 (1+2+3+4+5=15)
# 輸入說明： 輸入一正整數 n。
# 輸出說明： 判斷並輸出該整數為幾位數與各位數之和，最後必須有換行字元。
n = int(input("請輸入一串正整數："))                      # 將數字轉換為字串以便計算位數和各位數字
n_str = str(n)                                          # 計算有位數
num_digits = len(n_str)                                 # 計算各位數字之和
sum_of_digits = sum(int(digit) for digit in n_str)
print(f"{num_digits}\n{sum_of_digits}\n")               # 利用格式化輸出結果，最後加上換行字元
