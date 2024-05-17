# 問題描述： 請寫一個程式讓使用者輸入一個中文字元，程式回傳取得該字元的萬國碼。
# 輸入說明： 輸入一個中文字元 ch (char)。
# 輸出說明： 輸出該字元對應的「萬國碼」(Unicode)值 (int)，最後必須有換行字元。
ch = input("請輸入一個中文數：")
uc = ord(ch)                    # ord將變數轉為ASCII碼
print (uc)
print('%2x'% uc)                # %x是將該數轉為16進制