from pico2d import *
import game_framework
import play_state
import title_state

image = None
logo_time = 0.0
def enter():
    global image
    image =load_image('add_delete_boy.png')

def exit():
    global image
    del image


def update():
    pass

def draw():
    # fill here
    global image
    clear_canvas()
    play_state.draw_world()
    image.draw(400,300)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case pico2d.SDLK_0:
                    game_framework.stack[-2].boy.item = None
                    game_framework.pop_state()
                case pico2d.SDLK_1:
                    game_framework.stack[-2].boy.item = 'Ball'
                    game_framework.pop_state()
                case pico2d.SDLK_2:
                    game_framework.stack[-2].boy.item = 'BigBall'
                    game_framework.pop_state()
                case pico2d.SDLK_a:
                    play_state.team.append(play_state.Boy())
                    game_framework.pop_state()
                case pico2d.SDLK_PLUS:
                    play_state.team.append(play_state.Boy())
                    game_framework.pop_state()
                case pico2d.SDLK_MINUS:
                    if len(play_state.team) > 1:
                     del play_state.team[len(play_state.team) -1]
                    game_framework.pop_state()


def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()


if __name__ == '__main__': # 단독 실행이면
    test_self()



