#'可以发射的子弹数一定'
#'调节难度'
#'敌机被击中后从敌机列表中删除'
#'显示剩余子弹数'
#'被敌机击中、敌机到终点、与敌机碰撞都会减少生命值，生命值减少到零时结束'
#结束条件：1.子弹打光 2.'生命值减少到零'
#'背景音效、我方开火音效、击中敌方音效'、生命值减少音效、游戏结束音效
#子弹相撞爆炸


import pygame
import random
import math

pygame.init() 
#设置初始值
wo_x=250
wo_y=520
wo_v=5
yunxing=True
a=[True,False]
kaishijiemian=True
nanduxuanze=False
youxikaishi=False
diyidiji=True
jieshujiemian = False
可以发射子弹=True

# 添加背景音乐
pygame.mixer.music.load('bg.wav')
pygame.mixer.music.play(-1)
# 添加击中音效
hit_sound = pygame.mixer.Sound('exp.wav')
# 添加射击音效
shoot_sound = pygame.mixer.Sound('laser.wav')
# 添加被击中音效
hited_sound = pygame.mixer.Sound('hited.wav')
#添加结束音效
over_sound = pygame.mixer.Sound('游戏结束.wav')
#添加子弹碰撞音效
crush_sound = pygame.mixer.Sound('crush.wav') 
#添加飞机突破防线音效
tupo_sound = pygame.mixer.Sound('tupo1.wav') 

#创建窗口，引入各图像
screen=pygame.display.set_mode((600,800))
pygame.display.set_caption('飞机大战')
feijidazhan=pygame.image.load('飞机大战.png')
beijing1=pygame.image.load('beijing.png')
wo1=pygame.image.load('战斗机.png')
wo2=pygame.image.load('战斗机开火1.png')
diji=pygame.image.load('敌机.png')
baozha=pygame.image.load('爆炸效果.png')
dizidan=pygame.image.load('敌方子弹.png')
kaishi=pygame.image.load('开始.png')
结束游戏=pygame.image.load('结束游戏.png')

#引入时钟模块，以便主循环中调节帧率
clock=pygame.time.Clock()

#设置自定义事件，每几秒触发一次，用于每几秒执行一次操作的触发
directionchange=pygame.USEREVENT
dijichuxian=pygame.USEREVENT + 1
fashe=pygame.USEREVENT + 2




#背景类
class beijing():
    def __init__(self):
        self.tuyi=pygame.image.load('beijing.png')
        self.tuer=pygame.image.load('beijing.png')
        self.y1=0
        self.y2=-800
q=beijing()
    


#我方子弹类
class wo_zidan():

    def __init__(self):
        self.tupian = pygame.image.load('开火.png')
        shoot_sound.play()
        self.x= wo_x +20
        self.y= wo_y -20
        self.v= wo_zidan_v
    def wo_zidan_move(self):
        screen.blit(self.tupian,(self.x,self.y))
        self.jizhong1()
        self.y-=self.v
    def jizhong1(self):
        global score
        for e in di_feijis:
            	if(juli(self.x+10, self.y, e.x+25.5, e.y) < 30):
                    wo_zidans.remove(self)
                    e.jihui()  
                    hit_sound.play()
                    score+=1
    

#敌方飞机类
class di_feiji():
    def __init__(self):
        self.tupian = diji
        self.x= random.randrange(0,550)
        self.y= 0
        self.v= di_v
    def di_feiji_move(self):
        screen.blit(self.tupian,(self.x,self.y))
        if self.x<0 or self.x>550:
            self.v*=-1
        self.crush()
        self.x+=self.v
        self.y+= di_v
    def jihui(self):
        di_feijis.remove(self)
        screen.blit(pygame.image.load('敌机爆炸.png'),(self.x,self.y))
    def crush(self):
        global wo_x,wo_y,life
        if (juli(self.x+20.5, self.y+27.5, wo_x+28.5, wo_y+33.5) < 40):
            di_feijis.remove(self)
            screen.blit(pygame.image.load('敌机爆炸.png'),(self.x,self.y))  
            hit_sound.play()
            wo_x = 250
            wo_y = 500
            life = life -1

        
#敌方子弹类
class di_zidan():
    def __init__(self):
        self.tupian = dizidan
        self.x= n.x+25.5
        self.y= n.y+27.5
        self.v= di_zidan_v
    def di_zidan_move(self):
        screen.blit(self.tupian,(self.x,self.y))
        # self.jizhong2()
        self.y+=self.v

