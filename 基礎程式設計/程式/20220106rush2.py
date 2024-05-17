import pygame as pg
import random as rd
import time
import math
pg.init()

#設定視窗
width, height = 1024, 768
screen = pg.display.set_mode((width, height))
pg.display.set_caption('人生模擬器')

#bg
white , black ,pink ,yellow= (255,255,255),(0,0,0),(229,170,242),(255,255,0)
bg = pg.Surface(screen.get_size())
bg = bg.convert()
bg.fill(black)

src = ".\\\\Image\\"
howmuchpoint = 5
leftpoint = howmuchpoint
pointname = ['運氣','智力','外表','家境']
badending = ['出生時發生意外不幸死亡','因為太笨了所以沒辦法畢業','因為家裡沒錢支持你創業失敗了','因為長太醜找不到女朋友所以孤老終生']
rush=False
rushwin=False
win = 0
times = 0
time_start= time.time()
time_end= time.time()
target_times = 500
rushmod = True

#title
def title(word,size,x,y,willretrun=False,font_color = white,bg_color = black):
    global running    
    font = pg.font.SysFont("DFKai-SB", size)
    text = font.render(word, True, font_color,bg_color)
    textpos = text.get_rect()
    textpos.center = screen.get_rect().center
    textpos.move_ip(x,-y)
    bg.blit(text, textpos)
    if willretrun:
        return [text,textpos]
#圖片
def Image(location,x,y,size_X,size_Y,willretrun=False):
    image = pg.image.load(location).convert()
    image = pg.transform.scale(image, (size_X, size_Y))
    imagepos = image.get_rect()
    imagepos.center = screen.get_rect().center
    imagepos.move_ip(x,-y)
    bg.blit(image, imagepos)
    if willretrun:
        return [image,imagepos]
    
#點數加    
def levelup(ids):
    global points,leftpoint
    global add
    if points[ids] <5 and leftpoint >0:
        points[ids] += 1
        leftpoint -= 1
        Image(src + "level"+str(points[ids])+".png" ,-375+350*ids+25,0,100,300,False)
        screen.blit(bg, (0,0))
        pg.display.update()
#點數減    
def leveldown(ids):
    global points,leftpoint,howmuchpoint1
    global sub
    if points[ids] > 0 and leftpoint <howmuchpoint: 
        points[ids] -= 1
        leftpoint += 1
        Image(src + "level"+str(points[ids])+".png" ,-375+350*ids+25,0,100,300,False)
        screen.blit(bg, (0,0))
        pg.display.update()
