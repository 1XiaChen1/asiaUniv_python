# 問題描述： 讓使用者輸入一合法三角形的三邊長a, b, c (且  a≤b≤c  ) ， 判斷並輸出該三角形為「Right triangle(直角三角形)」，「Obtuse triangle(鈍角三角形)」，或「Acute triangle(銳角三角形)」。
# 判斷方法：假設三角形的三個邊長分別是 a, b, c，其中 c 為最長的邊長計算一下
# 如果  a2+b2<c2  則為鈍角三角形鈍角位於 c 所對應的角。
# 如果  a2+b2=c2  則為直角三角形直角位於c所對應的角。
# 如果  a2+b2>c2  則為銳角三角形 a, b, c 三邊所對應的角均為銳角
# 輸入說明： 輸入一合法三角形的三邊長 a (int), b (int), c(int) (且  a≤b≤c  )。
# 輸出說明： 判斷並輸出該三角形為「Right triangle(直角三角形)」，「Obtuse triangle(鈍角三角形)」，或「Acute triangle(銳角三角形)」，最後必須有換行字元。
x, y, z = map(int, input("請輸入x,y,z的邊長(以空格隔開)：").split())        # map是將多筆數值導入Function，int表示整數型態，在input後面加一個split就可以將輸入多筆數值用空格來切割

if x + y > z and x + z > y and y + z > x:
    x2 = x ** 2
    y2 = y ** 2
    z2 = z ** 2

    if x2 + y2 == z2:
        result = "Right triangle(直角三角形)"
    elif x2 + y2 < z2:
        result = "Obtuse triangle(鈍角三角形)"
    else:
        result = "Acute triangle(銳角三角形)"
else:
    result = False
    
print (result)