#我方移动函数
def wo_move():
    
    global wo_x,wo_y,life
    for e in di_zidans:
        if (juli(e.x+8.5, e.y, wo_x+28.5, wo_y) < 30):
            di_zidans.remove(e)
            wo_x = 250
            wo_y = 500
            life = life - 1
            hited_sound.play()
    if moveleft and 0<wo_x:
        wo_x -= wo_v
    if moveright and wo_x<550:
        wo_x += wo_v
    if moveup and wo_y>0:
        wo_y -= wo_v
    if movedown and wo_y<750:
        wo_y += wo_v

        

#距离函数
def juli(ax,ay,bx,by):
    a = ax - bx
    b = ay - by
    return math.sqrt(a*a + b*b)


#分数
score = 0
font1 = pygame.font.Font('freesansbold.ttf', 32)
def fenshu():
    text1 = f"Score:{score}"
    score_render = font1.render(text1,True,(255,255,255))
    screen.blit(score_render,(10,10))
#结束分数
def over_fenshu():
    text1 = f"{score}"
    score_render = font1.render(text1,True,(255,255,255))
    screen.blit(score_render,(335,375))  
#生命值
life = 30
font2 = pygame.font.Font('freesansbold.ttf', 32)
def shengming():
    text2 = f"Life:{life}"
    life_render = font2.render(text2,True,(0,0,255))
    screen.blit(life_render,(10,40))
#子弹数
bullet = 100
font3 = pygame.font.Font('freesansbold.ttf',32)
def zidan():
    text3 = f"Bullet:{bullet}"
    bullet_render = font3.render(text3,True,(255,0,0))
    screen.blit(bullet_render,(10,65))
    
# 游戏结束
font4 = pygame.font.Font('freesansbold.ttf',100)
def over():
    text4 = 'Game Over'
    render = font4.render(text4,True,(255,0,0))
    screen.blit(render,(20,150))
    


#选择重新开始后的重置函数
def chongzhi():
    global wo_x,wo_y,score,life,bullet,wo_zidans,di_feijis,di_zidans
    wo_x=250
    wo_y=500
    score=0
    life=20
    bullet=100
    wo_zidans=[]
    di_feijis=[]
    di_zidans=[]
    
    
    
    
        
     
#我方子弹列表   
wo_zidans=[]
#敌方飞机列表
di_feijis=[]
#敌方子弹列表
di_zidans=[]



