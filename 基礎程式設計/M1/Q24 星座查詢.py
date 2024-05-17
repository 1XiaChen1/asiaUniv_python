# 問題描述： 請設計程式，根據輸入之及日期，輸出對應之星座。
# 1997年 1月 21日 ~ 1997年 2月 18日 水瓶 (Aquarius)
# 1997年 2月 19日 ~ 1997年 3月 20日 雙魚 (Pisces)
# 1997年 3月 21日 ~ 1997年 4月 20日 牡羊 (Aries)
# 1997年 4月 21日 ~ 1997年 5月 21日 金牛 (Taurus)
# 1997年 5月 22日 ~ 1997年 6月 21日 雙子 (Gemini)
# 1997年 6月 22日 ~ 1997年 7月 22日 巨蟹 (Cancer)
# 1997年 7月 23日 ~ 1997年 8月 23日 獅子 (Leo)
# 1997年 8月 24日 ~ 1997年 9月 23日 處女 (Virgo)
# 1997年 9月 24日 ~ 1997年 10月 23日 天秤 (Libra)
# 1997年10月 24日 ~ 1997年 11月 22日 天蠍 (Scorpio)
# 1997年11月 23日 ~ 1997年 12月 21日 射手 (Sagittarius)
# 1997年12月 22日 ~ 1998年 1月 20日 摩羯 (Capricorn)
# 輸入說明： 請輸入月(int)及日期(int)。
# 輸出說明： 依照星座標準，將及日期轉成星座(String)輸出，最後必須有換行字元。
month ,day = map(int ,input("請輸入月、日(以空格隔開)：").split())      # map是將多筆數值導入Function，int表示整數型態，在input後面加一個split就可以將輸入多筆數值用空格來切割

if (month == 1 and day >= 21) or (month == 2 and day <= 10) :
    zodiac = "水瓶(Aquarius)"
elif (month == 2 and day >= 19) or (month == 3 and day <= 20) :
    zodiac = "雙魚(Pisces)"
elif (month == 3 and day >= 21) or (month == 4 and day <= 20) :
    zodiac = "牡羊(Aries)"
elif (month == 4 and day >= 21) or (month == 5 and day <= 21) :
    zodiac = "金牛(Taurus)"
elif (month == 5 and day >= 22) or (month == 6 and day <= 21) :
    zodiac = "雙子(Gemini)"
elif (month == 6 and day >= 22) or (month == 7 and day <= 22) :
    zodiac = "巨蟹(Cancer)"
elif (month == 7 and day >= 23) or (month == 8 and day <= 23) :
    zodiac = "獅子(Leo)"
elif (month == 8 and day >= 24) or (month == 9 and day <= 23) :
    zodiac = "處女(Virgo)"
elif (month == 9 and day >= 24) or (month == 10 and day <= 23) :
    zodiac = "天秤(Libra)"
elif (month == 10 and day >= 24) or (month == 11 and day <= 22) :
    zodiac = "天蠍(Scorpio)"
elif (month == 11 and day >= 23) or (month == 12 and day <= 21) :
    zodiac = "射手(Sagittarius)"
elif (month == 12 and day >= 22) or (month == 1 and day <= 20) :
    zodiac = "摩羯(capricorn)"
else :
    zodiac = "無效的日期"

print (zodiac)