# 問題描述： 請寫一個程式讓使用者輸入圓的半徑(float)與高(float)，程式輸出該圓的體積 (float)。  π×𝑟2
# 輸入說明： 輸入半徑(float)與高度 (float)。
# 輸出說明： 輸出該圓的體積(float)，最後必須有換行字元。
import math
r ,h = map(float,input("請輸入半徑與高：").split())   # map是將多筆數值導入Function，int表示整數型態，在input後面加一個split就可以將輸入多筆數值用空格來切割
wiig = math.pi * r**2                              # 用數學庫中導入PI的運算式乘以半徑平方
print (wiig*h)                                     # 再乘以高