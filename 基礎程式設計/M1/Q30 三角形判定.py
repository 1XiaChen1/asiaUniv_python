# 問題描述： 讓使用者輸入三角形的三邊長a, b, c (且 a ≤ b ≤ c ) ，判斷並輸出 a, b, c 是否為合法三邊長。
# 輸入說明： 輸入三角形的三邊長 a, b, c (且a ≤ b ≤ c )。
# 輸出說明： 輸出是否為合法三邊長，最後必須有換行字元。
# 讀取輸入的三邊長
x, y, z = map(int, input("請輸入x,y,z的邊長(以空格隔開)：").split())    # map是將多筆數值導入Function，int表示整數型態，在input後面加一個split就可以將輸入多筆數值用空格來切割
if x + y > z and y + z > x and x + z > y:
    if x == y and x != z:                   # 等腰三角形
        print(True)
    elif x == y and x != z:
        print(True)
    elif x == z and x != y:
        print(True)
    elif y == z and y != x:
        print(True)
    elif x ** 2 + y ** 2 == z ** 2:         # 直角三角形
        print(True)
    elif y ** 2 + z ** 2 == x ** 2:
        print(True)
    elif x ** 2 + z ** 2 == y ** 2:
        print(True)
    elif y ** 2 + z ** 2 - x ** 2 < 0:      # 鈍角三角形
        print(True)
    elif x ** 2 + y ** 2 - z ** 2 < 0:
        print(True)
    elif y ** 2 + x ** 2 - z ** 2 < 0:
        print(True)
    else:
        print(False)
else:
    print(False)