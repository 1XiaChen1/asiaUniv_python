# 問題描述： 輸入一個字元，判斷是大寫或小寫或是其他字元。
# 輸入說明： 輸入一個字元 (char)。
# 輸出說明： 輸出判斷結果(大寫：uppercase、小寫：lowercase、特殊字元：special character)，最後必須有換行字元。
char = input("請輸入一個字元：")
if char.isupper():              #.isupper()檢查字符串中所有的字母是否都為大寫。
    result = "Uppercase"
elif char.islower():            #.islower()檢查字符串中所有的字母是否都為小寫。
    result = "Lowercase"
else:
    result = "Special character"
print (result)