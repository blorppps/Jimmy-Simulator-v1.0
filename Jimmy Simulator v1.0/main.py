#launcher + options
'START BLOCK'
import launcher

if launcher.cheats == 1:
    cheats = True
else:
    cheats = False

#horror is True if the value is 0 because the checkbox is "non-horror"
if launcher.horror == 0:
    horror = True
else:
    horror = False

if launcher.music == 1:
    music = True
else:
    music = False

waitoncheats = False #makes it so the player skips 1 level at a time
'END BLOCK'

#setup
'START BLOCK'
import pygame
import random
import keyboard
import mouse
import math
import levels
import pygame.mixer

from sprites import *
from sounds import *

pygame.init()

running = True

showcredits = False
scrollcredits = 0

level = 0
levelcleared = True

FPS = 150
fpsclock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf',32)
leveldisplay = font.render(str(level),True,(0,0,0))
leveldisplayfinal = font.render(str(level),True,(255,255,255))

endfont = pygame.font.Font('freesansbold.ttf',16)

screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption('Jimmy Simulator')
pygame.display.set_icon(pygame.image.load('assets\enemies\small jimmy\small-left.png'))

#credits
creditsfile = open('credits.txt','r')
creditslist = creditsfile.readlines()
'END BLOCK'

#player
'START BLOCK'
playerX = 10
playerY = 10
playerdirection = 'right'
playerspeed = 3

attackstate = 'normal'
holdattack = 0
attackcooldown = 0
attackcanhurt = False

health = 100
'END BLOCK'

#enemies
'START BLOCK'
enemydata = []
enemyprojectiledata = []

levelcleared = True
clearlevel = False

bossattack = 100

spikedata = []
spikes = 0
spikedistance = 10
spikedirX = 0
spikedirY = 0
waitthisframe = False #used to slow down the spawning of spikes
jumpscaretimer = 0

#angel animations
angelcrownheight = 20
angelcrownstate = 'up'

angelwingswitch = 200
angelwingstate = 'up'

angelattack = 0
angelpreviousattack = 0

#default far = 400, close = 30
def chase(far,close,spritemid):
    
    global playerX
    global playerY

    global enemyX
    global enemyY

    global enemyspeed
    global enemydirection

    distance = math.dist((playerX+15,playerY+18),(enemyX+spritemid[0],enemyY+spritemid[1]))

    if distance < far and distance > close:
        enemylocation = [enemyX,enemyY]
        playerlocation = [playerX,playerY]

        #dumb math
        a = (enemyX+spritemid[0]) - (playerX+15)
        b = (enemyY+spritemid[1]) - (playerY+18)
        c = math.sqrt(a**2 + b**2)
                
        d = math.asin(-b/c)

        #move
        if playerX+15 > enemyX+spritemid[0]:
            enemyX = enemyX + math.cos(d)*enemyspeed
            enemyY = enemyY + math.sin(d)*enemyspeed
        else:
            enemyX = enemyX - math.cos(d)*enemyspeed
            enemyY = enemyY + math.sin(d)*enemyspeed

        #direction
        if playerX > enemyX:
            enemydirection = 'right'
        if playerX < enemyX:
            enemydirection = 'left'

#take damage
def hurt(ylimit,dist,spritemid):
    
    global attackcanhurt

    global playerX
    global playerY
    global playerdirection

    global enemy
    
    global enemyhealth
    global enemyX
    global enemyY
    global enemyKB

    spritemidX = spritemid[0]
    spritemidY = spritemid[1]
    
    enemyKB = enemy[3]

    distance = math.dist((playerX+15,playerY+18),(enemyX+spritemidX,enemyY+spritemidY))
    
    if attackcanhurt:
        
        enemyhurtsound = random.choice(enemyhurtsounds)
        
        if abs(playerY - enemyY) < ylimit and distance < dist and playerX > enemyX and playerdirection == 'left':
            enemyhealth = enemyhealth - 1
            enemyKB = -7
            enemyhurtsound.play()
        elif abs(playerY - enemyY) < ylimit and distance < dist and playerX < enemyX and playerdirection == 'right':
            enemyhealth = enemyhealth - 1
            enemyKB = 7
            enemyhurtsound.play()

#draw sword
#idk how to use surfaces, so im just gonna draw the entire sprite with lines :D
#these are used only for the angel boss
def drawsword(location):

    global epX
    global epY
    global epXmove
    global epYmove

    hiltX = epX-20*epXmove
    hiltY = epY-20*epYmove

    #blade
    pygame.draw.line(screen,(255,255,255),location,(epX-20*epXmove,epY-20*epYmove),5)
    #handle
    pygame.draw.line(screen,(255,255,255),location,(epX-25*epXmove,epY-25*epYmove),3)
    #hilt
    pygame.draw.line(screen,(255,255,255),(hiltX-5*epYmove,hiltY+5*epXmove),(hiltX+5*epYmove,hiltY-5*epXmove),3)

