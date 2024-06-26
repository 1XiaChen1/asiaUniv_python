# 問題描述： 已知男生標準體重＝(身高－80 )×0.7；女生標準體重＝(身高－70) × 0.6；試寫一個程式可以計算男生女生的標準體重
# 輸入說明： 輸入兩個數值，依序代表為身高(int)及性別(int)（1代表男性；2代表女性）。
# 輸出說明： 輸出標準體重，浮點數(float)取至第一位，最後必須有換行字元。
height ,gander = map(int ,input("請輸入身高(CM),性別(1代表男性；2代表女性)：").split())
if gander == 1:                  # 利用if迴圈判斷性別不同，套用不同的運算式
    sw =(height-80)*0.7
elif gander == 2:
    sw =(height-70)*0.6
else:
    print ("輸入的性別代碼無效！")  # 如果條件不符合則跳出迴圈
    exit()
print ('{:.1f}'.format(sw))      # 利用格式化輸出，保留小數第一位