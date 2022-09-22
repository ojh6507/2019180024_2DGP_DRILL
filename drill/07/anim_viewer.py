from pico2d import *
open_canvas()

character =load_image('penguin.png')
frame = 0
action = 1010
frame_count = [15,11,11,11,10,11,11,14,14,11,15]
index =0

while action > 0:
    clear_canvas()
    character.clip_draw(frame * 100, action, 100, 110, 400, 300)
    update_canvas()
    frame = (frame + 1) % frame_count[index]

    if frame == 0:
        action = (action -100)
        index+=1
    delay(0.15)

    get_events()

close_canvas()