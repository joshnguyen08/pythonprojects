#Import the necessary modules
import sys
import pygame

#Initialize the game
pygame.init()

#Set the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Set the file path to the image file
file_path = "C:\\Users\\lyfeo\\Desktop\\pong_icon.png"
#Load the image file
icon = pygame.image.load(file_path)
#Set the title and icon
pygame.display.set_caption("Pong")
pygame.display.set_icon(icon)

#Set the colors
WHITE = (255, 255, 255)

#Define the ball's properties
BALL_RADIUS = 20
#Set the initial position of the ball to the middle of the screen
BALL_X = SCREEN_WIDTH / 2
BALL_Y = SCREEN_HEIGHT / 2
BALL_VELOCITY = 5

#Define the platform's properties
PLATFORM_WIDTH = 200
PLATFORM_HEIGHT = 20
PLATFORM_X = SCREEN_WIDTH / 2 - PLATFORM_WIDTH / 2
PLATFORM_Y = SCREEN_HEIGHT - PLATFORM_HEIGHT - BALL_RADIUS

#Set the game loop running at 60 FPS
clock = pygame.time.Clock()

#Define the ball's vertical velocity
BALL_VERTICAL_VELOCITY = 5
#Define platform's velocity
PLATFORM_VELOCITY = 5

#Run game loop indefinitely
while True:
    #Handle events
    for event in pygame.event.get():
        #Check for keyboard events
        if event.type == pygame.KEYDOWN:
            #If the left arrow key is pressed
            if event.key == pygame.K_LEFT:
                #Set the platform's velocity to move left
                PLATFORM_VELOCITY = -15
            #If the right arrow key is pressed
            elif event.key == pygame.K_RIGHT:
                #Set the platform's velocity to move right
                PLATFORM_VELOCITY = 15
        #Check for KEYUP event
        elif event.type == pygame.KEYUP:
            #Set the platform's velocity to 0
            PLATFORM_VELOCITY = 0
    #Update the platform's position based on its velocity
    PLATFORM_X += PLATFORM_VELOCITY

    #Update the ball's position
    BALL_X += BALL_VELOCITY
    BALL_Y += BALL_VERTICAL_VELOCITY
    #Check if the ball has hit the left or right edges of the screen
    if BALL_X + BALL_RADIUS >= SCREEN_WIDTH or BALL_X - BALL_RADIUS <= 0:
        #Invert the ball's horizontal velocity
        BALL_VELOCITY = -BALL_VELOCITY
    #Check if the platform has reached the left edge of the screen
    if PLATFORM_X <= 0:
        #If so, set its position to the left edge of the screen
        PLATFORM_X = 0

    #Check if the platform has reached the right edge of the screen
    if PLATFORM_X + PLATFORM_WIDTH >= SCREEN_WIDTH:
        #If so, set its position to the right edge of the screen
        PLATFORM_X = SCREEN_WIDTH - PLATFORM_WIDTH

    #Check if the ball has hit the top or bottom of the screen
    if BALL_Y + BALL_RADIUS >= SCREEN_HEIGHT or BALL_Y - BALL_RADIUS <= 0:
        #Invert the ball's vertical velocity once it touches border of game window
        BALL_VERTICAL_VELOCITY = -BALL_VERTICAL_VELOCITY

    #Check if the ball is in contact with the platform
    if BALL_Y + BALL_RADIUS > PLATFORM_Y and BALL_X > PLATFORM_X and BALL_X < PLATFORM_X + PLATFORM_WIDTH:
        #Invert the ball's vertical velocity, once it touches platform
        BALL_VERTICAL_VELOCITY = -BALL_VERTICAL_VELOCITY
        #Set the ball's horizontal velocity based on where it hits the platform
        BALL_VELOCITY = (BALL_X - (PLATFORM_X + PLATFORM_WIDTH / 2)) / 10
        #Check if the user has clicked the "x" button on the window
    if event.type == pygame.QUIT:
        #If so, end game loop
        break
    #Update the screen
    screen.fill(WHITE)
    pygame.draw.circle(screen, (0, 0, 0), (int(BALL_X), int(BALL_Y)), BALL_RADIUS)
    pygame.draw.rect(screen, (0, 0, 0), (PLATFORM_X, PLATFORM_Y, PLATFORM_WIDTH, PLATFORM_HEIGHT))
    pygame.display.update()

    #60 FPS 
    clock.tick(60)