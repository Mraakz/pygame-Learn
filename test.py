import pygame
import sys

space = False
prespace = False

def spaced():
    global space
    global prespace
    global y
    if not prespace:
        prespace = True
        space = True
        while y >= 120:
            y -= 2

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('runner')
clock = pygame.time.Clock()

sky1 = pygame.image.load('graphics/Sky1.png').convert_alpha()
sky1 = pygame.transform.scale(sky1,(800, 400))

sky2 = pygame.image.load('graphics/Sky2.png').convert_alpha()
sky2 = pygame.transform.scale(sky2,(800, 400))

ground1 = pygame.image.load('graphics/ground1.png')
ground2 = pygame.image.load('graphics/ground2.png')

######### Display buttons #########
Left_arrow = pygame.image.load('Buttons/Left_arrow.png')
Left_arrow = pygame.transform.scale(Left_arrow,(40, 40))

Right_arrow = pygame.image.load('Buttons/Right_arrow.png')
Right_arrow = pygame.transform.scale(Right_arrow,(40, 40))

Space_button = pygame.image.load('Buttons/space.png')
Space_button = pygame.transform.scale(Space_button,(40, 40))

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



# Main game loop
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

while running:
    screen.blit(sky1,(sx,sy))
    screen.blit(sky2,(s2x,s2y))
    screen.blit(ground1,(gx,gy))
    screen.blit(ground2,(g2x,g2y))
    screen.blit(fly,(350,50))
    screen.blit(player,(x , y))

    screen.blit(Left_arrow,(0,0))
    screen.blit(Right_arrow,(40,0))
    screen.blit(Space_button,(80,0))

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
            else: 
                if gx != 800:
                    g2x -= 10
                    if g2x == -800:
                        g2x = 800
                        print("picture ground2 has reach out of screen")
                          

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            spaced()
            sy += 30
            s2y += 30
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

pygame.quit()
sys.exit()