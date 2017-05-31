import pygame
import random
import math
import GameClasses
 
# Define some colors as global constants
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
WIDTH    = 480
HEIGHT   = 272


def makeAsteroids(asteroidList, allSpritesList):
    """This function adds 75 ateroids to the star field"""
    blockWidth = 42
    blockHeight = 39
    numberOfAsteroids = 16
    for i in range(numberOfAsteroids):
        asteroid = GameClasses.Asteroid("PythonGame/TTSPasteroid.png")
            
        asteroid.rect.x = random.randrange(WIDTH - blockWidth)
        asteroid.rect.y = -(random.randrange(HEIGHT - blockHeight))
            
        asteroidList.add(asteroid)
        allSpritesList.add(asteroid)
    """End of makeAsteroids Function"""


def gameOver(allSpritesList, x, y):

    cont = pygame.sprite.Sprite()
    cont.image = pygame.image.load("PythonGame/TTSPcontinue.png").convert()
    cont.image.set_colorkey(WHITE)
    cont.rect = cont.image.get_rect()
    cont.rect.x = 575
    cont.rect.y = 100
    
    if x > 575 and y > 100:
        cont.add(allSpritesList)

    gameOver = pygame.sprite.Sprite()
    gameOver.image = pygame.image.load("PythonGame/TTSPgameover.png").convert()
    gameOver.image.set_colorkey(WHITE)
    gameOver.rect = gameOver.image.get_rect() 
    gameOver.rect.x = 575
    gameOver.rect.y = 100
    gameOver.add(allSpritesList)
    pygame.mouse.set_visible(True)
    
    
    
def theScoreText(score, screen):
    """theScoreText function"""
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, (0, 0))
    """end of theScoreTextFunction"""

def background():
    background_image = pygame.image.load("PythonGame/StarField.jpg").convert()
    return background_image


