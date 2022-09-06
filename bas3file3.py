# !/usr/bin/python
# -*- coding: utf-8 -*-

from p5 import *
from random import randint

# Taille des cubes (pix)
TAILLE_CUBE = 100
# Espace entre les cubes (pix)
ESPACE_CUBE = 20
# Position des centres des cubes sur une direction
POSITIONS = [-(TAILLE_CUBE+ESPACE_CUBE), 0, TAILLE_CUBE+ESPACE_CUBE]
print('POSITIONS = ', POSITIONS)

COULEUR_ARRETE = 'yellow'

def setup():
    background(0)
    size(1280, 720)
    fill(0)

    
def draw():
    background(0, 0, 0)
    fill(0, 0, 0)
    fill(randint(100, 255), randint(100, 255), randint(100, 255))
    #blinn_phong_material()

    rotate_x(frame_count * 0.05)
    rotate_y(frame_count * 0.05)

    # tracer les ligne des axes
        
    for x in POSITIONS:
        for y in POSITIONS:
            for z in POSITIONS:
                with push_matrix():
                    stroke(randint(100, 255), randint(100, 255), randint(100, 255))
                    stroke_weight(100)
                    no_stroke()
                    fill(randint(100, 255), randint(100, 255), randint(100, 255))

                    #blinn_phong_material()
                    translate(x, y, z)
                    box(TAILLE_CUBE, TAILLE_CUBE, TAILLE_CUBE)
    
    with push_matrix():
        #blinn_phong_material()
        stroke(randint(100, 255), randint(100, 255), randint(100, 255))
        translate(400, 0, 0)
        sphere(200, detail_x=10, detail_y=10)

    with push_matrix():
        #blinn_phong_material()
        translate(-400, 0, 0)
        fill(255, 255, 255)
        stroke_weight(20)
        strokeWeight(20)
        stroke(randint(100, 255), 0, randint(200, 255))
        plane(400, 400)

if __name__ == '__main__':
    run(mode='P3D')

