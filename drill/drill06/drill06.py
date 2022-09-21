from pico2d import * #몽땅 다 pico2d import 해라 
import math
open_canvas()
grass = load_image("grass.png")
character = load_image('character.png')
x = 0
y= 90
theta =0    
while True:
    theta = -90
    while x < 700:
        clear_canvas_now()
        character.draw_now(x,y)
        grass.draw_now(400,30)
        x+=2
        delay(0.001)
    while y < 500:
        clear_canvas_now()
        character.draw_now(x,y)
        grass.draw_now(400,30)
        y+=2
        delay(0.001)
    while x > 100:
        clear_canvas_now()
        character.draw_now(x,y)
        grass.draw_now(400,30)
        x-=2
        delay(0.001)
    while y > 90:
        clear_canvas_now()
        character.draw_now(x,y)
        grass.draw_now(400,30)
        y-=2
        delay(0.001)
    while x < 400:
        clear_canvas_now()
        character.draw_now(x,y)
        grass.draw_now(400,30)
        x+=2
        delay(0.001)
    while theta <= 270:
        clear_canvas_now()
        character.draw_now( 400 + math.cos(theta/360*2*math.pi) * 210 , 300 + math.sin(theta/360*2*math.pi)* 210)
        grass.draw_now(400,30)
        theta=theta+2
        delay(0.01)
    
close_canvas()
