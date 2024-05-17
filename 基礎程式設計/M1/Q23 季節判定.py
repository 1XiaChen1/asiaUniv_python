# 問題描述： 試撰寫一程式，可輸入月份，然後判斷其所屬的季節 3 ~ 5 月為春季，6 ~ 8 月為夏季， 9 ~ 11 月為秋季， 12 ~ 2 月為冬季。
# 輸入說明： 輸入月份(int)。
# 輸出說明： 輸出該月份的季節(String)， 3 ~ 5 月為春季(Spring)， 6 ~ 8 月為夏季(Summer)， 9 ~ 11 月為秋季(Autumn)，12 ~ 2 月為冬季(Winter)，最後必須有換行字元。
month = int(input("請輸入月份："))
if 3 <= month <= 5:
    season = "春季(Spring)"
elif 6 <= month <= 8:
    season = "夏季(Summer)"
elif 9 <= month <= 11:
    season = "秋季(Autumu)"
elif month == 12 or month == 1 or month == 2:
    season = "冬季(Winter)"
else:
    season = "無效的月份" 

print (season)