#levels

'''
small jimmy: [[x,y],'small',3,0,0,0,5,0.6,'left']
medium jimmy: [[x,y],'medium',6,0,0,0,10,1,'left']
projectile jimmy: [[x,y],'projectile',5,0,0,0,0*,0.4,'left']

*damage variable is unused for projectile enemies
'''

'''
how the npc data works
0: location
1: sprite
2: health
3: knockback
4: attack cooldown
5: used for attack animation
6: damage
7: speed
8: direction
'''

'START BLOCK'
leveldata = [
    [],
    
    [[[600,300],'small',3,0,0,0,5,0.6,'left']],
    [[[300,100],'small',3,0,0,0,5,0.6,'left'],[[600,300],'small',3,0,0,0,5,0.6,'left'],[[900,500],'small',3,0,0,0,5,0.6,'left']],
    [[[500,100],'small',3,0,0,0,5,0.6,'left'],[[500,500],'small',3,0,0,0,5,0.6,'left'],[[700,300],'medium',6,0,0,0,10,1,'left']],
    [[[600,150],'small',3,0,0,0,5,0.6,'left'],[[400,250],'small',3,0,0,0,5,0.6,'left'],[[800,250],'small',3,0,0,0,5,0.6,'left'],[[500,450],'small',3,0,0,0,5,0.6,'left'],[[700,450],'small',3,0,0,0,5,0.6,'left']],
    [[[600,300],'spider',20,0,0,0,10,1,'left']],
    
    [[[600,300],'projectile',5,0,0,0,0,0.4,'left']],
    [[[500,200],'small',3,0,0,0,5,0.6,'left'],[[500,400],'small',3,0,0,0,5,0.6,'left'],[[700,300],'projectile',5,0,0,0,0,0.4,'left']],
    [[[600,100],'small',3,0,0,0,5,0.6,'left'],[[600,300],'small',3,0,0,0,5,0.6,'left'],[[600,500],'small',3,0,0,0,5,0.6,'left'],[[800,200],'projectile',5,0,0,0,0,0.4,'left'],[[800,400],'projectile',5,0,0,0,0,0.4,'left']],
    [[[500,300],'medium',6,0,0,0,10,1,'left'],[[700,300],'projectile',5,0,0,0,0,0.4,'left']],
    [[[575,268],'mask',20,0,0,0,5,0,'left']],

    [[[300,200],'small',3,0,0,0,5,0.6,'left'],[[600,200],'small',3,0,0,0,5,0.6,'left'],[[900,200],'small',3,0,0,0,5,0.6,'left'],[[300,400],'small',3,0,0,0,5,0.6,'left'],[[600,400],'small',3,0,0,0,5,0.6,'left'],[[900,400],'small',3,0,0,0,5,0.6,'left'],[[900,300],'projectile',5,0,0,0,0,0.4,'left']],
    [[[600,100],'projectile',5,0,0,0,0,0.4,'left'],[[600,300],'projectile',5,0,0,0,0,0.4,'left'],[[600,500],'projectile',5,0,0,0,0,0.4,'left'],[[700,300],'projectile',5,0,0,0,0,0.4,'left']],
    #level 13 - definitely not a swastika
    [
        [[500,200],'small',3,0,0,0,5,0.6,'left'],
        [[600,200],'small',3,0,0,0,5,0.6,'left'],
        [[650,200],'small',3,0,0,0,5,0.6,'left'],
        [[700,200],'small',3,0,0,0,5,0.6,'left'],

        [[500,250],'small',3,0,0,0,5,0.6,'left'],
        [[600,250],'small',3,0,0,0,5,0.6,'left'],
        
        [[500,300],'small',3,0,0,0,5,0.6,'left'],
        [[550,300],'small',3,0,0,0,5,0.6,'left'],
        [[600,300],'small',3,0,0,0,5,0.6,'left'],
        [[650,300],'small',3,0,0,0,5,0.6,'left'],
        [[700,300],'small',3,0,0,0,5,0.6,'left'],

        [[600,350],'small',3,0,0,0,5,0.6,'left'],
        [[700,350],'small',3,0,0,0,5,0.6,'left'],

        [[500,400],'small',3,0,0,0,5,0.6,'left'],
        [[550,400],'small',3,0,0,0,5,0.6,'left'],
        [[600,400],'small',3,0,0,0,5,0.6,'left'],
        [[700,400],'small',3,0,0,0,5,0.6,'left']
    ],
    [[[400,100],'small',3,0,0,0,5,0.6,'left'],[[400,300],'small',3,0,0,0,5,0.6,'left'],[[400,500],'small',3,0,0,0,5,0.6,'left'],[[600,200],'medium',6,0,0,0,10,1,'left'],[[600,400],'medium',6,0,0,0,10,1,'left'],[[800,300],'projectile',5,0,0,0,0,0.4,'left']],
    
    [[[584,280],'angel',30,0,0,0,5,0.6,'left']]
]

levelcolors = [
    (255,255,255),
    
    (80,255,80),
    (80,255,80),
    (80,255,80),
    (80,255,80),
    (80,255,80),

    (30,255,200),
    (30,255,200),
    (30,255,200),
    (30,255,200),
    (30,255,200),

    (255,200,100),
    (255,200,100),
    (255,200,100),
    (255,200,100),
    
    (0,0,0)
]

healthpacklevels = [1,3,5,7,9,10,11,12,13,14,15] #level 15 is unnecessary but whatever

#used for the angel boss which has a black background
whiteplayerlevels = [15,]
'END BLOCK'
