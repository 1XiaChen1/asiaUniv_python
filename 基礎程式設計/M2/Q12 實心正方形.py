# 問題描述： 試撰寫一程式，由使用者輸入一正整數 n 及字元 c，輸出以 c 字元印出邊長為 n 之實心正方形。
# 輸入說明： 分別輸入一正整數 n 及字元 c。
# 輸出說明： 輸出以 c 字元，印出邊長為 n 之實心正方形，最後必須有換行字元。
n ,c = input("請輸入數值、要印出的字元(以空格隔開)：").split()
n = int(n)
for i in range(1, n+1):
    for j in range(1, n+1):
        print (c,end="")
    print ()