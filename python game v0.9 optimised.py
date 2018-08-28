import pygame
import os
from random import *
from numpy.random import choice
import time

pygame.init();
#screen = pygame.display.set_mode((width,height));
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN|pygame.HWSURFACE);
get_info = pygame.display.Info();
print(get_info);
width = get_info.current_w;
height = get_info.current_h;
done = False;
init = True;
run_code = randint(0,100000);
active_locations = [];
inactive_locations = [];
new_active_locations = [];
_currently_playing_song = None;
strike = 1;
max_s = choice([1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,8,8,8,12]);
r_1 = choice([1]);
r_2 = choice([1]);
amount = choice([1,2]);
seed_angle = uniform(0.01, 9.99);
#10000 is rare, 1 is minimum and fast
frequency = 50;
h_percent = 60;
millisecond_wait = 100;
restart = False;

seed = [randint(0,width),0,seed_angle];
active_locations.append(seed);


SONG_END = pygame.USEREVENT + 1;

pygame.mixer.music.set_endevent(SONG_END);
pygame.mixer.music.load('sound/rain.ogg');
pygame.mixer.music.play();

_songs = ['sound/rain.ogg'];
_sounds = ['sound/lightning3.ogg','sound/thunder.ogg','sound/thundercrackle.ogg'];



def play_a_different_song():
    global _currently_playing_song, _songs
    next_song = choice(_songs)
    #prevent repeats
    #while next_song == _currently_playing_song:
    #    next_song = choice(_songs)
    _currently_playing_song = next_song
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.play()

_sound_library = {}
def play_sound(path,volume):
  global _sound_library
  sound = _sound_library.get(path)
  if sound == None:
    sound = pygame.mixer.Sound(path)
    _sound_library[path] = sound.set_volume(volume)
  sound.play()

def draw_background():
    global screen,width,height,h_percent,millisecond_wait
    pygame.draw.rect(screen, (13, 35, 13), pygame.Rect(0, height*(h_percent/100), width, height-height*(h_percent/100)));
    #pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(i[0], i[1], 1, 1));
    #updates lightning
    pygame.display.flip();
    #reduces performance and ruins flash but saves an image
    #pygame.image.save(screen, "screenshot_"+str(run_code)+"_strike_"+str(strike)+".jpeg")
    #flash below
    time.sleep(millisecond_wait/1000.0);
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, width+1, height*(h_percent/100)));
    #removes lightning
    pygame.display.flip();

while not done:
    if init == True:
        draw_background();
        init = False;
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True;
        if event.type == SONG_END:
            play_a_different_song();
    #print(active_locations);
    new_active_locations = [];
    #update the screen with the moving pixels
    wait_random = randint(0,frequency);
    if wait_random == int(round(frequency/2)) or event.type == SONG_END:
        
        for i in active_locations:
            inactive_locations.append(i);
            if i[0] > width or i[1] > height*(h_percent/100) or i[1] < 0 or i[0] < 0:
                print("strike:"+str(strike));
                strike += 1;
                prev_s = max_s;
                if prev_s == 1:
                    volume = uniform(0.5, 0.6);
                elif prev_s == 2:
                    volume = uniform(0.6, 0.7);
                elif prev_s == 3:
                    volume = uniform(0.8, 0.85);
                elif prev_s == 8:
                    volume = uniform(0.85, 0.95);
                elif prev_s == 12:
                    volume = uniform(0.95, 1.0);
                max_s = choice([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,3,8,12]);
                r_1 = choice([1]);
                r_2 = choice([1]);
                amount = choice([1,2]);
                seed_angle = uniform(0.01, 9.99);
                seed = [randint(0,width),0,seed_angle];
                for k in inactive_locations:
                    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(k[0], k[1], 1, 1));
                active_locations = [seed];
                new_active_locations = [];
                inactive_locations = [];
                
                if prev_s > 2:
                    play_sound(choice(_sounds,p=[0.9,0.05,0.05]),volume);
                else:
                    play_sound(choice(_sounds),volume);
                draw_background();
        #spread in a direction and possibly split
        for i in active_locations:
            i_new = [0,0];
            #maybe make this variable
            split = choice([0,1,2,3,4,5,6,7,8,9,10]);
            if split == 0:
                r = 0;
                for g in range(0,amount):
                    if len(new_active_locations) < max_s:
                        i_new[1] = i[1] + choice([0,1],p=[(i[2]/10),1-(i[2]/10)]);
                        if choice([0,1],p=[seed_angle/10,1-seed_angle/10]) == 1:
                            i_new[0] = i[0] - choice([0,1],p=[1-(i[2]/10),(i[2]/10)]);
                        else:
                            i_new[0] = i[0] + choice([0,1],p=[1-(i[2]/10),(i[2]/10)]);
                        r = r_1;
                        new_active_locations.append([i_new[0],i_new[1],choice([1,2,3,4,5,6,7,8,9])]);
                if r == r_2:
                    new_active_locations.append([i_new[0],i_new[1],i[2]]);
            else:
                i_new[1] = i[1] + choice([0,1],p=[(i[2]/10),1-(i[2]/10)]);
                if choice([0,1],p=[seed_angle/10,1-seed_angle/10]) == 1:
                    i_new[0] = i[0] - choice([0,1],p=[1-(i[2]/10),(i[2]/10)]);
                else:
                    i_new[0] = i[0] + choice([0,1],p=[1-(i[2]/10),(i[2]/10)]);
                new_active_locations.append([i_new[0],i_new[1],i[2]]);
        active_locations = new_active_locations;
        new_active_locations = [];
        #pygame.display.flip();
