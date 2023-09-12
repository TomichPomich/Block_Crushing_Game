spin = 0
randnumbox = 0
points = 00000
vida = 3

game = True
#from time import sleep
from pygame import *
from random import *
time_elapsed = time.get_ticks()
#Llamar clase de sprite
class GameSprite(sprite.Sprite):
    #Propiedades de sprite
    def __init__(self, imagen, x, y, speed):
        #"Super" mencionar a lo de arriba
        super().__init__()
        #Imagen y su tamaño
        self.image = transform.scale(image.load(imagen),(90, 90))
        #area rectangular usada para manipular
        self.rect = self.image.get_rect()
        #coordenada x 
        self.rect.x = x
        #coordenada y
        self.rect.y = y 
        #velocidad del sprite
        self.speed = speed

#función de reseteo de sprite(ocurrido cada cuadro x segundo (fps))
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class GameSprite2(sprite.Sprite):
    #Propiedades de sprite
    def __init__(self, imagen, x, y, speed):
        #"Super" mencionar a lo de arriba
        super().__init__()
        #Imagen y su tamaño
        self.image = transform.scale(image.load(imagen),(75, 75))
        #area rectangular usada para manipular
        self.rect = self.image.get_rect()
        #coordenada x 
        self.rect.x = x
        #coordenada y
        self.rect.y = y 
        #velocidad del sprite
        self.speed = speed

#función de reseteo de sprite(ocurrido cada cuadro x segundo (fps))
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    
    def actualizar(self):
        if key.get_pressed()[K_RIGHT]and self.rect.x < 500 - 30:
            self.rect.x += self.speed
            #player.image = transform.rotate(player.image, 1)
            
        if key.get_pressed()[K_LEFT]and self.rect.x >  -50:
            self.rect.x -= self.speed
            #player.image = transform.rotate(player.image, -1)

#CLASE BLOQUE           
class Block(GameSprite2):
    def actualizar(self):
        points = 00000
        #Define variables que ayudan a saber si cierta posición x ya está usada por un bloque
        is_1_occupied = False
        is_2_occupied = False
        is_3_occupied = False
        is_4_occupied = False
        is_5_occupied = False
        is_6_occupied = False
        is_7_occupied = False

        #Movimiento para arriba
        if 1==1:
            self.rect.y -= self.speed
        
        #Al llegar a cierto punto de arriba moverse para abajo
        if self.rect.y < -100:
            self.rect.y = 800
        #Elección de posición de bloque  
        if self.rect.y == 800:
            #1-7 son 7 posibles posiciones
            randnumbox=randint(1, 7)
            print(randnumbox)

            #CONDICIONALES QUE SIRVEN PARA ELEGIR POSICION DE BLOQUE
            #Arreglar(!!!)
            if randnumbox == 1 and is_1_occupied == False:
                self.rect.x = 0
                is_1_occupied = True
                if time_elapsed / 500 > 0 :
                    is_1_occupied = True
                is_1_occupied = False
            elif randnumbox == 2 and is_2_occupied == False:
                self.rect.x = 75
                is_2_occupied = True
                if time_elapsed / 500 > 0 :
                    is_2_occupied = True
                is_2_occupied = False
            elif randnumbox == 3 and is_3_occupied == False:
                self.rect.x = 150
                is_3_occupied = True
                if time_elapsed / 500 > 0 :
                    is_6_occupied = True
                is_3_occupied = False
            elif randnumbox == 4 and is_4_occupied == False:
                self.rect.x = 225
                is_4_occupied = True
                if time_elapsed / 500 > 0 :
                    is_4_occupied = True
                is_4_occupied = False
            elif randnumbox == 5 and is_5_occupied == False:
                self.rect.x = 300
                is_5_occupied = True
                if time_elapsed / 500 > 0 :
                    is_5_occupied = True
                is_5_occupied = False
            elif randnumbox == 6 and is_6_occupied == False:
                self.rect.x = 375
                is_6_occupied = True
                if time_elapsed / 500 > 0 :
                    is_6_occupied = True
                is_6_occupied = False
            elif randnumbox == 7 and is_7_occupied == False:
                self.rect.x = 450
                is_7_occupied = True
                if time_elapsed / 500 > 0 :
                    is_7_occupied = True
                is_7_occupied = False
            else:
                self.rect.x = 1000
        



