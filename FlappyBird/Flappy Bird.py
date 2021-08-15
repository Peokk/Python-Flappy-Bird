#Importing
import pygame
import sys
import random

#VARIABLE_______________________________________________________________________________________________________________
pygame.init()

#Sounds
fly_sound = pygame.mixer.Sound("audio/wing.ogg")
hit_sound = pygame.mixer.Sound("audio/hit.wav")
point_sound = pygame.mixer.Sound("audio/point.ogg")

#fps
max_fps = 60
clock = pygame.time.Clock()
delta = 0.0

#time
time = 0
time_shadow = 0
fall_time = 0
time_bird = 0

#space pos
x_space = 360
y_space = 180

#bird shadow
x_shadow = 500
y_shadow = 350

#lobby
lobby = 1

#map
map_x = 0

#bird
a = 0
x_bird = 500
y_bird = 350

#fall
fall = 0

#time to change image
time_wings = 0

#colour birds
bird_colour = random.randint(0,2)

#logo x y
logo_x = 300
logo_y = 10

#feathers
feather = 0
f_x = x_bird
f_y = y_bird

#reset
reset = 0
on = 0
single = 0

#speed map
speed = 0

#tubes
tube = []
crash = 0

angle = 0

#Score
score = 0



#Launcher Screen________________________________________________________________________________________________________
screen = pygame.display.set_mode((1100,800))

#map____________________________________________________________________________________________________________________
#Maps
map_d = pygame.image.load('images/map-day.png').convert()
map_n = pygame.image.load('images/map-night.png').convert()

tube_up = pygame.image.load('images/pipe-up.png').convert_alpha()
tube_down = pygame.image.load('images/pipe-down.png').convert_alpha()


#Numbers to score

l0 = pygame.image.load('images/0.png').convert_alpha()
l1 = pygame.image.load('images/1.png').convert_alpha()
l2 = pygame.image.load('images/2.png').convert_alpha()
l3 = pygame.image.load('images/3.png').convert_alpha()
l4 = pygame.image.load('images/4.png').convert_alpha()
l5 = pygame.image.load('images/5.png').convert_alpha()
l6 = pygame.image.load('images/6.png').convert_alpha()
l7 = pygame.image.load('images/7.png').convert_alpha()
l8 = pygame.image.load('images/8.png').convert_alpha()
l9 = pygame.image.load('images/9.png').convert_alpha()

dights = [l0,l1,l2,l3,l4,l5,l6,l7,l8,l9]

#Birds
bird_r1 = pygame.image.load('images/redbird-downflap.png').convert_alpha()
bird_r2 = pygame.image.load('images/redbird-midflap.png').convert_alpha()
bird_r3 = pygame.image.load('images/redbird-upflap.png').convert_alpha()

bird_b1 = pygame.image.load('images/bluebird-downflap.png').convert_alpha()
bird_b2 = pygame.image.load('images/bluebird-midflap.png').convert_alpha()
bird_b3 = pygame.image.load('images/bluebird-upflap.png').convert_alpha()

bird_y1 = pygame.image.load('images/yellowbird-downflap.png').convert_alpha()
bird_y2 = pygame.image.load('images/yellowbird-midflap.png').convert_alpha()
bird_y3 = pygame.image.load('images/yellowbird-upflap.png').convert_alpha()

#Feathers
red_f = pygame.image.load('images/red-feather.png').convert_alpha()
blue_f = pygame.image.load('images/blue-feather.png').convert_alpha()
yellow_f = pygame.image.load('images/yellow-feather.png').convert_alpha()

#Texts
start1 = pygame.image.load('images/start1.png').convert_alpha()
start2 = pygame.image.load('images/start2.png').convert_alpha()


logo = pygame.image.load('images/logo.png').convert_alpha()
game_over = pygame.image.load('images/gameover.png').convert_alpha()
continuation = pygame.image.load('images/Continue.png').convert_alpha()

szary1 = pygame.image.load('images/szary1.png').convert_alpha()
szary2 = pygame.image.load('images/szary2.png').convert_alpha()
szary3 = pygame.image.load('images/szary3.png').convert_alpha()

#Functions______________________________________________________________________________________________________________
for i in range(0,1000):
    x_tube = random.randint(1200 + i*350-i,1300 + i*350-i)
    y_tube = random.randint(200,600)
    tube.append([x_tube,y_tube])
#GAMEPLAY_______________________________________________________________________________________________________________

