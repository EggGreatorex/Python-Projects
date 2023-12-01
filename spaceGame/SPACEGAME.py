from random import randint
import pygame
import time
from sys import  exit

def main():
        pygame.init()

        #function
        def display_score():
            current_time  = int(pygame.time.get_ticks() / 1000) - start_time   # Gets time since game start rounded to seconds
            score_surface = test_font.render(f'Score:{current_time}',False,(64,64,64)) # gets colour and font for time and converts to string
            score_rectangle = score_surface.get_rect(center = (600,60))
            screen.blit(score_surface, score_rectangle)
            return  current_time


        # Starting variables

        screen = pygame.display.set_mode((1200, 600))
        clock = pygame.time.Clock()
        wkeydown = False
        skeydown = False
        rockspeed = 4
        start_time = 0
        score = 0
        hearts = 3
        game_active = False
        test_font = pygame.font.Font("./assests/Pixeltype.ttf", 100)

        # Surfaces
        space = pygame.image.load("./assests/space.png").convert_alpha()
        space_rectangle = space.get_rect(midbottom = (0,0))

        spaceship = pygame.image.load("./assests/Rocket.png").convert_alpha()
        spaceship = pygame.transform.scale(spaceship, (50,90))
        spaceship = pygame.transform.rotate(spaceship, -90)
        spaceship_rectangle = spaceship.get_rect(midbottom = (300, 600))



        laser = pygame.image.load("./assests/Laser.png").convert_alpha()
        laser = pygame.transform.rotate(laser, 90)
        laser = pygame.transform.scale(laser, (30, 30))
        laser_rectangle = laser.get_rect(center= (300, 500))

        #coding for heart
        heart1 = pygame.image.load("./assests/heart pixel art 32x32.png").convert_alpha()
        heart2 = pygame.image.load("./assests/heart pixel art 32x32.png").convert_alpha()
        heart3 = pygame.image.load("./assests/heart pixel art 32x32.png").convert_alpha()
        heart1_rectangle = heart1.get_rect(midbottom = (550, 40))
        heart2_rectangle = heart2.get_rect(midbottom = (600, 40))
        heart3_rectangle = heart3.get_rect(midbottom = (650, 40))

        #Earth for main menu
        earth = pygame.image.load("./assests/Earth.png")
        earth = pygame.transform.scale(earth, (1000,800))
        earth_rectangle = earth.get_rect(center = (600,700))

        #spaceman for main menu
        spaceman = pygame.image.load("./assests/Spaceman.png")
        spaceman = pygame.transform.scale(spaceman, (100,100))
        spaceman = pygame.transform.rotate(spaceman, (-45))
        spaceman_rectangle = spaceman.get_rect(center = (150, 150))




        # Coding for rock
        rock = pygame.image.load("./assests/Rock.png").convert_alpha()
        rock = pygame.transform.scale(rock, (60,60))
        rock_rectangle=rock.get_rect(center= (randint(1300,1500), randint(0, 550)))
        #rockX = rock_rectangle.x
        #rockY = rock_rectangle.y
        #rock_hitbox = (rockX , rockY, 109, 109)
        #pygame.draw.rect(screen, (255,0,0), rock_hitbox, 3)

        rock2= pygame.image.load("./assests/Rock.png").convert_alpha()
        rock2 = pygame.transform.scale(rock2, (80,80))
        rock2_rectangle=rock2.get_rect(center= (randint(1300,1500), randint(0, 550)))
        # rock2X = rock2_rectangle.x
        # rock2Y = rock2_rectangle.y
        # rock2_hitbox = (rock2X , rock2Y, 80, 80)

        rock3 = pygame.image.load("./assests/Rock.png").convert_alpha()
        rock3 = pygame.transform.scale(rock3, (100,100))
        rock3_rectangle=rock3.get_rect(center= (randint(1800,1900), randint(0, 550)))
        # rock3X = rock3_rectangle.x
        # rock3Y = rock3_rectangle.y
        # rock3_hitbox = (rock3X , rock3Y, 80, 80)

        rock4 = pygame.image.load("./assests/Rock.png").convert_alpha()
        rock4 = pygame.transform.scale(rock4, (100,100))
        rock4_rectangle=rock4.get_rect(center= (randint(1800,1900), randint(0, 550)))
        # rock4X = rock4_rectangle.x
        # rock4Y = rock4_rectangle.y
        # rock4_hitbox = (rock4X , rock4Y, 100, 100)

        rock5 = pygame.image.load("./assests/Rock.png").convert_alpha()
        rock5 = pygame.transform.scale(rock5, (80,80))
        rock5_rectangle=rock5.get_rect(center= (randint(10000,11000), randint(0, 550)))
        # rock5X = rock5_rectangle.x
        # rock5Y = rock5_rectangle.y
        # rock5_hitbox = (rock5X , rock5Y, 80, 80)

        rock6 = pygame.image.load("./assests/Rock.png").convert_alpha()
        rock6 = pygame.transform.scale(rock6, (90,90))
        rock6_rectangle=rock6.get_rect(center= (randint(1450,1500), randint(0, 550)))
        # rock6X = rock6_rectangle.x
        # rock6Y = rock6_rectangle.y
        # rock6_hitbox = (rock6X , rock6Y, 60, 60)

        rock7 = pygame.image.load("./assests/Rock.png").convert_alpha()
        rock7 = pygame.transform.scale(rock7, (100,100))
        rock7_rectangle =rock7.get_rect(center= (randint(1450,1550), randint(0, 550)))
        # rock7X = rock7_rectangle.x
        # rock7Y = rock7_rectangle.y
        # rock7_hitbox = (rock7X , rock7Y, 100, 100)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Quits the game
                    pygame.quit()
                    exit()

                if game_active:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:
                            wkeydown = True
                        if event.key == pygame.K_s:
                            skeydown = True


                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_w:
                            wkeydown = False
                        if event.key == pygame.K_s:
                            skeydown = False
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            hearts = 3
                            rockspeed = 4
                            start_time = int(pygame.time.get_ticks() / 1000)
                            rock_rectangle.left = randint(1300, 1500)
                            rock_rectangle.top = randint(30, 400)
                            rock2_rectangle.left = randint(1370, 1550)
                            rock2_rectangle.top = randint(30, 400)
                            rock3_rectangle.left = randint(1800, 1900)
                            rock3_rectangle.top = randint(30, 400)
                            rock4_rectangle.left = randint(10000, 11000)
                            rock4_rectangle.top = randint(30, 400)
                            rock5_rectangle.left = randint(10050, 11050)
                            rock5_rectangle.top = randint(30, 400)
                            rock6_rectangle.left = randint(1450, 1500)
                            rock6_rectangle.top = randint(30, 400)
                            rock7_rectangle.left = randint(1450, 1550)
                            rock7_rectangle.top = randint(30, 400)
                            heart1_rectangle.midbottom = (550,40)
                            heart2_rectangle.midbottom = (600,40)
                            heart3_rectangle.midbottom = (650,40)
                            game_active = True


            if (wkeydown):
                spaceship_rectangle.y -=4
            if (skeydown):
                spaceship_rectangle.y +=4

            pygame.display.set_caption("SPACE GAME")

            if game_active:

                screen.blit(space,(0,0))
                screen.blit(spaceship, spaceship_rectangle)
                score = display_score()
                spaceX = spaceship_rectangle.x
                spaceY = spaceship_rectangle.y
                spaceship_hitbox = (spaceX, spaceY, 90, 50)
                screen.blit(heart1,heart1_rectangle)
                screen.blit(heart2, heart2_rectangle)
                screen.blit(heart3, heart3_rectangle)

                screen.blit(rock, rock_rectangle)
                screen.blit(rock2, rock2_rectangle)
                screen.blit(rock3, rock3_rectangle)
                screen.blit(rock4, rock4_rectangle)
                screen.blit(rock5, rock5_rectangle)
                screen.blit(rock6, rock6_rectangle)
                screen.blit(rock7, rock7_rectangle)

                #Rock movements
                rock_rectangle.x -= rockspeed

                rockX = rock_rectangle.x
                rockY = rock_rectangle.y
                rock_hitbox = (rockX, rockY,60,60)


                rock2_rectangle.x -= rockspeed
                rock2X = rock2_rectangle.x
                rock2Y = rock2_rectangle.y
                rock2_hitbox = (rock2X, rock2Y, 80, 80)


                rock3_rectangle.x -= rockspeed
                rock3X = rock3_rectangle.x
                rock3Y = rock3_rectangle.y
                rock3_hitbox = (rock3X, rock3Y, 100, 100)


                rock4_rectangle.x -= rockspeed
                rock4X = rock4_rectangle.x
                rock4Y = rock4_rectangle.y
                rock4_hitbox = (rock4X, rock4Y, 100, 100)


                rock5_rectangle.x -= rockspeed
                rock5X = rock5_rectangle.x
                rock5Y = rock5_rectangle.y
                rock5_hitbox = (rock5X, rock5Y, 80, 80)


                rock6_rectangle.x -= rockspeed
                rock6X = rock6_rectangle.x
                rock6Y = rock6_rectangle.y
                rock6_hitbox = (rock6X, rock6Y, 90, 90)


                rock7_rectangle.x -= rockspeed
                rock7X = rock7_rectangle.x
                rock7Y = rock7_rectangle.y
                rock7_hitbox = (rock7X, rock7Y, 100, 100)


                if rock_rectangle.right < 0:
                    rock_rectangle.left = randint(1300, 1500)
                    rock_rectangle.top = randint(0,500)

                if rock2_rectangle.right < 0:
                    rock2_rectangle.left = randint(1370, 1550)
                    rock2_rectangle.top = randint(0,500)
                if rock3_rectangle.right < 0:
                    rock3_rectangle.left = randint(1800, 1900)
                    rock3_rectangle.top = randint(0, 500)
                if rock4_rectangle.right < 0:
                    rock4_rectangle.left = randint(10000, 11000)
                    rock4_rectangle.top = randint(0, 500)
                if rock5_rectangle.right < 0:
                    rock5_rectangle.left = randint(10050, 11050)
                    rock5_rectangle.top = randint(0, 500)
                if rock6_rectangle.right < 0:
                    rock6_rectangle.left = randint(1450, 1500)
                    rock6_rectangle.top = randint(0, 500)
                if rock7_rectangle.right < 0:
                    rock7_rectangle.left = randint(1450, 1550)
                    rock7_rectangle.top = randint(0, 500)


                rockspeed +=0.002


                # stop rocket if goes out of border
                if spaceship_rectangle.top < 50:
                    spaceship_rectangle.top = 50

                if spaceship_rectangle.bottom > 550:
                    spaceship_rectangle.bottom = 550

                # Check for collision with rock and if so remove a heart from rocket
                if spaceship_rectangle.colliderect(rock_hitbox):
                    rock_rectangle.left = randint(1300, 1500)
                    rock_rectangle.top = randint(0, 400)
                    hearts -=1
                elif spaceship_rectangle.colliderect(rock2_hitbox):
                    rock2_rectangle.left = randint(1370, 1550)
                    rock2_rectangle.top = randint(0, 400)
                    hearts -=1
                elif spaceship_rectangle.colliderect(rock3_hitbox):
                    rock3_rectangle.left = randint(1800, 1900)
                    rock3_rectangle.top = randint(0, 400)
                    hearts -=1
                elif spaceship_rectangle.colliderect(rock4_hitbox):
                    rock4_rectangle.left = randint(10000, 11000)
                    rock4_rectangle.top = randint(0, 400)
                    hearts -=1
                elif spaceship_rectangle.colliderect(rock5_hitbox):
                    rock5_rectangle.left = randint(10050, 11050)
                    rock5_rectangle.top = randint(0, 400)
                    hearts -=1
                elif spaceship_rectangle.colliderect(rock6_hitbox):
                    rock6_rectangle.left = randint(1450, 1500)
                    rock6_rectangle.top = randint(0, 400)
                    hearts -=1
                elif spaceship_rectangle.colliderect(rock7_hitbox):
                    rock7_rectangle.left = randint(1450, 1550)
                    rock7_rectangle.top = randint(0, 400)
                    hearts -=1

                # check if lost any hearts if so remove a heart from screen
                if hearts == 2:
                    heart3_rectangle.left = 1300

                elif hearts == 1:
                    heart2_rectangle.left = 1300

                elif hearts == 0:
                    game_active = False

            else:
                screen.fill(('black'))
                screen.blit(earth, earth_rectangle)
                screen.blit(spaceman, spaceman_rectangle)
                score_message = test_font.render(f'Your Score Was: {score}', False, (111, 196, 169))
                play_again = test_font.render('Press SPACE To Play Again', False, (111,196,169))
                play_again_rectangle = play_again.get_rect(center = (600, 180))
                score_message_rectangle = score_message.get_rect(center=(600, 250))
                if score == 0:
                    welcome = test_font.render('Welcome! To Space Game!!',False, (111,196,169))
                    welcome_recangle = welcome.get_rect(center = (600, 180))
                    message = test_font.render('Press SPACE To Start', False, (111, 196, 169))
                    message_rectangle = message.get_rect(center=(600, 250))
                    screen.blit(message, message_rectangle)
                    screen.blit(welcome, welcome_recangle)
                else:
                    screen.blit(score_message, score_message_rectangle)
                    screen.blit(play_again, play_again_rectangle)



            pygame.display.update() # Keep display running
            clock.tick(60)  # Caps fps at 60

main()