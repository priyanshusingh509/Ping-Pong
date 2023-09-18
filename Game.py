import time
import pygame,random,distance
# Initialize
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Pong Ball')
game_over = pygame.image.load('gameover.jpg')
score = 0
font = pygame.font.Font("ka1.ttf",15)
font2 = pygame.font.Font("ka1.ttf",30)
# Bat1 Initialization
bat1 = pygame.image.load('bat1.png')
bat1_x = 10
bat1_y = 270
bat1_speed = 0
time.sleep(4)
# Bat2 Initialization
bat2 = pygame.image.load('bat2.png')
bat2_x = 780
bat2_y = 270
bat2_speed = 0

# Ball Initialization
ball = pygame.image.load('ball.png')
ball_x = 360
ball_y = 300

# Score
def score_show(x,y):
    score_text = font.render(f'Score: {score}',True,(255,255,255))
    screen.blit(score_text,(x,y))

# Bat1 Path
def bat1_path(x,y):
    screen.blit(bat1,(x,y))

# Bat2 Path
def bat2_path(x,y):
    screen.blit(bat1,(x,y))

# Ball Path
if score <=5:
    Path_Options = [(-0.3,-0.3),(0.3,-0.3), (0.3,-0.3),   (0.3,0.3)]
elif score <=10:
    Path_Options = [(-0.4,-0.4),(0.4,-0.4), (0.4,-0.4),   (0.4,0.4)]
else:
    Path_Options = [(-0.6,-0.6),(0.6,-0.6), (0.6,-0.6),   (0.6,0.6)]
#                  UpLEFT     UpRIGHT    DownLEFT      DownRIGHT
Start = random.choice(Path_Options)
ball_change_x = Start[0]
ball_change_y = Start[1]
def ball_path(x,y):
    global ball_x,ball_y
    ball_x = ball_x + ball_change_x
    ball_y = ball_y + ball_change_y
    screen.blit(ball,(x,y))
    
# Game Start
running  = True
while running:
    screen.fill('black')
    for event in pygame.event.get():
        # QUIT
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            # Bat1 Controls
            if event.key == pygame.K_w:
                bat1_speed=-0.7
            if event.key == pygame.K_s:
                bat1_speed=0.7
            # Bat2 Controls
            if event.key == pygame.K_UP:
                bat2_speed=-0.7
            if event.key == pygame.K_DOWN:
                bat2_speed=0.7
            if event.key == pygame.K_LCTRL:
                print(ball_y,bat2_y,distance.distance(ball_y,bat2_y))
                print(distance.distance(ball_x,bat2_x))
        # Key Release
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                bat1_speed =0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                bat2_speed =0

    # Summon Interface
    score_show(5,5)
    bat1_path(bat1_x,bat1_y)
    bat2_path(bat2_x,bat2_y)
    ball_path(ball_x,ball_y)
    
    # Bat Movement
    bat1_y+=bat1_speed
    bat2_y+=bat2_speed
    
    # Bat1 Constrictions
    if bat1_y>=500:
        bat1_y=499
    if bat1_y<=-1:
        bat1_y=0
    
    # Bat2 Constrictions
    if bat2_y>=500:
        bat2_y=499
    if bat2_y<=-1:
        bat2_y=0

    # Ball Constrictions
    if ball_y>=565:
        ball_y=564
        ball_change_y = eval('-'+str(ball_change_y))
    if ball_y<=-1:
        ball_y=0
        ball_change_y = eval('-'+str(ball_change_y))

    # Hit Logic
    if distance.distance(ball_x,bat1_x)<=6 and distance.distance(ball_y,bat1_y)<=68:
        ball_x+=2
        ball_change_x = eval('-'+str(ball_change_x))
        score+=1
    if distance.distance(ball_x,bat2_x)<=32 and distance.distance(ball_y,bat2_y)<=68:
        ball_x-=2
        ball_change_x = eval('-'+str(ball_change_x))
        score+=1
    # Game Over
    if ball_x>780 or ball_x<0:
        screen.blit(game_over,(0,0))
        score_text = font2.render(f'Score: {score}',True,(255,255,255))
        screen.blit(score_text,(10,10))
    pygame.display.update()