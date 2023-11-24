import pygame
import sys
import random

pygame.init()
screen_width, screen_height = 800, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

# Load images
sky1 = pygame.image.load('graphics/Sky1.png').convert_alpha()
sky1 = pygame.transform.scale(sky1, (screen_width, screen_height))

sky2 = pygame.image.load('graphics/Sky2.png').convert_alpha()
sky2 = pygame.transform.scale(sky2, (screen_width, screen_height))

ground1 = pygame.image.load('graphics/ground1.png')
ground2 = pygame.image.load('graphics/ground2.png')

player_images = ['graphics/player1.png', 'graphics/player2.png', 'graphics/player3.png']
fly_images = ['graphics/Fly1.png', 'graphics/Fly2.png', 'graphics/Fly1.png']

player_index = 0
fly_index = 0
player = pygame.image.load(player_images[player_index])
fly = pygame.image.load(fly_images[fly_index])

# Set up constants
PLAYER_MOVEMENT = pygame.USEREVENT + 1
FLY_MOVEMENT = pygame.USEREVENT + 2
SKY_MOVEMENT = pygame.USEREVENT + 3
GROUND_MOVEMENT = pygame.USEREVENT + 4
CUSTOM_EVENT = pygame.USEREVENT + 5
DISTANCE_COUNTER = pygame.USEREVENT + 6

speed = 200
pygame.time.set_timer(PLAYER_MOVEMENT, 400)
pygame.time.set_timer(FLY_MOVEMENT, 100)
pygame.time.set_timer(SKY_MOVEMENT, 20)
pygame.time.set_timer(GROUND_MOVEMENT, 15)
pygame.time.set_timer(CUSTOM_EVENT, 4)
pygame.time.set_timer(DISTANCE_COUNTER, speed)

# Set up fonts
font1 = pygame.font.SysFont("None", 60)
font2 = pygame.font.SysFont("None", 40)
font3 = pygame.font.SysFont("None", 30)
font4 = pygame.font.SysFont("None", 30)

# Set up text
text1 = font1.render('Welcome To Runner', True, 'Black')
text2 = font2.render('controls for this game are:', True, 'Black')
text3 = font3.render('Press space to start', True, 'Black')
text4 = font4.render('', True, 'Black')

txx1, txy1 = 202, 120
txx2, txy2 = 200, 350
txx3, txy3 = 304, 210
lax, lay = 560, 343
rax, ray = 615, 343
spx, spy = 670, 343

# Initialize variables
start = False
space = False
space1 = False
space2 = False
right = False
left = False
x, y = 30, 220
sx, sy = 0, -80
s2x, s2y = 800, -80
gx, gy = 0, 298
g2x, g2y = 800, 298
fly_x = -60
ran_fly_pos = 230
score = 0
high_score = 0
game_over = False

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == PLAYER_MOVEMENT:
            player_index = (player_index + 1) % len(player_images)
            player = pygame.image.load(player_images[player_index])

        if event.type == FLY_MOVEMENT:
            fly_index = (fly_index + 1) % len(fly_images)
            fly = pygame.image.load(fly_images[fly_index])

        if event.type == FLY_MOVEMENT:
            fly_x -= 4
            if fly_x <= -84:
                ran_fly_pos = random.randint(190, 258)
                fly_x = 884

        if event.type == SKY_MOVEMENT:
            sx -= 5
            if sx <= -805:
                sx = 800
            else:
                if sx != 800:
                    s2x -= 5
                    if s2x == -800:
                        s2x = 800

        if event.type == GROUND_MOVEMENT:
            gx -= 5
            if gx <= -805:
                gx = 800
            else:
                if gx != 800:
                    g2x -= 5
                    if g2x == -800:
                        g2x = 800

        if event.type == DISTANCE_COUNTER:
            score += 1

        if event.type == CUSTOM_EVENT and space:
            space1 = True
            if y != 60 and space1 and not space2:
                y -= 2
            if y != 220 and space2:
                y += 2

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                space = True

            if event.key == pygame.K_RIGHT:
                right = True

            elif event.key == pygame.K_LEFT:
                left = True

    if start:
        if right:
            x += 20
            right = False

        if left:
            x -= 20
            left = False

    if game_over:
        game_over = False
        if score > high_score:
            high_score = score
        x, y = 30, 220
        space = False
        space1 = False
        space2 = False

    game_over_rect = player.get_rect(topleft=(x, y)).colliderect(
        pygame.Rect(fly_x, ran_fly_pos, 40, 20)
    )
    if game_over_rect:
        print("Game Over!")
        game_over = True
        start = False

    screen.blit(sky1, (sx, sy))
    screen.blit(sky2, (s2x, s2y))
    screen.blit(ground1, (gx, gy))
    screen.blit(ground2, (g2x, g2y))
    screen.blit(fly, (fly_x, ran_fly_pos))
    screen.blit(player, (x, y))
    text4 = font4.render(f'Distance: {score} m', True, 'Black')
    text5 = font4.render(f'Highscore: {high_score} m', True, 'Black')
    screen.blit(text5, (250, 0))

    pygame.display.update()
    clock.tick(360)