def drawarrow(location):

    global epX
    global epY
    global epXmove
    global epYmove

    finX = epX-20*epXmove
    finY = epY-20*epYmove

    #shaft
    pygame.draw.line(screen,(255,255,255),location,(epX-25*epXmove,epY-25*epYmove),3)
    #fletching
    pygame.draw.line(screen,(255,255,255),(epX-15*epXmove,epY-15*epYmove),(epX-20*epXmove,epY-20*epYmove),6)
'END BLOCK'

#health kit
#"bandaids" -kathleen
'START BLOCK'
healthX = 0
healthY = 700

healthactive = False

healthpacks = 0

waitonhealth = False
'END BLOCK'

#levels
'START BLOCK'
levelnumber = len(levels.leveldata)-1

endingslide = 0

def loadnext():
    global levelcleared
    global level
    
    global enemydata
    global enemyprojectiledata
    global spikedata
    global enemydirection

    global playerX
    global health

    global startmusic
    global waitoncheats

    global endingslide

    global showcredits
    global scrollcredits
    
    if level < levelnumber and not level == -1:
        level = level + 1
        enemydata = levels.leveldata[level]
        enemyprojectiledata = []
        spikedata = []
        enemydirection = 'left'
        levelcleared = False
        playerX = 10

        startmusic = True
            
        #heal slightly
        health = health + 10
        if health > 100:
            health = 100

    #ending
    elif level == levelnumber:
        enemydata = []
        enemyprojectiledata = []
        spikedata = []
        
        endingslide = 1
        playerX = 10
        level = -1
        levelcleared = True

    elif endingslide == 1:
        endingslide = 2
        levelcleared = True
        playerX = 10
        
    elif endingslide == 2:
        endingslide = 3
        levelcleared = True
        playerX = 10

    elif endingslide == 3:
        endingslide = 4
        levelcleared = True
        playerX = 10

    elif endingslide == 4 and not showcredits: #stops the credits from restarting if already in play
        #start credits
        showcredits = True
        scrollcredits = -300

def loadlast():
    global levelcleared
    global level
    
    global enemydata
    global enemyprojectiledata
    global spikedata
    global enemydirection

    global playerX
    global health

    global startmusic
    
    if level > 0:
        level = level - 1
        enemydata = levels.leveldata[level]
        enemyprojectiledata = []
        spikedata = []
        enemydirection = 'left'
        levelcleared = False
        playerX = 10

        startmusic = True
            
        #heal slightly
        health = health + 10
        if health > 100:
            health = 100
'END BLOCK'

#music
'START BLOCK'
currentmusic = 'none'
startmusic = True
'END BLOCK'

#credits
'START BLOCK'
'END BLOCK'