#-------EVENTO DE COLISIÓN DEL JUGADOR CON LOS BLOQUES------

        





    

#ventana
window = display.set_mode((500, 800))

#texto de puntaje


#sprites
player = Player("character.png", 200, 0, 5)
block1 = Block("crate1.png", 0, 750, 5)
block2 = Block("crate1.png", 75, 750, 5)
block3 = Block("crate1.png", 150, 750, 5)
##
block5 = Block("crate1.png", 300, 750, 5)
##
block7 = Block("crate1.png", 375, 825, 5)
block8 = Block("crate1.png", 375, 825, 5)
block9 = Block("crate1.png", 375, 825, 5)
##
block11 = Block("crate1.png", 375, 825, 5)
block12 = Block("red_crate.png", 375, 825, 5)
##
block14 = Block("red_crate.png", 375, 900, 5)
block15 = Block("crate1.png", 375, 900, 5)
##
block17 = Block("crate1.png", 375, 900, 5)
block18 = Block("crate1.png", 375, 900, 5)
block19 = Block("crate1.png", 375, 975, 5)
block20 = Block("crate1.png", 375, 975, 5)
block21 = Block("star_crate.png", 375, 975, 5)
##
block23 = Block("red_crate.png", 375, 975, 5)
block24 = Block("crate1.png", 375, 975, 5)
block25 = Block("crate1.png", 375, 1050, 5)
###
###
###
block29 = Block("crate1.png", 375, 1050, 5)
block30 = Block("crate1.png", 375, 1050, 5)
block31 = Block("crate1.png", 375, 1125, 5)
###
block33 = Block("crate1.png", 375, 1125, 5)
block34 = Block("crate1.png", 375, 1125, 5)
block35 = Block("red_crate.png", 375, 1125, 5)
block36 = Block("crate1.png", 375, 1125, 5)
block37 = Block("crate1.png", 375, 1200, 5)
##
block39 = Block("crate1.png", 375, 1200, 5)
##
block41 = Block("star_crate.png", 375, 1200, 5)
block42 = Block("crate1.png", 375, 1200, 5)
##
block44 = Block("crate1.png", 375, 1275, 5)
block45 = Block("crate1.png", 375, 1275, 5)
##
block47 = Block("crate1.png", 375, 1275, 5)
block48 = Block("crate1.png", 375, 1275, 5)
block49 = Block("red_crate.png", 375, 1350, 5)
block50 = Block("crate1.png", 375, 1350, 5)
##
block52 = Block("crate1.png", 375, 1350, 5)
block53 = Block("crate1.png", 375, 1350, 5)
block54 = Block("crate1.png", 375, 1350, 5)
##
##
block57 = Block("crate1.png", 375, 1425, 5)
block58 = Block("red_crate.png", 375, 1425, 5)
block59 = Block("crate1.png", 375, 1425, 5)
block60 = Block("crate1.png", 375, 1425, 5)
block61 = Block("crate1.png", 375, 1500, 5)
block62 = Block("crate1.png", 375, 1500, 5)
##
##
block65 = Block("crate1.png", 375, 1500, 5)
block66 = Block("star_crate.png", 375, 1500, 5)
block67 = Block("crate1.png", 375, 1575, 5)
block68 = Block("crate1.png", 375, 1500, 5)
##
block70 = Block("crate1.png", 375, 1500, 5)
block71 = Block("red_crate.png", 375, 1500, 5)
block72 = Block("crate1.png", 375, 1500, 5)
#4, 6, 10, 13, 16, 22, 26, 27, 28, 32, 38, 40, 43, 46, 51, 55, 56, 63, 64, 69
#Grupos de sprites
block_group = sprite.Group([block1, block2, block3, block5, block7, block8, block9, block11, block12, block14, block15,  block17, block18, block19, block20, block21,  block23, block24, block25, block29, block30, block31, block33, block34, block35, block36, block37, block39, block41, block42, block44, block45,block47, block48, block49, block50, block52, block53, block54, block57, block58, block59, block60, block61, block62, block65, block66, block67, block68, block70, block71, block72])
player_group = sprite.Group([player])
print(block_group)

