import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('runner')
clock = pygame.time.Clock()

#sky image
sky1 = pygame.image.load('graphics/Sky1.png').convert_alpha()
sky1 = pygame.transform.scale(sky1,(800, 400))

sky2 = pygame.image.load('graphics/Sky2.png').convert_alpha()
sky2 = pygame.transform.scale(sky2,(800, 400))

#ground image
ground1 = pygame.image.load('graphics/ground1.png')
ground2 = pygame.image.load('graphics/ground2.png')

######### Display buttons #########
keys = 40
Left_arrow = pygame.image.load('Buttons/left_arrow.png')
Left_arrow = pygame.transform.scale(Left_arrow,(keys, keys))

Right_arrow = pygame.image.load('Buttons/right_arrow.png')
Right_arrow = pygame.transform.scale(Right_arrow,(keys, keys))

Space_button = pygame.image.load('Buttons/space.png')
Space_button = pygame.transform.scale(Space_button,(80, keys))

#Start text
score = 0
distance = f'Distance: {score} m'
font1 = pygame.font.SysFont("None", 60)
font2 =pygame.font.SysFont("None", 40)
font3 =pygame.font.SysFont("None", 30)
font4 =pygame.font.SysFont("None", 30)
text1 = font1.render('Welcome To Runner', True, 'Black')
text2 = font2.render('controls for this game are:', True, 'Black')
text3 = font3.render('Press space to start', True, 'Black')
#txt_width = text1.get_width()
#txt_height = text1.get_height()
            

#player and fly list of images to scroll thru
list = ['graphics/player1.png', 'graphics/player2.png', 'graphics/player3.png']
list1 = ['graphics/Fly1.png', 'graphics/Fly2.png', 'graphics/Fly1.png']
im = 0
fl = 0

player = pygame.image.load(list[im])
fly = pygame.image.load(list1[fl])

PLAYER_MOVEMENT = pygame.USEREVENT + 1
FLY_MOVEMENT = pygame.USEREVENT + 2
FLY_MOVEMENT2 = pygame.USEREVENT + 3
SKY_MOVEMENT = pygame.USEREVENT + 4
GROUND_MOVEMENT = pygame.USEREVENT + 5
CUSTOM_EVEN = pygame.USEREVENT + 6
DISTANCE_COUNTER = pygame.USEREVENT + 7
# Create a timer to trigger the custom event after a delay (1000 milliseconds)
speed = 200

pygame.time.set_timer(PLAYER_MOVEMENT, 400)
pygame.time.set_timer(FLY_MOVEMENT, 100)
pygame.time.set_timer(FLY_MOVEMENT2, 10)
pygame.time.set_timer(SKY_MOVEMENT, 20)
pygame.time.set_timer(GROUND_MOVEMENT, 15)
pygame.time.set_timer(CUSTOM_EVEN, 4)
pygame.time.set_timer(DISTANCE_COUNTER, speed)

running = True

#sarting variables
txx1, txy1 = 202, 120
txx2, txy2 = 200, 350
txx3, txy3 = 304, 210
lax, lay= 560, 343
rax, ray = 615, 343
spx, spy = 670, 343


start = False

def starting():
    screen.blit(text1,(txx1, txy1))
    screen.blit(text2,(txx2, txy2))
    screen.blit(text3,(txx3, txy3))
    screen.blit(text4,(0, 0))
    screen.blit(Left_arrow,(lax, lay))
    screen.blit(Right_arrow,(rax, ray))
    screen.blit(Space_button,(spx, spy))

space = False
space1 = False
space2 = False

right = False
left = False
x, y = 30, 220

back = True 
gx = 0
gy = 298
g2x = 800
g2y = 298
sx = 0
sy = -80
s2x = 800
s2y = -80

ran_fly_pos = 230
fly_x = -60

def spaced():
    global space, space1, space2, y, sy, s2y
    y-= 2
    if y == 60:
        space1 = False
        space2 = True

def despace():
    global space, space2, y, sy, s2y
    y+= 2
    if y == 220:
        space2 = False
        space = False

def random_fly_number():
    global ran_fly_pos
    ran_fly_pos
    ran_fly_pos = 0
    ran_fly_pos = random.randint(190,258)
    return ran_fly_pos