#main loop
while running:

    #fill color
    'START BLOCK'
    screencolor = levels.levelcolors[level]

    #makes sure the screen is always green for the ending
    if endingslide == 1:
        screencolor = (80,255,80)
    if endingslide == 2:
        screencolor = (50,150,50)
    if endingslide == 3:
        screencolor = (60,200,60)
    
    screen.fill(screencolor)
    'END BLOCK'
    
    #quit
    'START BLOCK'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    'END BLOCK'

    #player
    'START BLOCK'
    #movement
    #speed modifiers
    if attackstate == 'block':
        playerspeed = 0.6
    elif not jumpscaretimer == 0:
        playerspeed = 0
    else:
        playerspeed = 3
    
    if keyboard.is_pressed('w'):
        playerY = playerY - playerspeed
    if keyboard.is_pressed('a'):
        playerX = playerX - playerspeed
    if keyboard.is_pressed('s'):
        playerY = playerY + playerspeed
    if keyboard.is_pressed('d'):
        playerX = playerX + playerspeed

    if playerX < 0:
        playerX = 0
    if playerX > 1170:
        playerX = 1170
        if levelcleared:
            loadnext()
    if playerY < 0:
        playerY = 0
    if playerY > 565:
        playerY = 565

    #attack
    if attackstate == 'attack':
        holdattack = holdattack - 1
        if holdattack < 1:
            attackstate = 'normal'
            attackcooldown = 75

    if not attackstate == 'attack' and attackcooldown > 0:
        attackcooldown = attackcooldown - 1
    
    if keyboard.is_pressed('q') and not attackstate == 'attack' and attackcooldown == 0:
        playerdirection = 'left'
        attackstate = 'attack'
        holdattack = 30
        playerattacksound.play()
        attackcanhurt = True
    if keyboard.is_pressed('e') and not attackstate == 'attack' and attackcooldown == 0:
        playerdirection = 'right'
        attackstate = 'attack'
        holdattack = 30
        playerattacksound.play()
        attackcanhurt = True
        
    if keyboard.is_pressed('tab'):
        attackstate = 'block'

    #render
    if level in levels.whiteplayerlevels or endingslide == 4:
        if playerdirection == 'left':
            if attackstate == 'normal':
                screen.blit(playerleftfinal,(playerX,playerY))
            if attackstate == 'attack':
                screen.blit(playerleftattackfinal,(playerX-5,playerY))
            if attackstate == 'block':
                screen.blit(playerleftblockfinal,(playerX,playerY))

        if playerdirection == 'right':
            if attackstate == 'normal':
                screen.blit(playerrightfinal,(playerX,playerY))
            if attackstate == 'attack':
                screen.blit(playerrightattackfinal,(playerX,playerY))
            if attackstate == 'block':
                screen.blit(playerrightblockfinal,(playerX,playerY))
    else:
        if playerdirection == 'left':
            if attackstate == 'normal':
                screen.blit(playerleft,(playerX,playerY))
            if attackstate == 'attack':
                screen.blit(playerleftattack,(playerX-5,playerY))
            if attackstate == 'block':
                screen.blit(playerleftblock,(playerX,playerY))

        if playerdirection == 'right':
            if attackstate == 'normal':
                screen.blit(playerright,(playerX,playerY))
            if attackstate == 'attack':
                screen.blit(playerrightattack,(playerX,playerY))
            if attackstate == 'block':
                screen.blit(playerrightblock,(playerX,playerY))

    #die if out of health
    if health <= 0:
        running = False
    'END BLOCK'

    #enemies
    'START BLOCK'

    #clear dead enemies
    for i in range (enemydata.count([])):
        enemydata.remove([])

        if enemydata == []:
            levelcleared = True
            clearlevel = True
            startmusic = True

    #main enemy loop
    for i in range (len(enemydata)):

        #get all the data from the list
        'START BLOCK'
        enemy = enemydata[i]
        
        enemylocation = enemy[0]
        enemyX = enemylocation[0]
        enemyY = enemylocation[1]

        enemysprite = enemy[1]

        enemyhealth = enemy[2]

        enemyKB = 0

        enemyattack = enemy[4]
        holdenemyattack = enemy[5]

        enemydamage = enemy[6]

        enemyspeed = enemy[7]

        enemydirection = enemy[8]
        'END BLOCK'
        
        #code for small and medium enemies
        'START BLOCK'
        if enemysprite == 'small' or enemysprite == 'medium':

            if enemysprite == 'small':
                chase(400,30,(16,20))
                hurt(30,35,(16,20))

            if enemysprite == 'medium':
                chase(400,30,(25,32))
                hurt(40,35,(25,32))
            
            #attack if close enough
            if math.dist((playerX,playerY),(enemyX,enemyY)) < 40:
                if enemyattack == 0:
                    enemyattack = 200
                else:
                    if enemyattack > 0:
                        enemyattack = enemyattack - 1
                    if holdenemyattack > 0:
                        holdenemyattack = holdenemyattack - 1
                    if enemyattack == 0:
                        holdenemyattack = 10
                        if enemydirection == 'left' and playerdirection == 'right' and attackstate == 'block':
                            blocksound.play()
                        elif enemydirection == 'right' and playerdirection == 'left' and attackstate == 'block':
                            blocksound.play()
                        else:
                            health = health - enemydamage
                            enemyattacksound.play()
                    
            else:
                if enemyattack > 0:
                    enemyattack = enemyattack - 1
                if holdenemyattack > 0:
                    holdenemyattack = holdenemyattack - 1
        'END BLOCK'

        #code for projectile enemies
        'START BLOCK'
        if enemysprite == 'projectile':
            if enemyattack > 0:
                enemyattack = enemyattack - 1
                
            chase(600,200,(16,20))

            hurt(30,35,(16,20))
                
            #shoot if close enough
            if math.sqrt((playerX-enemyX)**2+(playerY-enemyY)**2) < 400 and enemyattack == 0:
                enemylocation = [enemyX,enemyY]
                playerlocation = [playerX,playerY]

                #dumb math
                a = enemyX - playerX
                b = enemyY - playerY
                c = math.sqrt(a**2 + b**2)
                
                d = math.asin(-b/c)

                if playerX > enemyX:
                    enemyprojectiledata.append([[enemyX+12,enemyY+16],[math.cos(d)*2,math.sin(d)*2],'normal',d])
                else:
                    enemyprojectiledata.append([[enemyX+12,enemyY+16],[-math.cos(d)*2,math.sin(d)*2],'normal',d])
                
                enemyattack = 500

                enemyshootsound.play()
        'END BLOCK'

        #code for spider boss
        'START BLOCK'
        if enemysprite == 'spider':
            
            chase(800,30,(23,60))

            hurt(80,70,(23,60))

            if math.dist((playerX+15,playerY+18),(enemyX+23,enemyY+60)) < 60:
                if enemyattack == 0:
                    enemyattack = 350
                else:
                    if enemyattack > 0:
                        enemyattack = enemyattack - 1
                    if holdenemyattack > 0:
                        holdenemyattack = holdenemyattack - 1
                    if enemyattack == 0 and holdenemyattack == 0:
                        holdenemyattack = 15
                        if enemydirection == 'left' and playerdirection == 'right' and attackstate == 'block':
                            health = health - enemydamage*0.5
                            spidersound.play()
                        elif enemydirection == 'right' and playerdirection == 'left' and attackstate == 'block':
                            health = health - enemydamage*0.5
                            spidersound.play()
                        else:
                            health = health - enemydamage
                            spidersound.play()
                    
            else:
                if enemyattack > 0:
                    enemyattack = enemyattack - 1
                if holdenemyattack > 0:
                    holdenemyattack = holdenemyattack - 1
            
            #summon attack + heal
            if bossattack > 0:
                bossattack = bossattack - 1
            else:
                enemydata.append([[enemyX-100,enemyY],'small',1,0,0,0,5,0.6,'left'])
                enemydata.append([[enemyX+60,enemyY],'small',1,0,0,0,5,0.6,'right'])
                enemyhealth = enemyhealth + 2
                if enemyhealth > 20:
                    enemyhealth = 20
                bossattack = 2000

            #spider boss healthbar
            pygame.draw.line(screen,(100,100,100),(300,30),(900,30),8)
            pygame.draw.line(screen,(255,0,0),(300,30),(300+enemyhealth*30,30),8)
        'END BLOCK'

        #code for mask boss
        'START BLOCK'
        if enemysprite == 'mask':

            hurt(40,40,(25,32))

            #health drain
            if enemyattack > 0:
                enemyattack = enemyattack - 1
                
            if enemyattack == 0:
                if math.dist((playerX,playerY),(enemyX,enemyY)) < 300:
                    enemyattack = 1500
                    holdenemyattack = 600

            if holdenemyattack > 0:
                holdenemyattack = holdenemyattack - 1
                
                if holdenemyattack < 400: #gives the player a slight delay
                    distance = math.dist((playerX,playerY),(enemyX,enemyY))
                    if distance < 500:
                        health = health - (500-distance) / 5000

                        enemyhealth = enemyhealth + 0.005
                        if enemyhealth > 20:
                            enemyhealth = 20

                        #sucks player in
                        a = (enemyX+25) - (playerX+15)
                        b = (enemyY+32) - (playerY+18)
                        c = math.sqrt(a**2 + b**2)
                
                        d = math.asin(-b/c)

                        #move
                        if playerX+15 > enemyX+25:
                            playerX = playerX - (math.cos(d)+(500-distance)/600)
                            playerY = playerY - (math.sin(d)+(500-distance)/6000)
                        else:
                            playerX = playerX + (math.cos(d)+(500-distance)/600)
                            playerY = playerY - (math.sin(d)+(500-distance)/600)

                        if distance < 30:

                            health = health - 10
                            
                            #puts the player in one of the corners of the map
                            #js = jumpscare
                            jslocations = ((50,50),(1135,50),(50,532),(1135,532))
                            jslocation = random.choice(jslocations)
                            playerX = jslocation[0]
                            playerY = jslocation[1]
                            
                            jumpscaretimer = 200


            #spikes
            if bossattack > 0:
                bossattack = bossattack - 1

            if bossattack == 0:

                #only runs when first starting an attack
                if spikes == 0:
                    a = enemyX - playerX
                    b = enemyY - playerY
                    c = math.sqrt(a**2 + b**2)
                
                    d = math.asin(-b/c)

                    if playerX > enemyX:
                        spikedirX = math.cos(d)
                        spikedirY = math.sin(d)
                    else:
                        spikedirX = -math.cos(d)
                        spikedirY = math.sin(d)

                if not waitthisframe:
                    spikeX = enemyX + (spikedirX*spikes*10+random.uniform(-20,20)+25)
                    spikeY = enemyY + (spikedirY*spikes*10+random.uniform(-20,20)+32)
                
                    spikedata.append([[spikeX,spikeY],random.randint(500,700)])

                    if horror:
                        spikesound.play()

                    if math.dist((playerX+15,playerY+18),(spikeX+4,spikeY+12)) < 30:
                        health = health - enemydamage
                
                    spikes = spikes + 1
                    if spikes == 70:
                        spikes = 0
                        bossattack = 1000
                    
                    waitthisframe = True
                else:
                    waitthisframe = False

            #mask boss healthbar
            pygame.draw.line(screen,(100,100,100),(300,30),(900,30),8)
            pygame.draw.line(screen,(255,0,0),(300,30),(300+enemyhealth*30,30),8)
        'END BLOCK'

        #code for angel boss
        'START BLOCK'
        if enemysprite == 'angel':
            
            hurt(30,35,(16,20))

            #animations
            if angelcrownstate == 'up':
                angelcrownheight = angelcrownheight + 0.05
                if angelcrownheight > 35:
                    angelcrownstate = 'down'
            if angelcrownstate == 'down':
                angelcrownheight = angelcrownheight - 0.05
                if angelcrownheight < 20:
                    angelcrownstate = 'up'

            angelwingswitch = angelwingswitch - 1
            if angelwingswitch == 0:
                if angelwingstate == 'up':
                    angelwingstate = 'down'
                elif angelwingstate == 'down':
                    angelwingstate = 'up'

                #damages player if hit by the wings
                if abs((enemyX+16)-(playerX+15)) > 20 and abs((enemyX+16)-(playerX+15)) < 100 and abs((enemyY+20)-(playerY+18)) < 30:
                    health = health - 3
                
                angelwingswitch = 200

            #attack handling
            if bossattack > 0:
                bossattack = bossattack - 1

            #randomly chooses attack
            if bossattack == 0:
                angelattack = random.randint(0,4)

                if angelattack == angelpreviousattack:
                    angelattack = random.randint(0,4) #reduces the chance of the same attack being used twice
                else:
                    angelpreviousattack = angelattack

                #start attacks
                if angelattack == 0:
                    electricitysound.set_volume(1)
                    electricitysound.play()
                    holdenemyattack = 200
                    aimX = playerX
                    aimY = playerY
                    bossattack = 500
                if angelattack == 1:
                    holdenemyattack = 250
                    bossattack = 550
                if angelattack == 2:
                    holdenemyattack = 200
                    bossattack = 600
                if angelattack == 3:
                    holdenemyattack = 600
                    aimX = playerX
                    aimY = playerY
                    bossattack = 900

                    a = (enemyX+15) - (aimX+15)
                    b = (enemyY+18) - (aimY+18)
                    c = math.sqrt(a**2 + b**2)
                    d = math.asin(-b/c)
                if angelattack == 4: #do nothing
                    enemyX = 584
                    enemyY = 280
                    
                    holdenemyattack = 900
                    bossattack = 900

            if holdenemyattack > 0:
                holdenemyattack = holdenemyattack - 1
                if holdenemyattack == 0:
                    angelattack = -1
                    electricitysound.set_volume(0)

            #attacks

            #lightning
            if angelattack == 0 and holdenemyattack > 1:
                shootlocation = (aimX+random.randint(-50,50),aimY+random.randint(-50,50))
                pygame.draw.line(screen,(255,255,255),(enemyX+16,enemyY+20),shootlocation,3)

                if math.dist(shootlocation,(playerX,playerY)) < 20:
                    health = health - 1

            #swords
            if angelattack == 1 and holdenemyattack > 1:

                #draws swords over the angels head
                if holdenemyattack < 210  and holdenemyattack > 70:
                    screen.blit(angelsword,(enemyX-40,enemyY-40))
                if holdenemyattack < 170 and holdenemyattack > 50:
                    screen.blit(angelsword,(enemyX-10,enemyY-50))
                if holdenemyattack < 130 and holdenemyattack > 30:
                    screen.blit(angelsword,(enemyX+20,enemyY-50))
                if holdenemyattack < 90 and holdenemyattack > 10:
                    screen.blit(angelsword,(enemyX+50,enemyY-40))

                a = (enemyX+5) - playerX
                b = (enemyY-45) - playerY
                c = math.sqrt(a**2 + b**2)
                
                d = math.asin(-b/c)

                #shoots swords
                #what even is this block
                if holdenemyattack == 70:
                    a = (enemyX-40) - playerX-15
                    b = (enemyY-40) - playerY-18
                    c = math.sqrt(a**2 + b**2)
                    d = math.asin(-b/c)
                    
                    if playerX > enemyX:
                        enemyprojectiledata.append([[enemyX-40,enemyY-40],[math.cos(d)*2,math.sin(d)*2],'angelsword',d])
                    else:
                        enemyprojectiledata.append([[enemyX-40,enemyY-40],[-math.cos(d)*2,math.sin(d)*2],'angelsword',d])

                    playerattacksound.play()
                        
                if holdenemyattack == 50:
                    a = (enemyX-10) - playerX-15
                    b = (enemyY-50) - playerY-18
                    c = math.sqrt(a**2 + b**2)
                    d = math.asin(-b/c)
                    
                    if playerX > enemyX:
                        enemyprojectiledata.append([[enemyX-10,enemyY-50],[math.cos(d)*2,math.sin(d)*2],'angelsword',d])
                    else:
                        enemyprojectiledata.append([[enemyX-10,enemyY-50],[-math.cos(d)*2,math.sin(d)*2],'angelsword',d])

                    playerattacksound.play()
                        
                if holdenemyattack == 30:
                    a = (enemyX+20) - playerX-15
                    b = (enemyY-50) - playerY-18
                    c = math.sqrt(a**2 + b**2)
                    d = math.asin(-b/c)
                    
                    if playerX > enemyX:
                        enemyprojectiledata.append([[enemyX+20,enemyY-50],[math.cos(d)*2,math.sin(d)*2],'angelsword',d])
                    else:
                        enemyprojectiledata.append([[enemyX+20,enemyY-50],[-math.cos(d)*2,math.sin(d)*2],'angelsword',d])

                    playerattacksound.play()
                        
                if holdenemyattack == 10:
                    a = (enemyX+50) - playerX-15
                    b = (enemyY-40) - playerY-18
                    c = math.sqrt(a**2 + b**2)
                    d = math.asin(-b/c)
                    
                    if playerX > enemyX:
                        enemyprojectiledata.append([[enemyX+50,enemyY-40],[math.cos(d)*2,math.sin(d)*2],'angelsword',d])
                    else:
                        enemyprojectiledata.append([[enemyX+50,enemyY-40],[-math.cos(d)*2,math.sin(d)*2],'angelsword',d])

                    playerattacksound.play()

            #arrows
            if angelattack == 2 and holdenemyattack > 1:
                chase(1200,30,(16,20))
                
                if holdenemyattack % 10 == 0: #shoot every 6 frames   
                    a = enemyX - playerX
                    b = enemyY - playerY
                    c = math.sqrt(a**2 + b**2)
                
                    d = math.asin(-b/c) + random.uniform(-0.2,0.2)

                    if playerX > enemyX:
                        enemyprojectiledata.append([[enemyX+12,enemyY+40],[math.cos(d)*2,math.sin(d)*2],'angel',d])
                    else:
                        enemyprojectiledata.append([[enemyX+12,enemyY+40],[-math.cos(d)*2,math.sin(d)*2],'angel',d])

                if holdenemyattack % 25 == 0: #play sound less often so it doesnt sound weird
                    angelfiresound.play()

            #teleport
            if angelattack == 3 and holdenemyattack > 1:

                #move
                if aimX+15 > enemyX+16:
                    enemyX = enemyX + math.cos(d)*enemyspeed*10
                    enemyY = enemyY + math.sin(d)*enemyspeed*10
                else:
                    enemyX = enemyX - math.cos(d)*enemyspeed*10
                    enemyY = enemyY + math.sin(d)*enemyspeed*10

                #direction
                if aimX > enemyX:
                    enemydirection = 'right'
                if aimX < enemyX:
                    enemydirection = 'left'

                if math.dist((aimX+15,aimY+18),(enemyX+16,enemyY+20)) < 20 or math.dist((playerX+15,playerY+18),(enemyX+16,enemyY+20)) < 100:

                    #deal damage
                    if math.dist((playerX+15,playerY+18),(enemyX+16,enemyY+20)) < 100:
                        health = health - 5
                    
                    aimX = playerX
                    aimY = playerY

                    #moves to edge of screen
                    enemyattacksound.play()
                    
                    if random.randint(0,1) == 0:
                        enemyX = 0
                    else:
                        enemyX = 1184

                    enemyY = random.randint(0,580)

                    a = (enemyX+15) - (aimX+15)
                    b = (enemyY+18) - (aimY+18)
                    c = math.sqrt(a**2 + b**2)
                    d = math.asin(-b/c)
                    
            #healthbar
            pygame.draw.line(screen,(100,100,100),(300,30),(900,30),8)
            pygame.draw.line(screen,(255,0,0),(300,30),(300+enemyhealth*20,30),8)
        'END BLOCK'
        
        #general stuff
        'START BLOCK'

        #take knockback
        if not enemysprite == 'mask':
            enemyX = enemyX + enemyKB
        
        if enemyKB > 0:
            enemyKB = enemyKB - 1
        if enemyKB < 0:
            enemyKB = enemyKB + 1
        'END BLOCK'

        #update data
        'START BLOCK'
        enemylocation = [enemyX,enemyY]
        enemy.pop(0)
        enemy.insert(0,enemylocation)

        enemy.pop(2)
        enemy.insert(2,enemyhealth)

        enemy.pop(3)
        enemy.insert(3,enemyKB)

        enemy.pop(4)
        enemy.insert(4,enemyattack)
        enemy.pop(5)
        enemy.insert(5,holdenemyattack)

        enemy.pop(8)
        enemy.insert(8,enemydirection)

        if enemyhealth < 1:
            enemy = []

        enemydata.pop(i)
        enemydata.insert(i,enemy)
        'END BLOCK'

        #draws sprite
        'START BLOCK'
        if enemysprite == 'small':
            if enemydirection == 'left':
                if holdenemyattack == 0:
                    screen.blit(smallleft,tuple(enemylocation))
                else:
                    screen.blit(smallleftattack,(enemyX-10,enemyY))
            if enemydirection == 'right':
                if holdenemyattack == 0:
                    screen.blit(smallright,tuple(enemylocation))
                else:
                    screen.blit(smallrightattack,tuple(enemylocation))
                    
        if enemysprite == 'medium':
            if enemydirection == 'left':
                if holdenemyattack == 0:
                    screen.blit(mediumleft,tuple(enemylocation))
                else:
                    screen.blit(mediumleftattack,(enemyX-10,enemyY))
            if enemydirection == 'right':
                if holdenemyattack == 0:
                    screen.blit(mediumright,tuple(enemylocation))
                else:
                    screen.blit(mediumrightattack,(enemyX+10,enemyY))
        
        if enemysprite == 'projectile':
            if enemydirection == 'left':
                screen.blit(projectileleft,(enemyX,enemyY))
            if enemydirection == 'right':
                screen.blit(projectileright,(enemyX,enemyY))

        if enemysprite == 'spider':
            if holdenemyattack == 0:
                screen.blit(spider,(enemyX,enemyY))
            else:
                screen.blit(spiderbite,(enemyX,enemyY))

        if enemysprite == 'mask':
            if holdenemyattack == 0:
                if horror:
                    screen.blit(mask,(enemyX,enemyY))
                else:
                    screen.blit(mask2,(enemyX,enemyY))
            else:
                if horror:
                    screen.blit(maskred,(enemyX,enemyY))
                else:
                    screen.blit(mask3,(enemyX,enemyY))

        if enemysprite == 'angel':
            if angelwingstate == 'up':
                screen.blit(angelwingsup,(enemyX-70,enemyY-20))
            if angelwingstate == 'down':
                screen.blit(angelwingsdown,(enemyX-70,enemyY-15))
            screen.blit(angelcrown,(enemyX,enemyY-angelcrownheight))
            screen.blit(angel,(enemyX,enemyY))
        'END BLOCK'
    'END BLOCK'

    #enemy projectiles
    'START BLOCK'
    for i in range(enemyprojectiledata.count([])):
        enemyprojectiledata.remove([])
        
    for i in range (len(enemyprojectiledata)):
        
        #get projectile data
        #ep = enemyprojectile
        ep = enemyprojectiledata[i]

        eplocation = ep[0]
        epmovement = ep[1]

        epX = eplocation[0]
        epY = eplocation[1]

        epXmove = epmovement[0]
        epYmove = epmovement[1]

        eptype = ep[2]

        epangle = ep[3]*(180/math.pi) #angle needs to be in degrees
        
        #moves projectile
        if eptype == 'angelsword':
            epX = epX + epXmove*5
            epY = epY + epYmove*5
        if eptype == 'angel':
            epX = epX + epXmove*2
            epY = epY + epYmove*2
        else:
            epX = epX + epXmove
            epY = epY + epYmove

        eplocation = [epX,epY]

        ep.pop(0)
        ep.insert(0,eplocation)

        #damage if touching player
        if abs(playerX+15 - epX+4) < 20 and abs(playerY+18 - epY+4) < 22:
            if eptype == 'angelsword':
                health = health - 7
            if eptype == 'angel':
                health = health - 2
            if eptype == 'normal':
                health = health - 5
                
            ep = []
            enemyattacksound.play()

        if epX < 0 or epX > 1200 or epY < 0 or epY > 600:
            ep = []

        #updates list
        enemyprojectiledata.pop(i)
        enemyprojectiledata.insert(i,ep)

        #draws bullet
        if eptype == 'normal':
            screen.blit(enemyprojectile,tuple(eplocation))
            
        if eptype == 'angel':
            #draws arrow
            drawarrow(eplocation)
            
        if eptype == 'angelsword':
            #draws sword
            drawsword(eplocation)
        
    'END BLOCK'

    #mask spikes
    'START BLOCK'
    for i in range (spikedata.count([])):
        spikedata.remove([])
    
    for i in range (len(spikedata)):

        #get the data
        spike = spikedata[i]

        timeleft = spike[1]
        spikelocation = spike[0]
        
        timeleft = timeleft - 1

        spike.pop(1)
        spike.insert(1,timeleft)

        if timeleft == 0:
            spike = []

        spikedata.pop(i)
        spikedata.insert(i,spike)

        #draws spike
        if horror:
            screen.blit(spikesprite,tuple(spikelocation))
        else:
            screen.blit(spike2,tuple(spikelocation))
    'END BLOCK'
    
    #health
    'START BLOCK'
    if clearlevel and level in levels.healthpacklevels:
        healthactive = True
        
    if healthactive:
        healthX = 590
        healthY = 290
        screen.blit(healthsprite,(healthX,healthY))
        if math.sqrt((playerX-healthX)**2+(playerY-healthY)**2) < 21:
            healthpacks = healthpacks + 1
            healthactive = False
            healthsound.play()

    if healthpacks > 0 and keyboard.is_pressed('r') and not waitonhealth and health < 100:
        healthpacks = healthpacks - 1
        health = health + 50
        if health > 100:
            health = 100
        waitonhealth = True

    if not keyboard.is_pressed('r'):
        waitonhealth = False

    #draws icon
    for i in range (healthpacks):
        screen.blit(healthsprite,(500+30*i,560))
    'END BLOCK'

    #ending props
    'START BLOCK'
    if level == -1:
        if endingslide == 1:
            screen.blit(knowledgetree,(490,190))
            screen.blit(holylance,(560,380))
            
        if endingslide == 2:
            screen.blit(trees,(300,150))
            screen.blit(morningstar,(800,400))

        if endingslide == 3:
            screen.blit(lifetree,(550,160))

        if endingslide == 4:
            screen.blit(duck,(580,280))
    'END BLOCK'

    #music
    'START BLOCK'
    if not music:
        startmusic = False
        
    if startmusic:
        if level == 10:
            pygame.mixer.music.load('assets\music\horror1.mp3')
            pygame.mixer.music.play()
            currentmusic = 'mask'
        elif level == 15:
            if not enemydata == []:
                pygame.mixer.music.load('assets\music\\boss1.mp3')
                pygame.mixer.music.play()
                currentmusic = 'boss'
            else:
                pygame.mixer.music.stop()
                currentmusic = 'none'
                
        else:
            if not currentmusic == 'game':
                pygame.mixer.music.load('assets\music\game1.mp3')
                pygame.mixer.music.play()
                currentmusic = 'game'
    'END BLOCK'

    #necessary stuff
    'START BLOCK'
    attackcanhurt = False
    clearlevel = False
    startmusic = False

    #healthbar
    pygame.draw.line(screen,(100,100,100),(500,550),(700,550),5)
    pygame.draw.line(screen,(255,0,0),(500,550),(500+2*health,550),5)

    leveldisplay = font.render(str(level),True,(0,0,0))
    leveldisplayfinal = font.render(str(level),True,(255,255,255))
    if level == -1:
        pass
    elif level == 15:
        screen.blit(leveldisplayfinal,(10,10))
    else:
        screen.blit(leveldisplay,(10,10))

    #jumpscare at the end so it covers the rest of the screen
    if jumpscaretimer > 0:
        jumpscaretimer = jumpscaretimer - 1

        if horror:
            screen.fill((0,0,0))
            if jumpscaretimer < 20:
                screen.blit(jumpscare,(400,50))
                jumpscaresound.play()

    #ending
    if showcredits:
        screen.fill((0,0,0))

        for o in range (len(creditslist)):
            creditslinetext = creditslist[o]
            creditslinetext = creditslinetext.replace('\n','')
            
            creditsline = endfont.render(creditslinetext,True,(255,255,255))
            screen.blit(creditsline,(100,scrollcredits+o*30))

        if scrollcredits < 1500:
            scrollcredits = scrollcredits + 0.2
            
        pygame.mixer.stop()
    
    fpsclock.tick(FPS)
    pygame.display.update()
    'END BLOCK'

    #cheats
    'START BLOCK'
    if cheats:
        #go forward 1 level
        if keyboard.is_pressed('2') and not waitoncheats:
            loadnext()
            waitoncheats = True
            
        #go back 1 level
        if keyboard.is_pressed('1') and not waitoncheats:
            loadlast()
            waitoncheats = True

        if not keyboard.is_pressed('1') and not keyboard.is_pressed('2'):
            waitoncheats = False

        #heal
        if keyboard.is_pressed('3'):
            health = 100

        #clear all enemies
        if keyboard.is_pressed('4'):
            enemydata = []
            enemyprojectiledata = []
            spikedata = []
            
            levelcleared = True
            clearlevel = True
            startmusic = True
    'END BLOCK'

#quit
'START BLOCK'
pygame.quit()
'END BLOCK'