#模板
def modol(text):
    global bg
    running = True
    nextpage = False
    
    ############# 畫面 #################
    button = title(text,50,0,300,True)
    
    ####################################
    screen.blit(bg, (0,0))
    pg.display.update()
        
    while running:
        for event in pg.event.get():
            ############# 按鈕功能 #################
            if event.type == pg.QUIT:
                running = False
                pg.quit() 
            if event.type == pg.MOUSEBUTTONDOWN:
                if button[1].collidepoint(event.pos):
                    nextpage = True
            #######################################
        if nextpage: break
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((0,0,0))
#開始畫面
def start():
    global bg,rush,win,lose,rushwin
    running = True
    nextpage = False
    
    ############# 畫面 #################
    title('人生模擬器', 72,0,200,False,pink)
    cont = ["在遊戲一開始時，玩家會獲得五個天賦點，","並可以將這些天賦點分配給三個能力，分配完成後即可進入遊戲，","每一個小段落都有著可以左右故事走向的情境選擇提供玩家選擇，","不同的天賦點分配、故事選擇都將導致不同的結局。"]
    for i in cont:
        title(i,32,0,100-50*cont.index(i))
    button = title("點我繼續",50,0,-200,True,yellow)
    
    if(rushmod):
        buttontwo = Image(src+"rush0"+".png", 30, -300, 500, 100,True)
    ####################################
    screen.blit(bg, (0,0))
    pg.display.update()
        
    while running:
        for event in pg.event.get():
            ############# 按鈕功能 #################
            if event.type == pg.QUIT:
                running = False
                pg.quit() 
            if event.type == pg.MOUSEBUTTONDOWN:
                if button[1].collidepoint(event.pos):
                    nextpage = True
                if(rushmod):
                    if buttontwo[1].collidepoint(event.pos):
                        if(rush):
                            if(rushwin):
                                rush = False
                                buttontwo = Image(src+"rush0"+".png", 30, -300, 500, 100,True)
                                rushwin = False
                            else:
                                rushwin = True
                                buttontwo = Image(src+"rush2"+".png", 30, -300, 500, 100,True)
                        else:
                            rush = True
                            win=0
                            lose=0
                            buttontwo = Image(src+"rush1"+".png", 30, -300, 500, 100,True)
                    screen.blit(bg, (0,0))
                    pg.display.update()
                    
            #######################################
        if nextpage: break
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((0,0,0))
#天賦點說明
def introduction():
    global bg
    running = True
    nextpage = False
    
    ############# 畫面 #################
    title('天賦點說明',72,0,200,False,pink)
    intro = ['每個能力都有一個基本的天賦點，而一個天賦點所增加的機率是10%，','他只能增加機率所以當同樣的天賦點分配也可能造成不同結果。']
    for i in intro:
        title(i,32,0,50-50*intro.index(i))
    button = title('點我開始遊戲',50,0,-200,True,yellow)
    ####################################
    screen.blit(bg, (0,0))
    pg.display.update()
        
    while running:
        for event in pg.event.get():
            ############# 按鈕功能 #################
            if event.type == pg.QUIT:
                running = False
                pg.quit() 
            if event.type == pg.MOUSEBUTTONDOWN:
                if button[1].collidepoint(event.pos):
                    nextpage = True
            #######################################
        if nextpage: break
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((0,0,0))
#點天賦點
def point():
    global bg,pointname,leftpoint,time_start
    running = True
    nextpage = False
    
    ############# 畫面 #################
    title('點天賦點',72,0,250,True,pink)

    [title(i,32,-355+350*(pointname.index(i)-1),180) for i in pointname[1:4]]
    [Image(src + "level0.png" ,-375+350*i+25,0,100,300,False) for i in range(3)]
    add = [Image(src + "add.png" ,-405+350*i+25,-180,40,40,True) for i in range(3)]
    sub = [Image(src + "sub.png" ,-345+350*i+25,-180,40,40,True) for i in range(3)]
    button = title('點我開始',50,0,-280,True,yellow)
    ####################################
    screen.blit(bg, (0,0))
    pg.display.update()
        
    while running:
        for event in pg.event.get():
            ############# 按鈕功能 #################
            if event.type == pg.QUIT:
                running = False
                pg.quit() 
            if event.type == pg.MOUSEBUTTONDOWN:
                if button[1].collidepoint(event.pos):
                    if leftpoint == 0:    
                        nextpage = True
                    if(rush):
                        time_start = time.time()
                for i in add:
                    if i[1].collidepoint(event.pos):
                        levelup(add.index(i))
                for i in sub:
                    if i[1].collidepoint(event.pos):
                        leveldown(sub.index(i))
            #######################################
        if nextpage: break
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((0,0,0))
#凶
def bad(i):
    global bg,badending,badending,restart
    running = True
    nextpage = False
    
    ############# 畫面 #################
    Image(src+"bad"+str(i)+".jpg", 0, 0, 400, 400)
    title('你...',70,0,300,False,pink)
    title(badending[i],32,0,250,False)
    button = title('重新投胎',50,-10,-250,True,yellow)
    buttontwo = title('離開遊戲',50,0,-320,True,yellow)    
    ####################################
    screen.blit(bg, (0,0))
    pg.display.update()
        
    while running:
        if(rush):
            nextpage=True
        for event in pg.event.get():
            ############# 按鈕功能 #################
            if event.type == pg.QUIT:
                running = False
                pg.quit() 
            if event.type == pg.MOUSEBUTTONDOWN:
                if button[1].collidepoint(event.pos):
                    bg = pg.Surface(screen.get_size())
                    bg = bg.convert()
                    bg.fill((0,0,0))
                    restart = True
                    running = False
                if buttontwo[1].collidepoint(event.pos):
                    running = False
                    pg.quit()
            #######################################
        if nextpage: break
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((0,0,0))
#運氣
def lucky():
    global bg,nb
    running = True
    nextpage = False

    ############# 畫面 #################
    Image(src+"IMG_7646.jpg",0,0,400,400)
    title('挖屋!你...',72,0,250,False,pink)
    title('出生了!!!',32,0,-250)
    button = title('繼續人生',50,0,-300,True,yellow)
    
    ####################################
    screen.blit(bg, (0,0))
    pg.display.update()
        
    while running:
        if(rush):
            nextpage=True
        for event in pg.event.get():
            ############# 按鈕功能 #################
            if event.type == pg.QUIT:
                running = False
                pg.quit() 
            if event.type == pg.MOUSEBUTTONDOWN:
                if button[1].collidepoint(event.pos):
                    nextpage = True
            #######################################
        if nextpage: break
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((0,0,0))
#智力
def smart():
    global bg
    running = True
    nextpage = False
    
    ############# 畫面 #################
    Image(src+'IMG_7650.jpg', 0,50, 350, 400)
    title('挖屋!你...',72,0,300,False,pink)
    title('因為太聰明了',32,0,-200)
    title("所以成功從逢甲大學應用數學系畢業",32,0,-250)
    button = title('繼續人生',50,0,-300,True,yellow)
    ####################################
    screen.blit(bg, (0,0))
    pg.display.update()
    
        
    while running:
        if(rush):
            nextpage=True
        for event in pg.event.get():
            ############# 按鈕功能 #################
            if event.type == pg.QUIT:
                running = False
                pg.quit() 
            if event.type == pg.MOUSEBUTTONDOWN:
                if button[1].collidepoint(event.pos):
                    nextpage = True
            #######################################
        if nextpage: break
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((0,0,0))
#外表
def outlook():
    global bg
    running = True
    nextpage = False
    
    ############# 畫面 #################
    Image(src + "IMG_7653.jpg", 0, 25, 475, 400)
    title('挖屋!你...',72,0,300,False,pink)
    title('因為帥氣的外表交到女朋友脫離了魯蛇',32,0,-220)
    title('並順利結婚了',32,0,-250)
    button = title('繼續人生',50,0,-300,True,yellow)    
    ####################################
    screen.blit(bg, (0,0))
    pg.display.update()
        
    while running:
        if(rush):
            nextpage=True
        for event in pg.event.get():
            ############# 按鈕功能 #################
            if event.type == pg.QUIT:
                running = False
                pg.quit() 
            if event.type == pg.MOUSEBUTTONDOWN:
                if button[1].collidepoint(event.pos):
                    nextpage = True
            #######################################
        if nextpage: break
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((0,0,0))
#家境
def home():
    global bg
    running = True
    nextpage = False
    
    ############# 畫面 #################
    Image(src + "IMG_7656.jpg", 0, 0, 400, 400)
    title('挖屋!你...',72,0,250,False,pink)
    title('因為家裡有錢支持你創業',32,0,-220)
    title('所以你創業成功了。',32,0,-250)
    button = title('繼續人生',50,0,-300,True,yellow)
    ####################################
    screen.blit(bg, (0,0))
    pg.display.update()
        
    while running:
        if(rush):
            nextpage=True
        for event in pg.event.get():
            ############# 按鈕功能 #################
            if event.type == pg.QUIT:
                running = False
                pg.quit() 
            if event.type == pg.MOUSEBUTTONDOWN:
                if button[1].collidepoint(event.pos):
                    nextpage = True
            #######################################
        if nextpage: break
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((0,0,0))

