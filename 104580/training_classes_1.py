from pygame import *
font.init()
class GameSprite(sprite.Sprite):
    def __init__(self,p_image,p_x,p_y,p_speed,p_size_x,p_size_y):
        super().__init__()
        self.size_x = p_size_x
        self.size_y =p_size_y
        self.image = transform.scale(image.load(p_image),(self.size_x,self.size_y))
        self.speed = p_speed
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys_p = key.get_pressed() 
        if keys_p[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_p[K_s] and self.rect.y < 570:
            self.rect.y += self.speed
    def update_r(self):
        keys_p = key.get_pressed() 
        if keys_p[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_p[K_DOWN] and self.rect.y < 570:
            self.rect.y += self.speed
    
window = display.set_mode((700,500))
hero1 = Player('sk1.png', 0,350,5,100,130)
hero2 = Player('sk2.png', 610,350,5,100,130)
egg = GameSprite('egg.png', 450,350,5,80,90)
background = transform.scale(image.load('sky.jpeg'),(900,700))
speed_x = 3
speed_y = 4
finish = False
game = True
FPS = 60
font1 = font.Font(None,35)
lose1 = font1.render('PLAYER 1 LOSE!', True,(180,0,0))
lose2 = font1.render('PLAYER 2 LOSE!', True,(180,0,0))
clock = time.Clock()
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        egg.rect.x += speed_x
        egg.rect.y += speed_y
        if egg.rect.y >= 410 or egg.rect.y <= 0 :
            speed_y *= -1
        if sprite.collide_rect(egg,hero1) or sprite.collide_rect(egg,hero2) :
            speed_x*= -1
        if egg.rect.x < 0:
            finish = True
            window.blit(lose1, (200,200))
        if egg.rect.x > 700:
            finish = True
            window.blit(lose2, (200,200))
            
            

        
        hero1.update_l()
        hero1.reset()
        hero2.update_r()
        hero2.reset()
        egg.reset()
        egg.update()

    display.update()