def fly():
    global x_shadow , lobby , y_shadow , x_space , y_space , y_bird, fall , time_bird , bird_r1 , angle , logo_x , logo_y , feather ,f_x , f_y , fly_sound
    if reset == on:
        if i.type == pygame.KEYDOWN:

            lobby = 0
            x_shadow = 10000
            y_shadow = 10000
            x_space = 10000
            y_space = 10000
            fall = 1
            logo_x = 1000000
            logo_y = 1000000
            feather = 1

            #Do thinks
            pygame.mixer.Sound.stop(fly_sound)
            pygame.mixer.Sound.play(fly_sound)
            for j in range(0,1000):
                time_bird += 1
                angle = 50

                if time_bird > 200:
                    y_bird -= 1

                if time_bird > 202:
                    time_bird = 0


def fal():
    global y_bird , fall_time , f_y , f_x , speed


    if fall == 1:
        fall_time -= 1

        if i.type == pygame.KEYDOWN:
            speed = 1
            fall_time = 8
            f_y += 1
            f_x -= 1

        elif fall_time < 2:
            for j in range(0,6):
                y_bird += 1
                f_y += 1
                f_x -= 1


#LOBBY__________________________________________________________________________________________________________________
def space():
    global time, x_space, y_space, y_bird
    x_space = 360
    y_space = 180

    if lobby == 1:
        time += 1

        if time <= 40:
            screen.blit(start1, (x_space, y_space))
            y_bird += 2

        if time >= 40:
            screen.blit(start2, (x_space, y_space))
            y_bird -= 2

        if time > 80:
            time = 0


def shadow():
    global x_shadow , y_shadow , time_shadow

    if lobby == 1:
        time_shadow += 1

        if time_shadow == 29 or time_shadow == 59 or time_shadow == 89:
            x_shadow += 50
            y_shadow -= 30

        if time_shadow == 30:
            screen.blit(szary1, (x_shadow, y_shadow))

        if time_shadow < 60 and time_shadow > 30:
            screen.blit(szary2, (x_shadow, y_shadow))

        if time_shadow < 120 and time_shadow > 60:
            screen.blit(szary3, (x_shadow, y_shadow))

        if time_shadow > 120:
            time_shadow = 0
            x_shadow = 500
            y_shadow = 350

def logos():
    global logo_x , logo_y
    screen.blit(logo, (logo_x, logo_y))


#ANIMATIONS_____________________________________________________________________________________________________________
def prt_tube():
    global crash , x_bird , y_bird , score
    for now in range(0,1000):
        tube[now][0] -= 2 * speed

        if tube[now][0] < 1200 and tube[now][0] > -100:
            screen.blit(tube_up, (tube[now][0], tube[now][1]))
            screen.blit(tube_down, (tube[now][0], -(900-tube[now][1])))

        if tube[now][0] < 1200 and tube[now][0] > 400:
            do = 0

            if (x_bird > tube[now][0] - 68 and x_bird < tube[now][0] + 100):

                if y_bird >= tube[now][1] - 50:
                        y_bird = 1000
                        pygame.mixer.Sound.stop(hit_sound)
                        pygame.mixer.Sound.play(hit_sound)
                if y_bird <= -(900-tube[now][1]) + 700:
                        y_bird = 1000
                        pygame.mixer.Sound.stop(hit_sound)
                        pygame.mixer.Sound.play(hit_sound)

                if tube[now][0] < 1200 and tube[now][0] > 300:
                    if x_bird == tube[now][0] or x_bird == tube[now][0]+1:

                        score += 1
                        pygame.mixer.Sound.stop(point_sound)
                        pygame.mixer.Sound.play(point_sound)

def maps():
    global map_x , map_d , speed
    screen.blit(map_d, (map_x, 0))

    map_x -= speed

    if map_x == -1100:
        map_x = 0


def restart():
    global  lobby , x_bird , y_bird , fall , x_shadow , y_shadow , logo_x , logo_y ,reset , on , single , speed , x_space , y_space , tube , x_tube , y_tube , score
    if y_bird > 800:
        speed = 0
        x_bird = 5000
        screen.blit(game_over, (350, 200))
        on = 1

        if i.type == pygame.KEYDOWN and single != 1:
            tube = []
            for j in range(0, 1000):
                x_tube = random.randint(1200 + j * 350, 1300 + j * 350)
                y_tube = random.randint(200, 600)
                tube.append([x_tube, y_tube])
            single = 1
            reset = 1
            if reset == 1 and single == 1:
                x_bird = 500
                y_bird = 350

                x_shadow = 500
                y_shadow = 350

                x_space = 360
                y_space = 180

                logo_x = 300
                logo_y = 10

                fall = 0
                lobby = 1

                reset = 0
                single = 0

                score = 0


                for j in range(0,10000000):
                    on += 1
                if on > 10000000:
                    on = 0
                    speed = 0



