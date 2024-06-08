# 問題描述： 設計一個程式，讓使用者輸入一個正整數，並將該數字反轉印出，如輸入：12345，輸出：54321。
# 輸入說明： 輸入一正整數 n。
# 輸出說明： 將輸入數字反轉印出，最後必須有換行字元。
n = int(input("請輸入一個正整數："))
reversed_number = str(n)[::-1]      # 使用切片操作 [::-1] 將字串反轉，得到反轉後的數字字串
print(reversed_number)