#游戏主循环
while yunxing:
    #调节帧率
    clock.tick(60) 
    if kaishijiemian:
        screen.blit(beijing1,(0,0))
        screen.blit(feijidazhan,(140,100))
        screen.blit(kaishi,(150,400))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                spot = event.pos
                if 181<spot[0]<419 and 466<spot[1]<535:
                    kaishijiemian=False
                    nanduxuanze=True
                    
                    
    if nanduxuanze:
        screen.blit(beijing1,(0,0))
        screen.blit(pygame.image.load('难度选择.png'),(170,150))
        screen.blit(pygame.image.load('简单.png'),(170,250))
        screen.blit(pygame.image.load('较难.png'),(170,350))
        screen.blit(pygame.image.load('极难.png'),(170,450))
        moveleft=False
        moveright=False
        moveup=False
        movedown=False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                spot = event.pos
                #简单模式
                if 170<spot[0]<430 and 250<spot[1]<330:
                    di_v=2.5
                    di_zidan_v=4
                    wo_zidan_v=12
                    dibfx=3000
                    dicx=3000
                    zidanfashe=1500
                    zdgl=4
                    pygame.time.set_timer(directionchange,dibfx)
                    pygame.time.set_timer(dijichuxian,dicx)
                    pygame.time.set_timer(fashe,zidanfashe)
                    
                    nanduxuanze=False
                    youxikaishi=True
                #较难模式
                if 170<spot[0]<430 and 350<spot[1]<430:
                    di_v=3
                    di_zidan_v=5
                    wo_zidan_v=9
                    dibfx=2000
                    dicx=2500
                    zidanfashe=1250
                    zdgl=3
                    pygame.time.set_timer(directionchange,dibfx)
                    pygame.time.set_timer(dijichuxian,dicx)
                    pygame.time.set_timer(fashe,zidanfashe)
                    nanduxuanze=False
                    youxikaishi=True
                #极难模式
                if 170<spot[0]<430 and 450<spot[1]<530:
                    di_v=3.5
                    di_zidan_v=7
                    wo_zidan_v=6
                    dibfx=1000
                    dicx=2000
                    zidanfashe=1000
                    zdgl=3
                    pygame.time.set_timer(directionchange,dibfx)
                    pygame.time.set_timer(dijichuxian,dicx)
                    pygame.time.set_timer(fashe,zidanfashe)
                    nanduxuanze=False
                    youxikaishi=True
                    
                    
    if youxikaishi:
        #背景滚动
        overyin=True
        screen.blit(q.tuyi,(0,q.y1))
        screen.blit(q.tuer,(0,q.y2))
        q.y1+=2
        q.y2+=2
        if q.y1>=800:
            q.y1=0
        if q.y2>=0:
            q.y2=-800
        #显示中途推出按钮
        screen.blit(结束游戏,(10,100))
        
        zidan()
        fenshu()
        shengming()
        screen.blit(wo1,(wo_x,wo_y))
        if diyidiji:
            di_feijis.append(di_feiji())
        diyidiji=False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            #通过moveleft等参数的状态完成持续按键时持续响应，否则必须按一下移动一下
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    moveleft=True
                if event.key==pygame.K_RIGHT:
                    moveright=True
                if event.key==pygame.K_UP:
                    moveup=True
                if event.key==pygame.K_DOWN:
                    movedown=True
                if event.key==pygame.K_SPACE and 可以发射子弹:
                    wo_zidans.append(wo_zidan())
                    screen.blit(wo2,(wo_x,wo_y))
                    bullet = bullet -1
                if event.key==pygame.K_SPACE:
                    pygame.time.delay(10**10)
                if event.key==pygame.K_DOWN:
                    pygame.time.get_ticks()
            if event.type == pygame.KEYUP:
                if event.key==pygame.K_LEFT:
                    moveleft=False
                if event.key==pygame.K_RIGHT:
                    moveright=False
                if event.key==pygame.K_UP:
                    moveup=False
                if event.key==pygame.K_DOWN:
                    movedown=False
                if event.key==pygame.K_SPACE:
                    screen.blit(wo1,(wo_x,wo_y))
            #需要每几秒执行一次的操作
            if event.type == pygame.USEREVENT + 1:
                if life != 0 and bullet >0:
                    di_feijis.append(di_feiji())
            if event.type == pygame.USEREVENT:
                for k in di_feijis:
                    x_direction=random.choice(a)
                    if x_direction and 10<k.x<520:
                        k.v*=-1
            if event.type == pygame.USEREVENT + 2:
                for n in di_feijis:
                    m=random.randrange(1,zdgl)
                    if m == 1:
                        di_zidans.append(di_zidan())
            #点击游戏结束按钮结束游戏
            if event.type == pygame.MOUSEBUTTONDOWN:
                spot = event.pos
                if 10<spot[0]<90 and 100<spot[1]<133:
                    pygame.mixer.music.stop()
                    youxikaishi=False
                    jieshujiemian=True
                    
        #我方飞机移动
        wo_move()
        #我方子弹移动与出界删除
        for i in wo_zidans:
            i.wo_zidan_move()
            if i.y<-180:
                wo_zidans.remove(i)
        #子弹碰撞检测
        for m in wo_zidans:
            for u in di_zidans:
                if juli(m.x+10,m.y,u.x+8.5,u.y)<25:
                    screen.blit(baozha,(m.x-5,m.y))
                    crush_sound.play()
                    wo_zidans.remove(i)
                    di_zidans.remove(u)
        #敌方飞机移动 和出界删除   
        for k in di_feijis:
            k.di_feiji_move()
            if k.y>800:
                life = life -1
                di_feijis.remove(k)
                tupo_sound.play()
        #敌方子弹移动与出界删除
        for o in di_zidans:
            o.di_zidan_move()
            if o.y>1000:
                di_zidans.remove(o)
        # 判断结束
        if life == 0:
            di_feijis.clear()
            di_zidans.clear()
            pygame.mixer.music.stop()
            youxikaishi = False
            jieshujiemian = True
        if bullet == 0:
            可以发射子弹=False   
            if wo_zidans==[]:
                pygame.mixer.music.stop()
                youxikaishi = False
                jieshujiemian = True
                
                
        # 结束界面
    if jieshujiemian:
        #game over音效加这里
        if overyin:        
            over_sound.play()
            overyin=False
        screen.blit(beijing1,(0,0))
        over()
        screen.blit(pygame.image.load('得分.png'),(170,350))
        over_fenshu()
        screen.blit(pygame.image.load('重新开始.png'),(170,450))
        screen.blit(pygame.image.load('退出游戏.png'),(170,550))
        可以发射子弹=True
        diyidiji=True
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                spot = event.pos
                if 170<spot[0]<430 and 450<spot[1]<530:
                    jieshujiemian=False
                    nanduxuanze=True
                    pygame.mixer.music.play(-1)
                    chongzhi()
                if 170<spot[0]<430 and 550<spot[1]<630:
                    pygame.quit()
    
    pygame.display.update()
pygame.quit()
