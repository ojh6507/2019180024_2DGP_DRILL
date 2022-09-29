from pico2d import *
TUK_WIDTH, TUK_HEIGHT = 800, 800
#TUK_WIDTH, TUK_HEIGHT = 1280, 1024 #background size

def handle_events():
    global running, x_dir, y_dir, action, time_delay

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                x_dir -= 1
                action = 3
            elif event.key == SDLK_LEFT:
                x_dir += 1
                action = 2
            elif event.key == SDLK_UP:
                y_dir -= 1
            elif event.key == SDLK_DOWN:
                y_dir += 1
            elif event.key == SDLK_ESCAPE:
                running = False
            time_delay = 0.15
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                x_dir += 1
                action = 1
            elif event.key == SDLK_LEFT:
                x_dir -= 1
                action = 0
            elif event.key == SDLK_UP:
                y_dir += 1
            elif event.key == SDLK_DOWN:
                y_dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
            time_delay = 0.02

def boundary(pos, pos_dir, max, min):
    if pos + pos_dir * 5 < max and pos + pos_dir * 5 > min:
        return True
    else:
        return False

open_canvas(TUK_WIDTH,TUK_HEIGHT)
grass = load_image('grass.png')
background = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
y = 90
frame = 0
x_dir = 0
y_dir = 0
action = 3
# action = 0 (left run)
# action = 1 (right run)
# action = 2 (left idle)
# action = 3 (right idle)

time_delay = 0.15

while running:
    clear_canvas()
    background.draw(TUK_WIDTH//2,TUK_HEIGHT//2)
    grass.draw(400, 30)
    grass.draw(TUK_WIDTH - 400, 30)
    character.clip_draw(frame * 100, 100 * action, 100, 100, x, y)
    update_canvas()

    handle_events()
    if boundary(x,x_dir,TUK_WIDTH,0):
        x += x_dir * 5

    if boundary(y,y_dir,TUK_HEIGHT - 10 ,90):
        y += y_dir * 5

    if action == 0 or action == 1:
        frame = (frame + x_dir) % 8
    else:
        frame = (frame + 1) % 8

    delay(time_delay)
close_canvas()

