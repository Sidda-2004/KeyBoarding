import pygame
pygame.init()
# screen setup
white=(255,255,255)
black = (0,0,0)
green=(0,255,0)
WIDTH=500
HEIGHT=700
screen=pygame.display.set_mode(500,700)
pygame.display.set_caption('KEY BOARDING')
turn = 0
board = [[" "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "]]


fps=60
timer=pygame.time.Clock()

def draw_board():
    global turn
    global board
    for col in range(0,7):
        for row in range(0,4):
            pygame.draw.rect(screen,white,[col*100+12,row*100+12,75,75],3,5)
    pygame.draw.rect(screen,green,[5,turn*100+5,WIDTH-10,90],3,5)


running = True
while running:
    timer.tick(fps)
    screen.fill(black)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    pygame.display.flip()