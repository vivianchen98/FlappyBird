# Shenghui Chen(sc9by)
# This program is to mimic game flappy bird using gamebox.py and pygame module in python

import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)
character = gamebox.from_image(200, 300, "transparent_flappy_bird.gif")
character.scale_by(0.3)

walls = [

    [gamebox.from_color(300, 150, "black", 50, 300), gamebox.from_color(300, 650, "black", 50, 300)],
    [gamebox.from_color(500, 100, "black", 50, 300), gamebox.from_color(500, 600, "black", 50, 300)],
    [gamebox.from_color(700, 50, "black", 50, 300), gamebox.from_color(700, 550, "black", 50, 300)],
    [gamebox.from_color(900, 80, "black", 50, 300), gamebox.from_color(900, 580, "black", 50, 300)],
]
counter = 0
game_on = False
time = 0

def tick(keys):
    global counter
    global game_on
    global time
    camera.clear('white')


    if pygame.K_SPACE in keys:
        gamebox.unpause()
        game_on = True

    # input
    if game_on:
        camera.x += 3
        if camera.mouseclick:
            character.y -= 25
        character.x += 3
        character.y += 5

        counter += 1
        if counter > 60 and counter % 60 == 0:
            random_height = random.randint(50, 150)
            new_wall = [gamebox.from_color(camera.x + 350, random_height, "black", 50, 300),
                        gamebox.from_color(camera.x + 350, random_height + 500, "black", 50, 300)]
            walls.append(new_wall)  # wall list continues to grow'''
            del walls[0]

        #timing
        time += 1

    seconds = str(int((time / ticks_per_second))).zfill(3)
    time_box = gamebox.from_text(camera.x+200, camera.y-250, "Playing Time: " + seconds + " s", "arial", 24, "red")

    # draw methods
    camera.draw(character)
    for pair in walls:
        for wall in pair:
            if wall.touches(character, -10,-10):
                character.move_to_stop_overlapping(wall)
                character.speedy = 4
                game_on = False
                camera.draw(gamebox.from_text(camera.x, camera.y, "Game over!", "Arial", 40, "Red", True))
                gamebox.pause()
            camera.draw(wall)
    camera.draw(time_box)

    camera.display()

ticks_per_second = 30

gamebox.timer_loop(ticks_per_second, tick)