from pygame import *
from time import sleep
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x , self.rect.y))

class Player(GameSprite):
    def update(self):
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 395:
            self.rect.y += self.speed


class Enemy(GameSprite):
    direction="left"
    def update(self):
        if self.rect.x <= 500:
            self.direction = "right"
        if self.rect.x >= 700 - 85:
            self.direction = "left"

        if self.direction =="left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((self.color_1, self.color_2, self.color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

window=display.set_mode((700,500))
display.set_caption("Пинпонг")
background = transform.scale(image.load("hon.jpg"),(700,500))


x1 = 10
y1 = 10
x2 = 550
y2 = 250
x3 = 550
y3 = 400
levo = 0
pravo = 0

'''wintext = font.render('Победа правого!',True, (255, 215, 0))
losetext = font.render('Победа левого!',True, (255, 215, 0))'''

sten1 = Player('sten.jpg', -55,200,5)
sten2 = Player2('sten.jpg', 690,200,5)
pp = Enemy('pp.png', 350,250,2)
clock=time.Clock()
FPS = 60

font.init()
font = font.SysFont('Arial', 70)
win2 = font.render('YOU WIN', True, (255, 215, 0))
loos2 = font.render('Loos', True, (255, 64, 0))
levogo=font.render('Счёт: '+ str(levo),True, (20, 255, 0))
pravogo=font.render('Счёт; '+ str(pravo),True, (0, 255, 200))
finish = False

#задай фон сцены


speed_x = 3
speed_y = 3


game= True
while game:


    if finish != True:
        pp.rect.x += speed_x
        pp.rect.y += speed_y
        
        if pp.rect.y > 500-50 or pp.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(sten2, pp) or sprite.collide_rect(sten1, pp):
            speed_x *=-1

        if pp.rect.x < 0:
            pp.rect.x= 350
            pravo =+ 1


        if pp.rect.x > 700:
            pp.rect.x= 350
            levo =+ 1

        window.blit(background,(0,0))
        sten1.reset()
        sten2.reset()
        pp.reset()


        keys_pressed = key.get_pressed()
        '''if keys_pressed[K_UP] and y1 > 5:
            y1 -= 10
        if keys_pressed[K_DOWN] and y1 < 395:
            y1 += 10


        if keys_pressed[K_w] and y2 < 5:
            y2 -= 10
        if keys_pressed[K_s] and y2 < 395:
            y2 += 10
        if x1==x2 and y1==y2'''

        '''if count1 >= 51:
            sleep(0.5)
            window.blit(wintext, (250, 250))
            finish = True
        if count2 >= 11:
            sleep(0.5)
            window.blit(losetext, (250, 250))
            finish = True'''

        for e in event.get():
            if e.type == QUIT:
                game = False

            if finish != True:

                '''if sprite.sprite.collide_rect(sten1, wall1) or sprite.collide_rect(sten2, wall2):
                    window.blit(loos2, (200, 200))
                    finish = True
                    loos.play()

                if sprite.collide_rect(sten1, treasure):
                    windowblit(win2, (200, 200))
                    finish = True
                    win.play()'''

        clock.tick(FPS)
        sten1.update()
        sten2.update()
        levogo=font.render('Счёт: '+ str(levo),True, (20, 255, 0))
        pravogo=font.render('Счёт; '+ str(pravo),True, (0, 255, 200))
        window.blit(levogo, (0, 0))
        window.blit(pravogo, (500, 0))
        display.update()
    
    

