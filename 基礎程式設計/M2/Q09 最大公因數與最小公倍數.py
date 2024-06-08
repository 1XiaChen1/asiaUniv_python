# 問題描述： 給定二個正整數，求其最大公因數與最小公倍數。  LCM(a,b)=(a∗b)/GCD(a,b)
# 輸入說明： 給定二個正整數。
# 輸出說明： 輸出最大公因數與最小公倍數，最後必須有換行字元。
x, y = map(int, input("請輸入兩個整數(以空格隔開)：").split())      # map是將多筆數值導入Function，int表示整數型態，在input後面加一個split就可以將輸入多筆數值用空格來切割
a = max(x, y)
b = min(x, y)
while a % b > 0:
    tmp = a % b
    a = b
    b = tmp
print (b)
print (int((x * y) / b))