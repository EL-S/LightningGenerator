import pygame
import random
from numpy.random import choice

pygame.init();
#window = pygame.display.set_mode((width,height));
window = pygame.display.set_mode((0,0),pygame.FULLSCREEN|pygame.HWSURFACE);
get_info = pygame.display.Info();
width = get_info.current_w;
height = get_info.current_h;
done = False;
run_code = random.randint(0,100000);
num = 0;

#vars
pixel_width = 1;
pixel_height = 1;
x_array_unused = [];
y_array_unused = [];
x_y_array_unused = [];
first_colour = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
colours = [first_colour];
for i in range(width):
    x_array_unused.append(i);
for i in range(height):
    y_array_unused.append(i);

random.shuffle(x_array_unused);
random.shuffle(y_array_unused);

for x in x_array_unused:
    for y in x_array_unused:
        random_choice = choice([0,1],p=[0.90,0.1]);
        if random_choice == 1:
            r = random.randint(0,255);
            g = random.randint(0,255);
            b = random.randint(0,255);
            colours.append([r,g,b]);
            #add new colour to the availiable colours
        else:
            rgb = random.choice(colours);
            r = rgb[0];
            g = rgb[1];
            b = rgb[2];
            #add the chosen colour back into the colours to increase likelihood
            colours.append([r,g,b]);
        x_y_array_unused.append([x,y,[r,g,b]]);


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True;
    for i in x_y_array_unused:
        pygame.draw.rect(window, (i[2][0], i[2][1], i[2][2]), pygame.Rect(i[0], i[1], pixel_width, pixel_height));
    pygame.display.flip();
    pygame.image.save(window, "screenshot_"+str(run_code)+"_"+str(num)+".jpeg");
    num += 1;
    done = True;
