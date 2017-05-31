import pygame 
import math
import random

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

"""
This is a basic game class that helps make the players 
and other Objects in a game.
"""

"""
The Bullet class inherits from the Sprite class. 
The Constructor takes two string variables that are 
file locations for the Image of the bullet and 
for the sound effect.
"""


class Bullet(pygame.sprite.Sprite):
    
    speed = 0
    
    """Bullet class"""
    def __init__(self, bulletImage, bulletSoundEffect):
        """Bullet constructor"""
        super(Bullet, self).__init__()
        self.image = pygame.image.load(bulletImage).convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        pew = pygame.mixer.Sound(bulletSoundEffect)
        pew.play()
        """end of Bullet constructor"""
        
    def update(self):
        """Update function"""
        self.rect.y -= self.speed
        """End of update"""
        
    def setSpeed(self, newSpeed):
        self.speed = newSpeed
        """end of set speed function"""
        
    """end of bullet class"""
    

"""
The Player class inherits from the pygame Sprite class.
The Constructor takes one string argument that is a file location for the 
image of the Player.
"""

class Player(pygame.sprite.Sprite):
    """Player Class"""
    health = 0
    exp = 0
    attack = 0
    multiplier = 1
    
    def __init__(self, playerImage):
        
        """Player constructor"""
        super(Player, self).__init__()
        
        self.image = pygame.image.load(playerImage).convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        """End of Player"""
        
    
    def playerUpdate(self, xPos, yPos):
        """playerUpdate function"""
        self.rect.x = xPos
        self.rect.y = yPos
        """end of playerUpdate function"""
        
    def setHealth(self, newHealth):
        health = newHealth
        """end of setHealth"""
        
    def getHealth(self):
        return health
    """end of getHealth"""
    
    def playerHit(self, damage):
        health -= damage
        """end of playerHit"""
    
    def playerHeal(self, heal):
        health += heal
        """End of plaerHeal"""
        
    def giveXp(self, xp):
        exp += xp
        """end of giveXp"""
        
    def takeXp(self, xp):
        exp -= xp
        """end of takeXp"""
        
    """
    put a destroyed class here maybe?
    """
    
    """end of Player class"""
    
class Enemy(Player, pygame.sprite.Sprite):
    
    health = 0
    attack = 0
    
    """End of Enemy class"""
    
class Asteroid(pygame.sprite.Sprite):
    """Asteroid class"""
    def __init__(self, image):
        super(Asteroid, self).__init__()
        self.image = pygame.image.load(image).convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        """End of Constructor"""
        
    def update(self):
        """update function"""
        self.rect.y += 3
                
        if self.rect.y > 300:
            self.reset()
        """End of Update function"""
                
    def reset(self):
        """reset function"""
        self.rect.y = random.randrange(-100, -10)
        self.rect.x = random.randrange(0, 500 - 40)
        """End of reset function"""    