from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('mummy.png')

frame = 0
for x in range(0,800,1):
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame * 30,50,30,50,50,90)
    #clip_draw(left, bottom, width, height, x, y)
    update_canvas()
    frame =(frame + 1) % 18 # 주어진 범위내에서 루프 frame = (0 ~ 7)루프
    delay(0.05)
    get_events()

close_canvas()

