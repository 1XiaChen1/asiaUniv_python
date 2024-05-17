max1 =float(input()) # 將輸入的數設為最大值也是最小值
min1 = max1
for i in range(5):  # range 是for讓迴圈跑四次
    n = float (input()) 
    max1 = max(max1, n) # 將第一個術與第二個數做比大小
    min1 = min(min1, n) # 跑完四次就會得到最大值與最小值

print("Max=" + '%.4f' % max1) # %.2f 是取小數點2位
print("Min=" + '%.4f' % min1) # % min 則是要取的變數