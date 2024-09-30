from pico2d import *



def set_flag():
    global running, player_flag, frame
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                player_flag = 'right'
                frame = 0
            elif event.key == SDLK_LEFT:
                player_flag = 'left'
                frame = 0
            elif event.key == SDLK_UP:
                player_flag = 'up'
                frame = 0
            elif event.key == SDLK_DOWN:
                player_flag = 'down'
                frame = 0
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            player_flag='idle'
            frame=0
def play_animation(dir, frame):
    clear_canvas()
    self.ground.draw(400, 300)

    update_canvas()
running = True
frame = 0
open_canvas()
player_x=800//2
player_y=600//2
player_idle = load_image('Sword_Idle_full.png')
player_run = load_image('Sword_Run_full.png')
ground = load_image('TUK_GROUND.png')
player_flag='idle'
player_dir={(0, 1), (0, -1), (-1, 0), (1, 0)} #상하좌우

while running:
    set_flag()
    if(player_flag=='idle'):
        pass
    elif(player_flag=='up'):
        pass
    elif(player_flag=='down'):
        pass
    elif(player_flag=='left'):
        pass
    elif(player_flag=='right'):
        pass

    delay(0.05)


