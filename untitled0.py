# -*- coding: utf-8 -*-
"""
Created on Fri May  8 16:42:14 2020

@author: ramya
"""


import pygame
import speech_recognition as sr

k_light=0
k_fan=0
be_light=0
be_fan=0
ba_light=0
l_fan=0
l_light=0
status=''

image_dictionary={'kitchen':'img_kitchen.jpg',
                  1:'img_kitchen_on_fan.jpg',
                  2:'img_kitchen_both.jpg',
                  3:'img_kitchen_on_light.jpg',
                  'bedroom':'img_bedroom.jpg',
                  4:'img_bedroom_on_fan.jpg',
                  5:'img_bedroom_on_light.jpg',
                  6:'img_bedroom_both.jpg',
                  'bathroom':'img_bathroom.jpg',
                  7:'img_bathroom_on_light.jpg',
                  'livingroom':'img_living_room.jpg',
                  8:'img_living_room_on_fan.jpg',
                  9:'img_living_room_on_light.jpg',
                  0:'img_living_room_both.jpg'
                  }



pygame.init()
r=sr.Recognizer()

displaywidth = 1280
displayheight = 720

win=pygame.display.set_mode((displaywidth,displayheight))
pygame.display.set_caption('project remote sensing')

image1=pygame.image.load(image_dictionary['kitchen'])
image23=pygame.image.load(image_dictionary[7])
image1=pygame.image.load(image_dictionary['kitchen'])
image9=pygame.image.load(image_dictionary['livingroom'])
image4=pygame.image.load(image_dictionary['bedroom'])
image20=pygame.image.load(image_dictionary['bathroom'])
image2=pygame.image.load(image_dictionary[3])
image3=pygame.image.load(image_dictionary[2])
image5=pygame.image.load(image_dictionary[1])
image6=pygame.image.load(image_dictionary[4])
image3=pygame.image.load(image_dictionary[2])
image7=pygame.image.load(image_dictionary[6])
image8=pygame.image.load(image_dictionary[5])
image10=pygame.image.load(image_dictionary[8])
image11=pygame.image.load(image_dictionary[0])
image40=pygame.image.load(image_dictionary[9])
image23=pygame.image.load(image_dictionary[7])

def speech():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source) 
            print("Speak:")
            audio = r.listen(source)
            command=r.recognize_google(audio)
            print(command)
          
    
            
    except:
        command = ''
        print(command)
        
    return command
        
        



    

