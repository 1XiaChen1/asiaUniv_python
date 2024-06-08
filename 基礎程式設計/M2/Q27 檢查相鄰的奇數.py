# 問題描述： 輸入5個數字
# 輸入說明： 輸出是否有相鄰的奇數。
# 輸出說明： 有相鄰的奇數，輸出第一組相鄰的奇數，否則輪出NO。
def check_adjacent_odd(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] % 2 != 0 and numbers[i + 1] % 2 != 0:
            return numbers[i], numbers[i + 1]
    return "NO"

numbers = list(map(int, input("請輸入五個數字（空格分隔）：").split()))
result = check_adjacent_odd(numbers)        # 檢查是否有相鄰的奇數並輸出結果
if result == "NO":
    print("NO")
else:
    print(result)