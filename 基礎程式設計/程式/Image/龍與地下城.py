import time

def print_delay(text, delay=1):
    print(text)
    time.sleep(delay)

def start_game():
    print_delay("歡迎來到龍與地下城冒險遊戲！")
    player_name = input("請輸入你的角色名稱：")
    print_delay(f"你的冒險者名稱是 {player_name}！")
    choose_path()

def choose_path():
    print_delay("你來到了一個古老的洞穴，洞穴分為左右兩條路。")
    choice = input("你要選擇向左邊走還是向右邊走？（左/右）")
    if choice.lower() == "左":
        print_delay("你選擇了向左邊走。")
        left_path()
    elif choice.lower() == "右":
        print_delay("你選擇了向右邊走。")
        right_path()
    else:
        print_delay("請輸入有效的選擇！")
        choose_path()

def left_path():
    print_delay("你進入了一個黑暗的房間。")
    choice = input("你要點亮燈光嗎？（是/否）")
    if choice.lower() == "是":
        print_delay("你點亮了燈光，發現了一個寶箱。")
        open_chest()
    elif choice.lower() == "否":
        print_delay("你在黑暗中摸索著，感到一陣寒意。")
        # 在這裡繼續遊戲的邏輯和互動
    else:
        print_delay("請輸入有效的選擇！")
        left_path()

def open_chest():
    print_delay("你打開了寶箱，裡面有一把魔法劍！")
    # 在這裡繼續遊戲的邏輯和互動

def right_path():
    print_delay("你來到了一個神祕的廳堂。")
    print_delay("一位老人走向你，他是一位賢者。")
    choice = input("賢者問道：你想要學習魔法嗎？（是/否）")
    if choice.lower() == "是":
        print_delay("賢者教授了你一個強大的火球術。")
        # 在這裡繼續遊戲的邏輯和互動
    elif choice.lower() == "否":
        print_delay("你向賢者致意，並繼續你的冒險。")
        # 在這裡繼續遊戲的邏輯和互動
    else:
        print_delay("請輸入有效的選擇！")
        right_path()

start_game()
