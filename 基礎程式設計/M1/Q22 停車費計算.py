# 問題描述： 假設某個停車場的費率是停車2小時以內，每半小時30元，超過2小時，但未滿4小時的部份，每半小時40元，超過4小時以上的部份，每半小時60元，未滿半小時部分不計費。如果您從早10點23分停到午3點20分，請撰寫程式計算共需繳交的停車費。
# 輸入說明： 輸入兩組時間時(int)與分(int)，分別為開始與離開時間，24小時制。
# 輸出說明： 輸出停車費(int)，最後必須有換行字元。
start_hour ,start_minute = map(int ,input("請輸入停入的時、分(以空格分隔)：").split())      # map是將多筆數值導入Function，int表示整數型態，在input後面加一個split就可以將輸入多筆數值用空格來切割
leave_hour ,leave_minute = map(int ,input("請輸入駛出的時、分(以空格分隔)：").split())
start_total = start_hour*60 + start_minute      # 將開始和結束時間轉換成總分鐘數
leave_total = leave_hour*60 + leave_minute

total_minutes = leave_total - start_total       # 計算總停車時間，以分鐘為單位

half_hours = total_minutes // 30                # 計算總停車時間，以半小時為單位

if half_hours <= 4:                             # 停車2小時以內
    fee = half_hours * 30
elif half_hours <= 8:                           # 停車超過2小時但未滿4小時
    fee = 4 * 30 + (half_hours - 4) * 40
else:                                           # 停車超過4小時
    fee = 4 * 30 + 4 * 40 + (half_hours - 8) * 60

print (fee)