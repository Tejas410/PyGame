"""
PyGame Library for Displaying Image
"""

""" Import Lib"""
import pygame

"""Variable for Brightness of Image"""
bright=100

""" Initialize Pygame"""
pygame.init()


""" Set the Dimension of the Screen"""
Width = 800
Height = 600

""" Set the Screen"""
screen = pygame.display.set_mode((Width,Height))


""" Set The Title of Screen"""
pygame.display.set_caption("Display Image")


""" Load the Image"""
screenImg = pygame.image.load("Images/Space.jpg")

""" Display Image at Specific Co-Ordinate"""

screen.blit(screenImg,(0,0))

""" Update the Display Continuously"""

EventStatus = "None"

while True:
    
           
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            EventStatus="Quit"
            break
        if event.type == pygame.KEYDOWN:
           if event.key==pygame.K_x:
               screenImg= pygame.image.load("Images/Sky.jpg")
               screen.blit(screenImg,(0,0))
               pygame.mixer.Sound("audio/Bell.wav")
               
           if event.key==pygame.K_y:
               screenImg= pygame.image.load("Images/Earth.jpg")
               screen.blit(screenImg,(0,0))
               
           if event.key==pygame.K_RIGHT: # This is the Right Arrow Key on Keyborad
               
               #Incrementing the brightness from 100 - 255 in steps of 20
               bright+=20
              
               if bright>=255:
                   bright=255
               
               screenImg= pygame.image.load("Images/Space.jpg")
               
               #Function to adjust brightness of the image
               screenImg.fill((bright,bright,bright),special_flags=pygame.BLEND_RGB_ADD)
               screen.blit(screenImg,(0,0))
              
              
           if event.key==pygame.K_h:
               screenImg= pygame.image.load("Images/Space.jpg")
               screen.blit(screenImg,(0,0))

        
    if EventStatus == "Quit":
        break
    
print("Closing")
    
    
        
    
     
            
        

    