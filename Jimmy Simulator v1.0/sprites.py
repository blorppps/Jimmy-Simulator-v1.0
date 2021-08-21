import pygame

#player sprites
'START BLOCK'
playerleft = pygame.image.load('assets\player\\normal\player-left.png')
playerleftattack = pygame.image.load('assets\player\\normal\player-left-attack.png')
playerleftblock = pygame.image.load('assets\player\\normal\player-left-block.png')

playerright = pygame.image.load('assets\player\\normal\player-right.png')
playerrightattack = pygame.image.load('assets\player\\normal\player-right-attack.png')
playerrightblock = pygame.image.load('assets\player\\normal\player-right-block.png')
'END BLOCK'

#player sprites for the final level (black background)
'START BLOCK'
playerleftfinal = pygame.image.load('assets\player\\final\player-left.png')
playerleftattackfinal = pygame.image.load('assets\player\\final\player-left-attack.png')
playerleftblockfinal = pygame.image.load('assets\player\\final\player-left-block.png')

playerrightfinal = pygame.image.load('assets\player\\final\player-right.png')
playerrightattackfinal = pygame.image.load('assets\player\\final\player-right-attack.png')
playerrightblockfinal = pygame.image.load('assets\player\\final\player-right-block.png')
'END BLOCK'

#enemy sprites
'START BLOCK'
smallleft = pygame.image.load('assets\enemies\small jimmy\small-left.png')
smallright = pygame.image.load('assets\enemies\small jimmy\small-right.png')

smallleftattack = pygame.image.load('assets\enemies\small jimmy\small-left-attack.png')
smallrightattack = pygame.image.load('assets\enemies\small jimmy\small-right-attack.png')

mediumleft = pygame.image.load('assets\enemies\medium jimmy\medium-left.png')
mediumright = pygame.image.load('assets\enemies\medium jimmy\medium-right.png')

mediumleftattack = pygame.image.load('assets\enemies\medium jimmy\medium-left-attack.png')
mediumrightattack = pygame.image.load('assets\enemies\medium jimmy\medium-right-attack.png')

projectileleft = pygame.image.load('assets\enemies\projectile jimmy\projectile-left.png')
projectileright = pygame.image.load('assets\enemies\projectile jimmy\projectile-right.png')
enemyprojectile = pygame.image.load('assets\enemies\projectile jimmy\projectile.png')

spider = pygame.image.load('assets\enemies\spider\spider.png')
spiderbite = pygame.image.load('assets\enemies\spider\spider-bite.png')

mask = pygame.image.load('assets\enemies\mask\mask.png')
maskred = pygame.image.load('assets\enemies\mask\mask-red.png')
spikesprite = pygame.image.load('assets\enemies\mask\spike.png')
jumpscare = pygame.image.load('assets\enemies\mask\jumpscare.png')

#non-horror mode
mask2 = pygame.image.load('assets\enemies\mask\mask2.png')
mask3 = pygame.image.load('assets\enemies\mask\mask3.png')
spike2 = pygame.image.load('assets\enemies\mask\spike2.png')

angel = pygame.image.load('assets\enemies\\angel\\angel.png')
angelwingsup = pygame.image.load('assets\enemies\\angel\\angel-wings-up.png')
angelwingsdown = pygame.image.load('assets\enemies\\angel\\angel-wings-down.png')
angelcrown = pygame.image.load('assets\enemies\\angel\\angel-crown.png')
angelsword = pygame.image.load('assets\enemies\\angel\sword.png')
'END BLOCK'

#health pack
'START BLOCK'
healthsprite = pygame.image.load('assets\health\health.png')
'END BLOCK'

#garden of eden
'START BLOCK'
morningstar = pygame.image.load('assets\eden\morning-star.png')
holylance = pygame.image.load('assets\eden\\non-believer.png')

trees = pygame.image.load('assets\eden\\trees.png')

knowledgetree = pygame.image.load('assets\eden\knowledge.png')
lifetree = pygame.image.load('assets\eden\life-everlasting.png')

duck = pygame.image.load('assets\eden\duck.png')
'END BLOCK'