def wings():
    global time_wings , time_bird, angle , sur_b_1  , sur_b_2  ,sur_b_3
    time_bird += 1

    angle -= 1.5
    if angle > 50:
        angle = 50
    if angle < -60:
        angle = -60

    sur_b_1 = pygame.transform.rotate(bird_b1,angle)
    sur_b_2 = pygame.transform.rotate(bird_b2,angle)
    sur_b_3 =pygame.transform.rotate(bird_b3,angle)

    sur_r_1 = pygame.transform.rotate(bird_r1, angle)
    sur_r_2 = pygame.transform.rotate(bird_r2, angle)
    sur_r_3 = pygame.transform.rotate(bird_r3, angle)

    sur_y_1 = pygame.transform.rotate(bird_y1, angle)
    sur_y_2 = pygame.transform.rotate(bird_y2, angle)
    sur_y_3 = pygame.transform.rotate(bird_y3, angle)

    #red
    if bird_colour == 0:
        if time_bird < 50:

            screen.blit(sur_r_1, (x_bird, y_bird-5))
        if time_bird > 50 and time_bird < 100:
            screen.blit(sur_r_2, (x_bird, y_bird))

        if time_bird > 100 and time_bird < 150:
            screen.blit(sur_r_3, (x_bird, y_bird-5))

        if time_bird > 150:
            screen.blit(sur_r_2, (x_bird, y_bird))

    #yellow
    if bird_colour == 1:
        if time_bird < 50:
            screen.blit(sur_y_1, (x_bird, y_bird - 5))

        if time_bird > 50 and time_bird < 100:
            screen.blit(sur_y_2, (x_bird, y_bird))

        if time_bird > 100 and time_bird < 150:
            screen.blit(sur_y_3, (x_bird, y_bird - 5))

        if time_bird > 150:
            screen.blit(sur_y_2, (x_bird, y_bird))

        #blue
    if bird_colour == 2:
        if time_bird < 50:
            screen.blit(sur_b_1, (x_bird, y_bird - 5))

        if time_bird > 50 and time_bird < 100:
            screen.blit(sur_b_2, (x_bird, y_bird))

        if time_bird > 100 and time_bird < 150:
            screen.blit(sur_b_3, (x_bird, y_bird - 5))

        if time_bird > 150:
            screen.blit(sur_b_2, (x_bird, y_bird))

    #RESTART TIME
    if time_bird > 200:
        time_bird = 0

def feathers():
    global bird_colour , feather , f_x , f_y , a , b
    a = 0
    b = 0
    if feather == 1:
        for j in range(0, 1):
            a = random.randint(-200,200)
            b = random.randint(0,200)
            #RED
            if bird_colour == 0:
                screen.blit(red_f, (f_x-a, f_y-b))


            #YELLOW
            if bird_colour == 1:
                screen.blit(yellow_f, (f_x-a, f_y-b))

            #BLUE
            if bird_colour == 2:
                screen.blit(blue_f, (f_x-a, f_y-b))

            if f_y > 900:
                feather = 0
                f_x = x_bird
                f_y = y_bird

def numbers():
    global score
    screen.blit(dights[int(score / 100)%10], (10, 10))
    screen.blit(dights[int((score / 10) % 10)], (60,10))
    screen.blit(dights[int(score % 10)], (110, 10))





#Loop___________________________________________________________________________________________________________________
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit(0)

#Before Ticking_________________________________________________________________________________________________________

#Ticking________________________________________________________________________________________________________________
    delta += clock.tick() / 1000.0
    while delta > 1 / max_fps:
        delta -= 1 / max_fps
#Performing functions___________________________________________________________________________________________________
        #Showing
        maps()
        prt_tube()
        logos()
        shadow()
        space()
        wings()
        numbers()
        fly()
        fal()
        wings()
        restart()
        pygame.display.update()
#Drawing________________________________________________________________________________________________________________