#end
def end():
    global bg,restart
    running = True
    nextpage = False
    
    ############# 畫面 #################
    title('挖屋!你...',72,0,200,False,pink)
    title('因為創業成功又娶了一個漂亮的老婆',32,0,100)
    title('順利成為人生勝利組過完這輩子',32,0,50)
    button = title('重新投胎',50,-10,-180,True,yellow)
    buttontwo = title('離開遊戲',50,0,-250,True,yellow)
    ####################################
    screen.blit(bg, (0,0))
    pg.display.update()
        
    while running:
        if(rush and rushwin==False):
            nextpage=True
        for event in pg.event.get():
            ############# 按鈕功能 #################
            if event.type == pg.QUIT:
                running = False
                pg.quit() 
            if event.type == pg.MOUSEBUTTONDOWN:
                if button[1].collidepoint(event.pos):
                    bg = pg.Surface(screen.get_size())
                    bg = bg.convert()
                    bg.fill((0,0,0))
                    restart = True
                    running = False
                if buttontwo[1].collidepoint(event.pos):
                    running = False
                    pg.quit()
            #######################################
        if nextpage: break
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((0,0,0))
#過場
def duration(i):
    global bg
    running = True
    nextpage = False
    
    ############# 畫面 #################
    Image(src+"dur"+str(i)+".jpg",0,0,516,400)
    
    arr = ["你平安長大了","你成功考上優秀的大學"]
    title('挖屋!你...',72,0,250,False,pink)
    title(arr[i],32,0,-240)

    button = title("繼續",50,0,-300,True,yellow)
    
    ####################################
    screen.blit(bg, (0,0))
    pg.display.update()
        
    while running:
        if(rush):
            nextpage=True
        for event in pg.event.get():
            ############# 按鈕功能 #################
            if event.type == pg.QUIT:
                running = False
                pg.quit() 
            if event.type == pg.MOUSEBUTTONDOWN:
                if button[1].collidepoint(event.pos):
                    nextpage = True
            #######################################
        if nextpage: break
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((0,0,0))
#Rush葉面
def rushpage():
    global bg
    running = True
    nextpage = False
    
    ############# 畫面 #################
    title("在"+str(times)+"次的輪迴中，你成為人生勝利組"+str(win)+"次",32,0,60)
    title("可見人生可貴，要珍惜生命。",32,0,-10)
    button = title("繼續",50,0,-300,True,yellow)
    
    ####################################
    screen.blit(bg, (0,0))
    pg.display.update()
        
    while running:
        
        for event in pg.event.get():
            ############# 按鈕功能 #################
            if event.type == pg.QUIT:
                running = False
                pg.quit() 
            if event.type == pg.MOUSEBUTTONDOWN:
                if button[1].collidepoint(event.pos):
                    nextpage = True
            #######################################
        if nextpage: break
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((0,0,0))
def number(a):
    if(target_times>0):
        digits = int(math.log10(target_times))
        if(target_times%10**digits!=0):
            return 10**digits
        else:
            return 10**(digits-1)
    else:
        return 1

