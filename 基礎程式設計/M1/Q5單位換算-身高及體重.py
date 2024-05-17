# 問題描述： 寫一程式，讓使用者輸入身高(cm)及體重(kg)，作單位換算輸出身高(英吋)及體重(磅)。(1 磅=0.454 公斤，1 吋=2.54 公分)
# 輸入說明： 分別輸入身高(cm)(int)及體重(kg)(int)。
# 輸出說明： 作單位換算輸出身高(英吋)(float)及體重(磅)(float)，最後必須有換行字元。
cm ,kg = map(int ,input().split())      # map是將多筆數值導入Function，int表示整數型態，在input後面加一個split就可以將輸入多筆數值用空格來切割
h = cm / 2.54
w = kg / 0.454
print(h)
print(w)