import pygame
import sys

space = False
prespace = False

def spaced():
    global space
    global prespace
    global y
    global sy
    global s2y
    if not prespace:
        prespace = True
        space = True
        while y >= 120:
            y -= 2
        sy += 30
        s2y += 30

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
font1 = pygame.font.SysFont("None", 60)
font2 =pygame.font.SysFont("None", 40)
text1 = font1.render('Welcome To Runner', True, 'Black')
text2 = font2.render('controls for this game are:', True, 'Black')
txt_width = text2.get_width()
txt_height = text2.get_height()


#player and fly list of images to scroll thru
list = ['graphics/player1.png', 'graphics/player2.png', 'graphics/player3.png']
list1 = ['graphics/Fly1.png', 'graphics/Fly2.png', 'graphics/Fly1.png']
im = 0
fl = 0

player = pygame.image.load(list[im])
fly = pygame.image.load(list1[fl])

PLAYER_MOVEMENT = pygame.USEREVENT + 1
FLY_MOVEMENT = pygame.USEREVENT + 2
SKY_MOVEMENT = pygame.USEREVENT + 3
GROUND_MOVEMENT = pygame.USEREVENT + 4
CUSTOM_EVEN = pygame.USEREVENT + 5

# Create a timer to trigger the custom event after a delay (1000 milliseconds)
pygame.time.set_timer(PLAYER_MOVEMENT, 300)
pygame.time.set_timer(FLY_MOVEMENT, 500)
pygame.time.set_timer(SKY_MOVEMENT, 40)
pygame.time.set_timer(GROUND_MOVEMENT, 30)
pygame.time.set_timer(CUSTOM_EVEN, 1000)

running = True
space = False
prespace = False
right = False
left = False
x = 30
y = 220
j=0

back = True 
gx = 0
gy = 298
g2x = 800
g2y = 298
sx = 0
sy = -80
s2x = 800
s2y = -80

#sarting variables
txw1 = 202
txh1 = 120
txw2 = 200
txh2 = 350
law = 560
lah = 335
raw = 630
rah = 335
spw = 710
sph = 335

def starting():
    screen.blit(text1,(txw1, txh1))
    screen.blit(text2,(txw2, txh2))
    screen.blit(Left_arrow,(law, lah))
    screen.blit(Right_arrow,(raw, rah))
    screen.blit(Space_button,(spw, sph))

def images():
    screen.blit(sky1,(sx,sy))
    screen.blit(sky2,(s2x,s2y))
    screen.blit(ground1,(gx,gy))
    screen.blit(ground2,(g2x,g2y))
    screen.blit(fly,(350,50))
    screen.blit(player,(x , y))

while running:
    images()
    starting()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == PLAYER_MOVEMENT:
            im = (im + 1) % len(list)
            player = pygame.image.load(list[im])

        if event.type == FLY_MOVEMENT:
            fl = (fl + 1) % len(list1)
            fly = pygame.image.load(list1[fl])
        
        if event.type == SKY_MOVEMENT:
            sx-= 10
            if sx <= -810:
                sx = 800
                print("picture sky1 has reach out of screen")
            else: 
                if sx != 800:
                    s2x -= 10
                    if s2x == -800:
                        s2x = 800
                        print("picture sky2 has reach out of screen")

        if event.type == GROUND_MOVEMENT:
            gx-= 10
            if gx <= -810:
                gx = 800
                print("picture ground1 has reach out of screen")
                #print(txt_width, txt_height)
            else: 
                if gx != 800:
                    g2x -= 10
                    if g2x == -800:
                        g2x = 800
                        print("picture ground2 has reach out of screen")
                          

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            spaced()            
            print("Spacebar pressed - Action 1")


        elif event.type == CUSTOM_EVEN and space:
            while y != 220:
                y += 2
            sy -= 30
            s2y -= 30 
            print("Action 2")
            space = False
            prespace = space
        
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
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

    pygame.display.update()
    clock.tick(60)
pygame.quit()
sys.exit()