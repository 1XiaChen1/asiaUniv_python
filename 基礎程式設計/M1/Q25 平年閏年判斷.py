# 問題描述： 試撰寫一個程式，可由鍵盤讀入一個4 位數的整數代表西洋年，然後這個年份是否為閏年每四年一閏，每百年不閏，每四百年一閏，例如西元1900 雖為4 的倍數，但可被100 整除，所以不是閏年，同理，2000 是閏年，因可被400 整數，而2004 當然也是閏，因可以被4 整除
# 輸入說明： 輸入西元年份(int)。
# 輸出說明： 輸出閏年(Leap Year)或是平年(Common Year)(String)，最後必須有換行字元。
year = int(input("請輸入西元年："))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) : # 可以被4整除但不能被100整除 或是 可以被400整除都是閏年
    result = "閏年(Leap year)"
else :
    result = "平年(Comon year)"

print (result)