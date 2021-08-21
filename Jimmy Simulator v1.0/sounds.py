import pygame
pygame.mixer.init()

#player sprites
'START BLOCK'
playerattacksound = pygame.mixer.Sound('assets\sounds\Low Whoosh.mp3')

blocksound = pygame.mixer.Sound('assets\sounds\Clang.mp3')
'END BLOCK'

#enemy sprites
'START BLOCK'
enemyattacksound = pygame.mixer.Sound('assets\sounds\Crunch.mp3')
enemyattacksound.set_volume(0.8)

enemyshootsound = pygame.mixer.Sound('assets\sounds\Pew.mp3')

enemyhurt1 = pygame.mixer.Sound('assets\sounds\Duck.mp3')
enemyhurt2 = pygame.mixer.Sound('assets\sounds\Goose.mp3')

enemyhurt1.set_volume(0.1)
enemyhurt2.set_volume(0.1)

enemyhurtsounds = (enemyhurt1,enemyhurt2)

spidersound = pygame.mixer.Sound('assets\sounds\Bite.mp3')

spikesound = pygame.mixer.Sound('assets\sounds\Rip.mp3')

jumpscaresound = pygame.mixer.Sound('assets\sounds\Scare.mp3')

angelfiresound = pygame.mixer.Sound('assets\sounds\High Whoosh.mp3')
angelfiresound.set_volume(0.1)
shockwave = pygame.mixer.Sound('assets\sounds\Pop.mp3')
shockwave.set_volume(2)

electricitysound = pygame.mixer.Sound('assets\sounds\Electricity.mp3')
'END BLOCK'

#health pack
'START BLOCK'
healthsound = pygame.mixer.Sound('assets\sounds\Coin.mp3')
'END BLOCK'
