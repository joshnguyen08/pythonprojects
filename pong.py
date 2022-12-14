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
# Set the initial position of the ball to the middle of the screen
BALL_X = SCREEN_WIDTH / 2
BALL_Y = SCREEN_HEIGHT / 2
BALL_VELOCITY = 5

#Define the platform's properties
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 20
PLATFORM_X = SCREEN_WIDTH / 2 - PLATFORM_WIDTH / 2
PLATFORM_Y = SCREEN_HEIGHT - PLATFORM_HEIGHT - BALL_RADIUS

#Set the game loop running at 60 FPS
clock = pygame.time.Clock()

# Define the ball's vertical velocity
BALL_VERTICAL_VELOCITY = 0

# Set the game loop to run indefinitely
while True:
    # Handle events
    for event in pygame.event.get():
    # Update the ball's position
        BALL_X += BALL_VELOCITY
        BALL_Y += BALL_VERTICAL_VELOCITY
    #Check if the ball has hit the top or bottom of the screen
    if BALL_Y + BALL_RADIUS >= SCREEN_HEIGHT or BALL_Y - BALL_RADIUS <= 0:
    #Invert the ball's vertical velocity
        BALL_VERTICAL_VELOCITY = -BALL_VERTICAL_VELOCITY

    # Check if the ball is in contact with the platform
    if BALL_Y + BALL_RADIUS > PLATFORM_Y and BALL_X > PLATFORM_X and BALL_X < PLATFORM_X + PLATFORM_WIDTH:
    # Invert the ball's vertical velocity
        BALL_VERTICAL_VELOCITY = -BALL_VERTICAL_VELOCITY
    # Set the ball's horizontal velocity based on where it hits the platform
        BALL_VELOCITY = (BALL_X - (PLATFORM_X + PLATFORM_WIDTH / 2)) / 10
    # Check for keyboard events
    if event.type == pygame.KEYDOWN:
    # If the left arrow key is pressed
        if event.key == pygame.K_LEFT:
        # Move the platform to the left
            PLATFORM_X -= 10
    # If the right arrow key is pressed
        elif event.key == pygame.K_RIGHT:
        # Move the platform to the right
            PLATFORM_X += 10

    #Check if the user has clicked the "x" button on the window
    if event.type == pygame.QUIT:
        #If so, end the game loop
        break
    # Update the screen
    screen.fill(WHITE)
    pygame.draw.circle(screen, (0, 0, 0), (int(BALL_X), int(BALL_Y)), BALL_RADIUS)
    pygame.draw.rect(screen, (0, 0, 0), (PLATFORM_X, PLATFORM_Y, PLATFORM_WIDTH, PLATFORM_HEIGHT))
    pygame.display.update()

    # Limit the frame rate to 60 FPS
    clock.tick(60)