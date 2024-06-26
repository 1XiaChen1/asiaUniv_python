# 問題描述： 寫一個程式來找出輸入的 5 個數字的最大值和最小值，數值不限定為整數，且值可存放於 float 型態數值內。
# 輸入說明： 輸入5個數字
# 輸出說明： 輸出數列中的最大值與最小值，輸出時需附上小數點後兩位數字，最後必須有換行字元
max1 =float(input("請輸入五個數(用enter隔開)："))       # 將輸入的數設為最大值也是最小值
min1 = max1
for i in range(4):                                    # range 是for讓迴圈跑四次，如果要輸入五六個數就改成5依此類推
    n = float (input("請輸入五個數(用enter隔開)：")) 
    max1 = max(max1, n)                               # 將第一個術與第二個數做比大小
    min1 = min(min1, n)                               # 跑完四次就會得到最大值與最小值

print("Max=" + '%.2f' % max1)                         # %.2f 是取小數點2位
print("Min=" + '%.2f' % min1)                         # % min 則是要取的變數
# 此程式用於輸入以Enter隔開的題型