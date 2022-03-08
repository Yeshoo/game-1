
from turtle import screensize
import pygame
import time
import random
  
# windowsize
WINDOW_W=1000
WINDOW_H=702
WINDOW_SIZE=(WINDOW_W,WINDOW_H)
size_x_cursor=70
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("חי צומח דומם")


bk_image=pygame.image.load("back.jpg")
write_image=pygame.image.load("images.jpg")
cursor_image=pygame.image.load("הורדה.png")
bk_image=pygame.transform.scale(bk_image,(1000,500))
write_image=pygame.transform.scale(write_image,(1000,220))
cursor_image=pygame.transform.scale(cursor_image,(size_x_cursor,40))


# clock=pygame.time.clock()
# https://www.yo-yoo.co.il/data/game/solutions/

latters=["א","ב","ג","ד","ה","ו","ז","ח","ט","י","כ","ל","מ","נ","ס","ע","פ","צ","ק","ר","ש","ת"]
Latters=["א","ב","ג","ד","ה","ו","ז","ח","ט","י","כ","ל","מ","נ","ס","ע","פ","צ","ק","ר","ש","ת","ף","ץ","ך","ם"]
start=True
lottery_latter=random.choice(latters)
print(str(lottery_latter))
mouse_position=(0,0)
while start:
 screen.blit(bk_image,(0,0))
 screen.blit(write_image,(0,500))
#  screen.blit(cursor_image,(0,))
 for event in pygame.event.get():
    print (event)
    if event.type==pygame.QUIT:
      start=False
    if event.type==pygame.MOUSEMOTION:
        mouse_position = pygame.mouse.get_pos()
 screen.blit(cursor_image,(mouse_position[0]-size_x_cursor/2,mouse_position[1]-10))
 pygame.display.flip()
 


pygame.quit