#Imagen de fondo
fondo = transform.scale(image.load("fondo_bricc.png"),(500, 850))


clock = time.Clock()
fps = 60
game = True
while game:
    
    spin += 1
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(fondo, (0,0))
    #player.rect.y = player.rect.y + 1
    #player.rect.x = randint(-50, 500)
    if 1==1: 
        if player.rect.colliderect(block1.rect):
            print("HI")
            block1.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block2.rect):
            print("HI")
            block2.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block3.rect):
            print("HI")
            block3.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block5.rect):
            print("HI")
            block5.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block7.rect):
            print("HI")
            block7.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block8.rect):
            print("HI")
            block8.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block9.rect):
            print("HI")
            block9.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block11.rect):
            print("HI")
            block11.rect.x = 600
        if player.rect.colliderect(block12.rect):###
            print("HI")
            block12.rect.x = 600
            if points > 10000:
                points = points - 10000
            else:
                points = 0
            vida = vida-1
        if player.rect.colliderect(block14.rect):
            print("HI")
            block14.rect.x = 600
            if points > 10000:
                points = points - 10000
            else:
                points = 0
            vida = vida-1
        if player.rect.colliderect(block15.rect):
            print("HI")
            block15.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block17.rect):
            print("HI")
            block17.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block18.rect):
            print("HI")
            block18.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block19.rect):
            print("HI")
            block19.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block20.rect):
            print("HI")
            block20.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block21.rect):
            print("HI")
            block21.rect.x = 600
            points = points + 3000
        if player.rect.colliderect(block23.rect):
            print("HI")
            block23.rect.x = 600
            if points > 10000:
                points = points - 10000
            else:
                points = 0
                print("ouch")
            vida = vida-1
        if player.rect.colliderect(block24.rect):
            print("HI")
            block24.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block25.rect):
            print("HI")
            block25.rect.x = 600
            points = points + 1000
        
        
        if player.rect.colliderect(block29.rect):
            print("HI")
            block29.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block30.rect):
            print("HI")
            block30.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block31.rect):
            print("HI")
            block31.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block33.rect):
            print("HI")
            block33.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block34.rect):
            print("HI")
            block34.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block35.rect):
            print("HI")
            block35.rect.x = 600
            if points > 10000:
                points = points - 10000
            else:
                points = 0
            vida = vida-1
        if player.rect.colliderect(block36.rect):
            print("HI")
            block36.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block37.rect):
            print("HI")
            block37.rect.x = 600
            points = points + 1000
        
        if player.rect.colliderect(block39.rect):
            print("HI")
            block39.rect.x = 600
            points = points + 1000
        
        if player.rect.colliderect(block41.rect):
            print("HI")
            block41.rect.x = 600
            points = points + 3000
        if player.rect.colliderect(block42.rect):
            print("HI")
            block42.rect.x = 600
            points = points + 1000
        
        if player.rect.colliderect(block44.rect):
            print("HI")
            block44.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block45.rect):
            print("HI")
            block45.rect.x = 600
            points = points + 1000
        
        if player.rect.colliderect(block47.rect):
            print("HI")
            block47.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block48.rect):
            print("HI")
            block48.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block49.rect):
            print("HI")
            block49.rect.x = 600
            if points > 10000:
                points = points - 10000
            else:
                points = 0
            vida = vida-1
        if player.rect.colliderect(block50.rect):
            print("HI")
            block50.rect.x = 600
            points = points + 1000
        
        if player.rect.colliderect(block52.rect):
            print("HI")
            block52.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block53.rect):
            print("HI")
            block53.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block54.rect):
            print("HI")
            block54.rect.x = 600
            points = points + 1000
        
        
        if player.rect.colliderect(block57.rect):
            print("HI")
            block57.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block58.rect):
            print("HI")
            block58.rect.x = 600
            if points > 10000:
                points = points - 10000
            else:
                points = 0
            vida = vida-1
        if player.rect.colliderect(block59.rect):
            print("HI")
            block59.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block60.rect):
            print("HI")
            block60.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block61.rect):
            print("HI")
            block61.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block62.rect):
            print("HI")
            block62.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block65.rect):
            print("HI")
            block65.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block66.rect):
            print("HI")
            block66.rect.x = 600
            points = points + 3000
        if player.rect.colliderect(block67.rect):
            print("HI")
            block67.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block68.rect):
            print("HI")
            block68.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block70.rect):
            print("HI")
            block70.rect.x = 600
            points = points + 1000
        if player.rect.colliderect(block71.rect):
            print("HI")
            block71.rect.x = 600
            if points > 10000:
                points = points - 10000
            else:
                points = 0
            vida = vida-1
        if player.rect.colliderect(block72.rect):
            print("HI")
            block72.rect.x = 600
            points = points + 1000
        
        
        

    #Actualización de sprites
    block1.actualizar()
    block1.reset()
    block2.actualizar()
    block2.reset()
    block3.actualizar()
    block3.reset()
    
    block5.actualizar()
    block5.reset()
    
    block7.actualizar()
    block7.reset()
    block8.actualizar()
    block8.reset()
    block9.actualizar()
    block9.reset()
    
    block11.actualizar()
    block11.reset()
    block12.actualizar()
    block12.reset()
    
    block14.actualizar()
    block14.reset()
    block15.actualizar()
    block15.reset()
    
    block17.actualizar()
    block17.reset()
    block18.actualizar()
    block18.reset()
    block19.actualizar()
    block19.reset()
    block20.actualizar()
    block20.reset()
    block21.actualizar()
    block21.reset()
    
    block23.actualizar()
    block23.reset()
    block24.actualizar()
    block24.reset()
    block25.actualizar()
    block25.reset()
    
    
    block29.actualizar()
    block29.reset()
    block30.actualizar()
    block30.reset()
    block31.actualizar()
    block31.reset()
    
    block33.actualizar()
    block33.reset()
    block34.actualizar()
    block34.reset()
    block35.actualizar()
    block35.reset()
    block36.actualizar()
    block36.reset()
    block37.actualizar()
    block37.reset()
    
    block39.actualizar()
    block39.reset()
    
    block41.actualizar()
    block41.reset()
    block42.actualizar()
    block42.reset()
    
    block44.actualizar()
    block44.reset()
    block45.actualizar()
    block45.reset()
    
    block47.actualizar()
    block47.reset()
    block48.actualizar()
    block48.reset()
    block49.actualizar()
    block49.reset()
    block50.actualizar()
    block50.reset()
    
    block52.actualizar()
    block52.reset()
    block53.actualizar()
    block53.reset()
    block54.actualizar()
    block54.reset()
    
    
    block57.actualizar()
    block57.reset()
    block58.actualizar()
    block58.reset()
    block59.actualizar()
    block59.reset()
    block60.actualizar()
    block60.reset()
    block61.actualizar()
    block61.reset()
    block62.actualizar()
    block62.reset()
    
    block65.actualizar()
    block65.reset()
    block66.actualizar()
    block66.reset()
    block67.actualizar()
    block67.reset()
    block68.actualizar()
    block68.reset()
    
    block70.actualizar()
    block70.reset()
    block71.actualizar()
    block71.reset()
    block72.actualizar()
    block72.reset()
    font.init()
    puntaje = font.SysFont('Comic Sans MS', 30)
    bigger_text = font.SysFont('Comic Sans MS', 50)
    #Renderización de texto de puntaje
    text_surface = puntaje.render(str(points), False, (255,255, 255))
    window.blit(text_surface, (0,0))
    font.init()
    
    text_surface2 = puntaje.render("Vida:"+str(vida), False, (255, 255, 255))
    window.blit(text_surface, (0,0))
    window.blit(text_surface2, (400,0))
    text_surface3 = bigger_text.render("¡¡HAS PERDIDO!!", False, (255, 255, 255))
    text_surface4 = bigger_text.render("Puntos:"+str(points), False, (255, 255, 255))
    
    if vida < 1:
        player.rect.x = 1000
        window.blit(text_surface3, (55,200))
        window.blit(text_surface4, (85,250))
        if time_elapsed / 10000 > 0 :
                    vida = 0
    
 
    
    
    player.actualizar()
    player.reset()

    
    #if sprite.groupcollide(player_group, block_group, False, False):
        #print("Ouch")
        #points = points + 1000

             
     
    
    display.update()
    clock.tick(fps)





