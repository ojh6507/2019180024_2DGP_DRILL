from pico2d import *
def handle_events():
    global running
    global dir
    global action
    global character
    events = get_events()
    for event in events:
        if event.type ==SDL_QUIT:
            running =False
        elif event.type ==SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir+= 1
                action = 70
                character =load_image('mario_walk.png')
            elif event.key == SDLK_LEFT:
                dir-= 1
                action = 5
                character =load_image('mario_walk.png')
        elif event.type ==SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir-= 1
                character =load_image('idle.png')
                action = 5
             
            if event.key == SDLK_LEFT:
                dir+= 1
                character =load_image('idle.png')
                action = 70
           
running = True
open_canvas(1280,1024)

frame = 0
dir = 0
x= 800//2
action  = 5
character =load_image('idle.png')

while running:
    clear_canvas()
    character.clip_draw(frame * 50,  action , 50, 60, x, 90)
    update_canvas()
    
    handle_events()

    x += dir * 5
    if dir != 0:
        frame = (frame + dir) % 25
        delay(0.01)

    else:
        frame = (frame + 1) % 79
        delay(0.03)

   
close_canvas()