# 問題描述： 輸入一個字元，轉換其大小寫輸出 (大寫 ->小寫，小寫->大寫)。
# 輸入說明： 輸入一個字元 (char)。
# 輸出說明： 將輸入轉換其大小寫輸出，最後必須有換行字元。
char = input("請輸入一個字元：")
if char.isupper():              #.isupper()檢查字符串中所有的字母是否都為大寫。
    result = char.lower()       #利用.lower()將大寫全部改為小寫
elif char.islower():            #.islower()檢查字符串中所有的字母是否都為小寫。
    result = char.upper()       #利用.upper()將小寫全部改為大寫
else:
    result = char
print(result)
