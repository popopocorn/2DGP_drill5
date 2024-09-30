from pico2d import *

class Player():
    def __init__(self):
        self.player_x=800//2
        self.player_y=90
        #self.player_idle = load_image('Sword_Idle_full.png')
        #self.player_run = load_image('Sword_Run_full.png')
        self.player_flag='idle'
        player_dir={(0, 1), (0, -1), (-1, 0), (1, 0)} #상하좌우
    def set_flag(self):
        global running
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                running = False
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                    pass
                elif event.key == SDLK_LEFT:
                    pass
                elif event.key == SDLK_UP:
                    pass
                elif event.key == SDLK_DOWN:
                    pass
                elif event.key == SDLK_ESCAPE:
                    running = False

    def do_act(self):
        if self.player_flag == 'idle':
            pass
        elif self.player_flag == 'right':
            pass
        elif self.player_flag == 'left':
            pass
        elif self.player_flag == 'up':
            pass
        elif self.player_flag == 'down':
            pass
    def play_animation(self, dir):
        pass




player = Player()
open_canvas()
running = True
while running:
    player.set_flag()
    player.do_act()


