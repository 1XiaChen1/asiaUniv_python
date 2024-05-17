# 問題描述： 讀取一四位數，並且依下列方式進行加密
#     以該位數加7後，除以 10 取餘數取代該位數
#     將第一個位數的數字與第三個位數的數字對調
#     將第二個位數的數字與第四個位數的數字對調
# 輸入說明： 輸入一個四位數的字串(String)。
# 輸出說明： 輸出加密後的數字串(String)，最後必須有換行字元。
num = int(input("請輸入四位數："))

num4 = (num%10 + 7)% 10
num = num // 10
print (num, num4)

num3 = (num%10 + 7)% 10
num = num // 10
print (num, num3)

num2 = (num%10 + 7)% 10
num = num // 10
print (num, num2)

num1 = (num%10 + 7)% 10
print (num1)

print(num3 ,num4 ,num1 ,num2 ,sep='')       # `sep` 是 `print` 函式的一個參數，用於指定輸出時的分隔符