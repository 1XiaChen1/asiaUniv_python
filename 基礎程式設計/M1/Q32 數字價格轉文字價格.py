# 問題描述： 輸入一 1~1000 的價格，並根據此價格在螢幕上印出「? thousand ? hundred? ten? dollar」字樣。
# 輸入說明： 輸入一 1~1000 的價格 (int)。
# 輸出說明： 輸出價格在螢幕上印出「? thousand ? hundred? ten? dollar」字樣，最後必須有換行字元。
num = int(input("請輸入1~1000的數："))
if 1 <= num <= 1000 :
    a = num // 1000
    b = (num % 1000) // 100
    c = (num % 100) // 10
    d = num % 10
    print (f"{a}thousand {b}hundred {c}ten {d}dollar")
else:
    print ("你輸入的數超出範圍")

# 以下程式也是對的但只會顯示有的數值，要用的話圈選後ctrl+/即可
# def convert_price_to_words(price):
#     # 將價格拆分成千、百、十、個位數
#     thousand = price // 1000
#     hundred = (price % 1000) // 100
#     ten = (price % 100) // 10
#     dollar = price % 10
    
#     # 構建輸出字串
#     result = ""
#     if thousand > 0:
#         result += f"{thousand} thousand "
#     if hundred > 0:
#         result += f"{hundred} hundred "
#     if ten > 0:
#         result += f"{ten} ten "
#     if dollar > 0 or price == 0:
#         result += f"{dollar} dollar"
    
#     return result.strip()

# # 讀取輸入的價格
# price = int(input("請輸入價格："))

# # 檢查輸入是否在範圍內
# if 1 <= price <= 1000:
#     result = convert_price_to_words(price)
#     print(result)
# else:
#     print("輸入的價格不在1到1000範圍內")
