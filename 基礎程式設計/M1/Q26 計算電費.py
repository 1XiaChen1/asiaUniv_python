# 問題描述： 輸入所使用的度數，換算夏月及非夏月之電費金額
# 每度(元):	夏月:	非夏月:
# 120 度以下部分	2.10	2.10
# 121-330 度部分	3.02	2.68
# 331-500 度部分	4.39	3.61
# 501-700 度部分	4.97	4.01
# 701 度以上部分	5.63	4.50
# 輸入說明： 使用的電力度數(int)。
# 輸出說明： 夏月與非夏月的金額(float)，請輸出至小數點後兩位，最後必須有換行字元。
def summer_bill(units):         # 計算夏季電費的函式
    if units <= 120:
        return units * 2.10
    elif units <= 330:
        return 120 * 2.10 + (units - 120 ) * 3.02
    elif units <= 500:
        return 120 * 2.10 + 210 * 3.02 + (units - 330 ) * 4.39
    elif units <= 700:
        return 120 * 2.10 + 210 * 3.02 + 170 * 4.39 + (units - 500 )* 4.97
    else:
        return 120 * 2.10 + 210 * 3.02 + 170 * 4.39 + 200 * 4.97 + (units - 700 )* 5.63

def nosummer_bill(units):       # 計算非夏季電費的函式
    if units <= 120:
        return units * 2.10
    elif units <= 330:
        return 120 * 2.10 + (units - 120 ) * 2.68
    elif units <= 500:
        return 120 * 2.10 + 210 * 2.68 + (units - 330 ) * 3.61
    elif units <= 700:
        return 120 * 2.10 + 210 * 2.68 + 170 * 3.61 + (units - 500 )* 4.01
    else:
        return 120 * 2.10 + 210 * 2.68 + 170 * 3.61 + 200 * 4.01 + (units - 700 )* 4.50

units = int(input("請輸入使用的度數："))
sb = summer_bill(units)         # 將夏季涵式導入變數
nosb = nosummer_bill(units)     # 將非夏季涵式導入變數
print(f"{sb:.2f}")              # 格式化輸出保留小數第二位
print(f"{nosb:.2f}")