def rushpage2():
    global bg,target_times
    running = True
    nextpage = False
    
    ############# 畫面 #################
    add = Image(src+"add.png", 0, 100, 100, 100,True)
    sub = Image(src+"sub.png", 0, -100, 100, 100,True)
    title(str(target_times), 50, 0, 0)
    button = title("OK",50,400,-300,True,yellow)
    
    ####################################
    screen.blit(bg, (0,0))
    pg.display.update()
        
    while running:
        for event in pg.event.get():
            ############# 按鈕功能 #################
            if event.type == pg.QUIT:
                running = False
                pg.quit() 
            if event.type == pg.MOUSEBUTTONDOWN:
                if button[1].collidepoint(event.pos):
                    nextpage = True
                if add[1].collidepoint(event.pos):
                    target_times+=number(0)
                    bg = pg.Surface(screen.get_size())
                    bg = bg.convert()
                    bg.fill((0,0,0))
                    rushpage2()
                if sub[1].collidepoint(event.pos):
                    if(target_times>0):
                        target_times-=number(1)
                        bg = pg.Surface(screen.get_size())
                        bg = bg.convert()
                        bg.fill((0,0,0))
                        rushpage2()
            #######################################
        if nextpage: break
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((0,0,0))
#比較
def test(i):
    global nb,sd
    if nb[i] <= sd[i]:
        return 1
    else:
        return 0

############# 流程 #################   

while 1 :
    if(times!=100):
        times+=1
    else:
        rushpage()
        rush=False
        time_end = time.time()
        print(times,win)
        time_c= time_end - time_start   #執行所花時間
        print('time cost', time_c, 's')
        times=0
    
    
    firstnb = rd.random()
    nb = [rd.random() for i in range(3)]    
    restart = False
    if(rush==False):
        points = [0 for i in range(3)]
        leftpoint = howmuchpoint
        start()
        introduction()
        if(rush):
            rushpage2()
        point()
        
        

    
    sd = [(i+1/6)/10 for i in points]
    value = [test(i) for i in range(3)]
    value=[1,1,0]
    if firstnb <= 0.75:
        lucky()
        duration(0)
        for i in range(3):
            if i == 0:
                if value[i] == 1:
                    duration(1)
                    smart()
                else:
                    duration(1)
                    bad(i+1)
                    if restart :break 
            if i == 1:
                if value[i] == 1:
                    
                    home()
                else:
                    bad(i+1)
                    if restart : break
            if i == 2:
                if value[i] == 1:
                    outlook()
                    end()
                    win+=1
                else:
                    bad(i+1)
                    if restart : break
                
       
    else:
        bad(0)

                     
####################################
pg.quit()       