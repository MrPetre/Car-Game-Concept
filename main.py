# Import the pygame library and initialize the game engine
import pygame, random
pygame.init()

# Import the Car class
from car import Car

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
GREY = (188, 188, 188)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)

speed = 1
colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE)

# Open a new window
SCREENWIDTH = 800
SCREENHEIGHT = 600

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Car Racing")

# This will be a list that will contain all the sprites we intend to use in our game
all_sprites_list = pygame.sprite.Group()

playerCar = Car(RED, 60, 20, 30)
playerCar.rect.x = 160
playerCar.rect.y = SCREENHEIGHT - 100

car1 = Car(PURPLE, 60, 80, random.randint(50, 100))
car1.rect.x = 60
car1.rect.y = 100

car2 = Car(PURPLE, 60, 80, random.randint(50, 100))
car2.rect.x = 160
car2.rect.y = 600

car3 = Car(PURPLE, 60, 80, random.randint(50, 100))
car3.rect.x = 260
car3.rect.y = 300

car4 = Car(PURPLE, 60, 80, random.randint(50, 100))
car4.rect.x = 360
car4.rect.y = 900

# Add the car to the list of objects
all_sprites_list.add(playerCar)
all_sprites_list.add(car1)
all_sprites_list.add(car2)
all_sprites_list.add(car3)
all_sprites_list.add(car4)

all_coming_cars = pygame.sprite.Group()
all_coming_cars.add(car1)
all_coming_cars.add(car2)
all_coming_cars.add(car3)
all_coming_cars.add(car4)

# The loop will carry on until the user exits the game (eg. clicks the close button)
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# ---------- Main Program Loop ----------
while carryOn:
    # ---- Main Event Loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            carryOn = False # Flag that we are done so we can exit the while loop
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x:
                carryOn = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and playerCar.rect.x > 0:
        playerCar.moveLeft(5)
    if keys[pygame.K_RIGHT] and playerCar.rect.x < SCREENWIDTH - 60:
        playerCar.moveRight(5)
    if keys[pygame.K_UP]:
        speed += 0.05
    if keys[pygame.K_DOWN]:
        speed -= 0.05


    # ---- Game logic
    for car in all_coming_cars:
        car.moveForward(speed)
        if car.rect.y > SCREENHEIGHT:
            car.changeSpeed(random.randint(50, 100))
            car.repaint(random.choice(colorList))
            car.rect.y = -200

    # Check if there is a car collision
        car_collision_list = pygame.sprite.spritecollide(playerCar, all_coming_cars, False)
        for car in car_collision_list:
            print("Car crash!")
            # End of game
            carryOn = False

    all_sprites_list.update()

    # ---- Drawing on screen
    screen.fill(GREEN)

    # ---- Draw the road
    pygame.draw.rect(screen, GREY, [40, 0, 400, SCREENHEIGHT])

    # --- Line painting on the road
    pygame.draw.line(screen, WHITE, [140, 0], [140, SCREENHEIGHT], 5)
    pygame.draw.line(screen, WHITE, [240, 0], [240, SCREENHEIGHT], 5)
    pygame.draw.line(screen, WHITE, [340, 0], [340, SCREENHEIGHT], 5)

    # Now let's draw all the psrites in one go. (For now we only have 1 sprite)
    all_sprites_list.draw(screen)

    # ---- Go ahead and update the screen with what we've drawn
    pygame.display.flip()

    # ---- Limit to 60fps
    clock.tick(60)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()