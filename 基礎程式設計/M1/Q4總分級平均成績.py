# 問題描述： 輸入國文、英文和數學成績，計算其總分數及平均成績。
# 輸入說明： 輸入國文(int)、英文(int)和數學(int)成績。
# 輸出說明： 輸出總分數及四捨五入後的平均成績(int)，最後必須有換行字元。
x ,y ,z = map(int ,input().split())     # map是將多筆數值導入Function，int表示整數型態，在input後面加一個split就可以將輸入多筆數值用空格來切割
tot = x + y + z
avg = tot / 3.0
print (tot)
print ('%.0f' % avg)                    # %.0f 就是四捨五入取整數，% 變數代表輸出的數為浮點數