tejas=True
while tejas:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tejas=False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                speak=speech().lower()
                
            
         
    
            if "kitchen" in speak:
                if k_light == 0 and k_fan == 0:
                    image1=pygame.image.load(image_dictionary['kitchen'])
                    win.blit(image1, (0, 0))
                    pygame.display.update()
                    
                elif k_light == 0 and k_fan == 1:
                    win.blit(image5,(0,0))
                    pygame.display.update()
                    
                elif k_light==1 and k_fan==0:
                    win.blit(image2,(0,0))
                    pygame.display.update()
                    
                elif k_light==1 and k_light==1:
                    win.blit(image3,(0,0))
                status='kitchen'
                    
            elif 'bedroom' in speak:
                if be_light==0 and be_fan==0:
                    image4=pygame.image.load(image_dictionary['bedroom'])
                    win.blit(image4,(0,0))
                    pygame.display.update()
                
                elif be_fan == 0 and be_light==1:
                    win.blit(image8,(0,0))
                    pygame.display.update()
                    
                elif be_fan==1 and be_light==0:
                    win.blit(image6,(0,0))
                    pygame.display.update()
                    
                elif be_fan==1 and be_light==1:
                    win.blit(image7,(0,0))
                    pygame.display.update()
                    
                status = 'bedroom'
                
            elif 'living' in speak and 'room' in speak:
                if l_fan==0 and l_light==0:
                    image9=pygame.image.load(image_dictionary['livingroom'])
                    win.blit(image9,(0,0))
                    pygame.display.update()
                    
                elif l_fan==1 and l_light==0:
                    win.blit(image10,(0,0))
                    pygame.display.update()
                    
                elif l_fan==0 and l_light==1:
                    win.blit(image40,(0,0))
                    pygame.display.update()
                    
                elif l_fan==1 and l_light==1:
                    win.blit(image11,(0,0))
                    
                status='living_room'
                
            elif 'bathroom' in speak:
                if ba_light==0:
                    image20=pygame.image.load(image_dictionary['bathroom'])
                    win.blit(image20,(0,0))
                    pygame.display.update()
                    
                elif ba_light==1:
                    win.blit(image23,(0,0))
                    
                status='bathroom'
                    
            if status =='kitchen':
                
                if 'on' in speak and 'light' in speak:
                    if k_light==0 and k_fan==0:
                        image2=pygame.image.load(image_dictionary[3])
                        win.blit(image2,(0,0))
                        pygame.display.update()
                        k_light=1
                        
                    elif k_light==0 and k_fan==1:
                        image3=pygame.image.load(image_dictionary[2])
                        win.blit(image3,(0,0))
                        pygame.display.update()
                        k_light=1
                        
                elif 'of' in speak and 'light' in speak:
                    if k_light==1 and k_fan==0:
                        win.blit(image1,(0,0))
                        pygame.display.update()
                        k_light=0
                        
                    elif k_light==1 and k_fan==1:
                        image5=pygame.image.load(image_dictionary[1])
                        win.blit(image5,(0,0))
                        pygame.display.update()
                        k_light=0
                        
                elif 'on' in speak and 'ac' in speak:
                    if k_light == 0 and k_fan==0:
                        win.blit(image5,(0,0))
                        pygame.display.update()
                        k_fan=1
                        
                    elif k_light==1 and k_fan == 0:
                        win.blit(image3,(0,0))
                        pygame.display.update()
                        k_fan=1
                        
                elif 'of' in speak and 'ac' in speak:
                    if k_light ==0 and k_fan == 1:
                        win.blit(image1,(0,0))
                        pygame.display.update()
                        k_fan=0
                        
                    elif k_light==1 and k_fan == 1:
                        win.blit(image2,(0,0))
                        pygame.display.update()
                        k_fan=0
                        
            
                
            elif status == 'bedroom':
                
                if 'on' in speak and 'ac' in speak:
                    if be_fan==0 and be_light == 0:
                        image6=pygame.image.load(image_dictionary[4])
                        win.blit(image6,(0,0))
                        pygame.display.update()
                        be_fan=1
                        
                    elif be_fan == 0 and be_light==1:
                        image7=pygame.image.load(image_dictionary[6])
                        win.blit(image7,(0,0))
                        pygame.display.update()
                        be_fan=1
                        
                elif 'of' in speak and 'ac' in speak:
                    if be_fan==1 and be_light==0:
                        win.blit(image4,(0,0))
                        pygame.display.update()
                        be_fan=0
                        
                    elif be_fan==1 and be_light==1:
                        image8=pygame.image.load(image_dictionary[5])
                        win.blit(image8,(0,0))
                        pygame.display.update()
                        be_fan=0
                        
                elif 'on' in speak and 'light' in speak:
                    if be_fan==0 and be_light==0:
                        win.blit(image8,(0,0))
                        pygame.display.update()
                        be_light=1
                        
                    elif be_fan==1 and be_light==0:
                        win.blit(image7,(0,0))
                        pygame.display.update()
                        be_light=1
                        
                elif 'of' in speak and 'light' in speak:
                    if be_fan==0 and be_light==1:
                        win.blit(image4,(0,0))
                        pygame.display.update()
                        be_light=0
                        
                    elif be_fan == 1 and be_light ==1:
                        win.blit(image6,(0,0))
                        pygame.display.update()
                        be_light=0            
                        
            
            elif status == 'living_room':
                
                if 'on' in speak and 'ac' in speak:
                    if l_fan==0 and l_light == 0:
                        image10=pygame.image.load(image_dictionary[8])
                        win.blit(image10,(0,0))
                        pygame.display.update()
                        l_fan=1
                        
                    elif l_fan == 0 and l_light==1:
                        image11=pygame.image.load(image_dictionary[0])
                        win.blit(image11,(0,0))
                        pygame.display.update()
                        l_fan=1
                        
                elif 'of' in speak and 'ac' in speak:
                    if l_fan==1 and l_light==0:
                        win.blit(image9,(0,0))
                        pygame.display.update()
                        l_fan=0
                        
                    elif be_fan==1 and be_light==1:
                        image40=pygame.image.load(image_dictionary[9])
                        win.blit(image40,(0,0))
                        pygame.display.update()
                        l_fan=0
                        
                elif 'on' in speak and 'light' in speak:
                    if l_fan==0 and l_light==0:
                        win.blit(image40,(0,0))
                        pygame.display.update()
                        l_light=1
                        
                    elif be_fan==1 and be_light==0:
                        win.blit(image11,(0,0))
                        pygame.display.update()
                        l_light=1
                        
                elif 'of' in speak and 'light' in speak:
                    if be_fan==0 and be_light==1:
                        win.blit(image9,(0,0))
                        pygame.display.update()
                        l_light=0
                        
                    elif be_fan == 1 and be_light ==1:
                        win.blit(image10,(0,0))
                        pygame.display.update()
                        l_light=0
                        
            
                
            elif status == 'bathroom':
                if 'on'in speak and 'light' in speak:
                    image23=pygame.image.load(image_dictionary[7])
                    win.blit(image23,(0,0))
                    pygame.display.update()
                    ba_light=1
                    
                elif 'of' in speak and 'light' in speak:
                    win.blit(image20,(0,0))
                    pygame.display.update()
                    ba_light=0
            
pygame.quit()