def gameLoop(screen, joystickCount, terry, redical, background_image, allSpritesList, bulletList, asteroidList):
    """gameLoop function"""
    done = False
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    
    
    bulletsFired = 0
    kills = 0
    
    score = 0
    
    xSpeed = 0
    ySpeed = 0
              
    xPos = 750
    yPos = 750
           
    x = 750
    y = 250
              
    vel = 10
    redVel = 5 
    speedMultiplier = 4    
     
    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():# User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop
                """
            elif event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                rotateAngle = math.acos(float( abs(xPos*x) - abs(yPos*y) ) )
                terry.image = pygame.transform.rotate(Surface, rotateAngle)
                terry.rect = terry.image.get_rect()
                """
                      
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if terry in allSpritesList:
                    bullet = GameClasses.Bullet("PythonGame/bullet.png", "SoundEffectsTTSP/Laser_Shoot7.ogg")
                    bullet.setSpeed(15)
                    bullet.rect.x = xPos + 25
                    bullet.rect.y = yPos
                    allSpritesList.add(bullet)
                    bulletList.add(bullet)
                    bulletsFired += 1

            
            elif event.type == pygame.KEYDOWN:
                if terry in allSpritesList:
                    if event.key == pygame.K_p:
                        bullet = GameClasses.Bullet("PythonGame/bullet.png", "SoundEffectsTTSP/Laser_Shoot7.ogg")
                        bullet.setSpeed(15)
                        bullet.rect.x = terry.rect.x + 25
                        bullet.rect.y = terry.rect.y
                        allSpritesList.add(bullet)
                        bulletList.add(bullet)
                        bulletsFired += 1
                        
                        
            if joystickCount == 0:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        xSpeed -= vel
                    if event.key == pygame.K_RIGHT:
                        xSpeed += vel
                    if event.key == pygame.K_UP:
                        ySpeed -= vel
                    if event.key == pygame.K_DOWN:
                        ySpeed += vel
                        
                                                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        xSpeed += vel
                    if event.key == pygame.K_RIGHT:
                        xSpeed -= vel
                    if event.key == pygame.K_UP:
                        ySpeed += vel
                    if event.key == pygame.K_DOWN:
                        ySpeed -= vel
                    
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]                
                        
            else:
                if myJoystick.get_axis(2) < -0.9:
                    pew.play()
    
                
            # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
          
          
            # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
        allSpritesList.update()
        
        for bullet in bulletList:
            if bullet.rect.y < -10:
                bulletList.remove(bullet)
                allSpritesList.remove(bullet)
            
        if joystickCount != 0:
            horAxisPos1 = myJoystick.get_axis(0)
            verAxisPos1 = myJoystick.get_axis(1)
                       
            xPos = xPos + int(horAxisPos1 * vel)
            yPos = yPos + int(verAxisPos1 * vel)
                
            horAxisPos2 = myJoystick.get_axis(4)
            verAxisPos2 = myJoystick.get_axis(3)
                                   
            x = x + int(horAxisPos2 * redVel) * speedMultiplier
            y = y + int(verAxisPos2 * redVel) * speedMultiplier         
                
               
                       
        else:
            xPos += xSpeed
            yPos += ySpeed
            terry.playerUpdate(xPos, yPos)
                
        if yPos >= HEIGHT-50:
            yPos = HEIGHT-50
        if yPos <= 100:
            yPos = 100
        if xPos >= WIDTH-50:
            xPos = WIDTH-50
        if xPos <= 0:
            xPos = 0
                
        if y >= 700: 
            y = 700
        if y <= 0:
            y = 0
        if x >= 1550:
            x = 1550
        if x <= 0:
            x = 0        
     
            # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
     
             
     
            # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
            # First, clear the screen to white. Don't put other drawing commands
            # above this, or they will be erased with this command.
        screen.fill(BLACK)
        screen.blit(background_image, [0, 0])
        #screen.blit(redical, [x, y])
        
        #if terry not in allSpritesList:
            #gameOver(allSpritesList, x, y)
            
        
        asteroidHitList = pygame.sprite.groupcollide(bulletList, asteroidList, True, True)
        playerHit = pygame.sprite.spritecollide(terry, asteroidList, False)
        
        if len(playerHit) > 0:
            terry.remove(allSpritesList)
            print "You Scored: %d" % (score)
            done = True

        
        
        
        for asteroid in asteroidHitList:
            kills += 1
            score += 1
            
        
        theScoreText(score, screen)
        allSpritesList.draw(screen)
            
           
                
            # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
             
            # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
            # Limit to 20 frames per second
        clock.tick(45)
             
        # Close the window and quit.
        # If you forget this line, the program will 'hang'
        # on exit if running from IDLE.
    pygame.quit()
"""End of gameLoop function"""
 
def main():
    """ Main function for the game. """
    pygame.init()
    
      
    # Set the width and height of the screen [width,height]
    size = [WIDTH, HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Terry the Terrified Spaceship Pilot")
    music = pygame.mixer.Sound("SweetMusics/TerryTheme1.ogg")
    music.play(-1)    
    
    allSpritesList = pygame.sprite.Group()
    bulletList = pygame.sprite.Group()

       
    joystickCount = pygame.joystick.get_count()
    if joystickCount == 0:
        print("Mouse and Keyboard Mode")
    else:
        myJoystick = pygame.joystick.Joystick(0)
        myJoystick.init()
        
        
    background_image = background()
    
    asteroidList = pygame.sprite.Group()
    makeAsteroids(asteroidList, allSpritesList)
    
    terry = GameClasses.Player("PythonGame/terryTheSpaceShip.png")
    terry.rect.x = WIDTH/2
    terry.rect.y = HEIGHT+30
    allSpritesList.add(terry)
    
    redical = pygame.image.load("PythonGame/TTSPRedical.png").convert()
    redical.set_colorkey(WHITE)
    #Loop until the user clicks the close button.
    
    gameLoop(screen, joystickCount, terry, redical, background_image, allSpritesList, bulletList, asteroidList)
    
    """End of main"""

if __name__ == "__main__":
    main()
    
