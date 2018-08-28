import pygame
from random import *

pygame.init();
#screen = pygame.display.set_mode((width,height));
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN|pygame.HWSURFACE);
get_info = pygame.display.Info();
print(get_info);
width = get_info.current_w;
height = get_info.current_h;
done = False;
values = [randint(0,255),randint(0,255),randint(0,255)]
num = 0;
run_code = randint(0,100000);

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True;
    for x in range(0,width - 1):
        for y in range(0,height - 1):
            c = 0;
            for i in values:
                if c == 0:
                    randomvalue = randint(0,1);
                    if randomvalue == 1:
                        i += 1;
                    else:
                        i -+ 1;
                elif c == 1:
                    i = 255 - values[0];
                elif c == 2:
                    i = (values[0] + values[1])/2;
                if i > 255 or i < 0:
                    i = randint(0,255);
                values[c] = i;
                c += 1;
            
            pygame.draw.rect(screen, (values[0], values[1], values[2]), pygame.Rect(x, y, 1, 1))
    num += 1;
    pygame.image.save(screen, "screenshot_"+str(run_code)+"_"+str(num)+".jpeg")
    pygame.display.flip();
