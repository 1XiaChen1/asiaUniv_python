# 問題描述： 讓使用者輸入一正整數，撰寫程式找出一連續整數數列讓該數列的和為此一正整數， 若正整數不能找出連續整數之和，請印出「No」。 例如：15 =1+2+3+4+5 =4+5+6 =7+8
# 輸入說明： 輸入一個正整數。
# 輸出說明： 輸出可能的整數相加連續整數，若找不到時，請印出「No」，最後必須有換行字元。
def find_conseutive(n):
    results = []                         # 用來存放所有符合條件的數列
    for start in range(1, n):            # 遍歷所有可能的數列起始數字
        total = 0
        sequence = []                    # 初始化數列為空列表
        for num in range(start, n):
            total += num                 # 累加數列中的數字
            sequence.append(num)
            if total == n:               # 如果總和等於目標數字，將數列添加到結果列表中並跳出內層循環
                results.append(sequence) # 將當前數字添加到數列中
                break
            elif total > n:              # 如果總和超過目標數字，跳出內層循環
                break
    return results
n = int(input("請輸入一個正整數："))
sequences = find_conseutive(n)
if sequences:                            # 如果有找到符合條件的數列，則逐一輸出這些數列
    for sequence in sequences:
        print ("+".join(map(str, sequence))+f"={n}")
    print()
else:                                    # 如果沒有找到任何符合條件的數列，則輸出 "No" 並加上換行字元
    print ("No\n")