def images():
    global fly, distance, text4, score, high_score, h_score
    fly = pygame.transform.scale(fly,(40, 20))
    distance = f'Distance: {score} m'
    h_score = f'Highscore: {high_score} m'
    screen.blit(sky1,(sx,sy))
    screen.blit(sky2,(s2x,s2y))
    screen.blit(ground1,(gx,gy))
    screen.blit(ground2,(g2x,g2y))
    screen.blit(fly,(fly_x, ran_fly_pos))
    screen.blit(player,(x , y))
    text4 = font4.render(distance, True, 'Black')
    text5 = font4.render(h_score, True, "BLACK")
    screen.blit(text5,(250, 0))

def text_out():
    global txt_width, txt_height
    global txy1, txy2, txy3, lay, ray, spy, text1
    text1 = font1.render("Game Paused", True, "BLACK")
    txt_width = fly.get_width()
    txt_height = fly.get_height()
    txy1, txy2, txy3 = -41, 429, 420
    lay, ray, spy = 440, 440, 440

def text_in():
    global txy1, txx1, txy2, txy3, lay, ray, spy
    txx1, txy1 = 261, 130
    txy2, txy3 = 350, 210
    lay, ray, spy = 343, 343, 343

def sky_move():
    global sx, s2x
    sx-= 5
    if sx <= -805:
        sx = 800
        print("picture sky1 has reach out of screen")
    else: 
        if sx != 800:
            s2x -= 5
            if s2x == -800:
                s2x = 800
                print("picture sky2 has reach out of screen")

def fly_move():
    global fly_x
    if fly_x >= -84:
        fly_x-= 4
        if fly_x <= -84:
            random_fly_number()
            fly_x = 884

def ground_move():
    global gx, g2x
    gx-= 5
    if gx <= -805:
        gx = 800
        print("picture ground1 has reach out of screen")
        #print(txt_width, txt_height)
    else: 
        if gx != 800:
            g2x -= 5
            if g2x == -800:
                g2x = 800
                print("picture ground2 has reach out of screen")

def d_c():
    global score
    score +=1

def game_over():
    global gameover, high_score, text1, score
    global txx1, txy1, txx2, txy2, txx3, txy3, lax, lay, rax, ray, spx, spy, fly_x, x, y
    global txt_height, txt_width
    if gameover:
        text1 = font1.render("Game Over", True, "BLACK")
        txx1, txy1 = 287, 120
        txx2, txy2 = 200, 350
        txx3, txy3 = 304, 210
        lax, lay= 560, 343
        rax, ray = 615, 343
        spx, spy = 670, 343
        fly_x = -60
        score = 0
        gameover = False

high_score = 0
gameover = False

while running:
    
    images()
    starting()
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and start == False and not gameover:
            start = True
            text_out()
            print("started")
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            start = False
            text_in()
            print("user have pressed escape")
            #print(txt_width,txt_height)

        if start == True:
            if event.type == PLAYER_MOVEMENT:
                im = (im + 1) % len(list)
                player = pygame.image.load(list[im])

            if event.type == FLY_MOVEMENT:
                fl = (fl + 1) % len(list1)
                fly = pygame.image.load(list1[fl])

            if event.type == FLY_MOVEMENT2:
                fly_move()

            if event.type == SKY_MOVEMENT:
                sky_move()         

            if event.type == GROUND_MOVEMENT:
                ground_move()                               
            
            if event.type == DISTANCE_COUNTER:
                d_c()

            if event.type == CUSTOM_EVEN and space == True: 
                space1 = True
                if y != 60 and space1 and not space2:
                    spaced()
                if y != 220 and space2:
                    despace()
                    

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                space = True
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                right = True
                print("right button has been pressed")
            
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                left = True
                print("left button has been pressed")

            while right:
                x+=20
                right = False

            while left:
                x-=20
                left = False

            gameover = False
            fly_width = 8
            fly_height = 8
            fly_rect = pygame.Rect(fly_x, ran_fly_pos, fly_width, fly_height)
            player_rect = player.get_rect(topleft = (x , y))
            if player_rect.colliderect(fly_rect):
                pass
                if not gameover:
                    print("user has colided")
                    gameover = True
                    start = False
                    if score > high_score:
                        high_score = score
                    x, y = 30, 220
                    space = False
                    space1 = False
                    space2 = False
                    game_over()



    pygame.display.update()
    clock.tick(360)
pygame.quit()
sys.exit()