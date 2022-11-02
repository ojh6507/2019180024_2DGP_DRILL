from pico2d import *
# 이벤트 정의
RD, LD, RU, LU, TIMER, AUTO = range(6)

key_event_table = {
(SDL_KEYDOWN, SDLK_RIGHT): RD,
(SDL_KEYDOWN, SDLK_LEFT): LD,
(SDL_KEYUP, SDLK_RIGHT): RU,
(SDL_KEYUP, SDLK_LEFT): LU,
(SDL_KEYDOWN, SDLK_a): AUTO
}

class SLEEP:
    @staticmethod
    def enter(self, event):
        print('ENTER SLEEP')
        self.dir = 0
        pass

    @staticmethod
    def exit(self):
        print('EXIT SLEEP')

        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        pass

    @staticmethod
    def draw(self):
        if self.face_dir == 1: # 오른쪽을 바라고 있는 상태
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,
                                           3.141592/2, ' ',
                                           self.x+25, self.y - 25, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100,
                                           -3.141592 / 2, ' ',
                                           self.x + 25, self.y - 25, 100, 100)

#클래스를 이용해서 상태를 만듦
class IDLE:
    @staticmethod
    def enter(self, event):
        self.dir = 0
        # 타이머 설정
        self.timer = 1000
        pass

    @staticmethod
    def exit(self):
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0: #시간이 경과하면
            #이벤트를 발생시켜야함
            #self.q.insert(0, TIMER) # 객체지향프로그래 위배, q를 직접 엑세스하고 있으므로
            self.add_evnet(TIMER)

    @staticmethod
    def draw(self):
        if self.face_dir == 1: # 오른쪽을 바라고 있는 상태 Run상태에서 나올 때 전달해야됨
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
        pass

class AUTO_RUN:
    @staticmethod
    def enter(self, event):
        print('ENTER Auto_RUN')
        self.dir = self.face_dir
        self.opoosite = False
        pass

    @staticmethod
    def exit(self):
        print('Exit Auto_RUN')
        # run을 나가서 idle로 갈 때, run의 방향을 알려줄 필요가 있다
        self.face_dir = self.dir
        pass

    @staticmethod
    def do(self):

        self.frame = (self.frame + 1) % 8
        self.x = clamp(0,self.x, 800)
        if self.x <= 0 and not self.opoosite:
            self.x += 1
            self.opoosite = False
        elif self.x >= 800:
            self.x -= 1
            self.opoosite = True

        pass

    @staticmethod
    def draw(self):
        print(self.x)
        if self.dir == -1:
             self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
             self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)

class RUN:
    @staticmethod
    def enter(self, event):
        print('ENTER RUN')
        #self.dir를 결정 해야함 , idle에서 나올 때 결정됨
        if event == RD: self.dir += 1
        elif event == LD: self.dir -= 1
        elif event == RU: self.dir -= 1
        elif event == LU: self.dir += 1
        pass

    @staticmethod
    def exit(self):
        print('Exit RUN')
        # run을 나가서 idle로 갈 때, run의 방향을 알려줄 필요가 있다
        self.face_dir = self.dir
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0,self.x, 800) # self.x 0 ~ 800으로 제한
        pass

    @staticmethod
    def draw(self):
         if self.dir == -1:
             self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
         elif self.dir == 1:
             self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)


next_state = {
    AUTO_RUN:{RD: RUN, LD: RUN, RU: RUN, LU: RUN, AUTO: IDLE},
    SLEEP: {RD: RUN, LD: RUN, RU: RUN, LU: RUN, SLEEP: SLEEP, AUTO: SLEEP},
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, AUTO: AUTO_RUN},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, AUTO: AUTO_RUN}
}

class Boy:
    def add_evnet(self,event):
        self.q.insert(0, event)

    def handle_event(self, event): #소년이 스스로 이벤트를 처리함수 입력
        # event 는 키이벤트.. 이것을 내부 RD 등으로 변환
        if (event.type,event.key) in key_event_table:
            key_event = key_event_table[(event.type,event.key)]
            self.add_evnet(key_event) # 변환된 내부 이벤트를 큐에 추가


        # if event.type == SDL_KEYDOWN:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir -= 1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir += 1
        #
        # elif event.type == SDL_KEYUP:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir += 1
        #             self.face_dir = -1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir -= 1
        #             self.face_dir = 1

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.q: #q에 뭔가 들어있다면
            event = self.q.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event] #다음 상태를 계산함
            self.cur_state.enter(self, event)


        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)

    def draw(self):
        self.cur_state.draw(self)
        # if self.dir == -1:
        #     self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        # elif self.dir == 1:
        #     self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        # else:
        #     if self.face_dir == 1:
        #         self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        #     else:
        #         self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)


