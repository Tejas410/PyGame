# -*- coding: utf-8 -*-
"""
Created on Fri May  8 12:47:22 2020

@author: ramya
"""

roomdictionary={'kitchen':'img_Kitchen',
                'bathroom':'img_Bathroom',
                'bedroom':'img_Bedroom',
                'living room':'img_living_room'
                }

command_kitchen={['kitchen','on','light']:['kitchen_light_on_only','kitchen_light_fan_on'],
                 ['kitchen','fan','on']:['kitchen_fan_on_only','kitchen_light_fan_on'],
                 ['kitchen','light','off']:['img_kitchen','kitchen_fan_on_only'],
                 ['kitchen','light','off']:['img_kitchen','kitchen_light_on_only']
                 }

command_bathroom={['bathroom','on','light']:'bathroom_light_on',
                  ['bathroom','light','off']:'img_bathroom'
                  }

command_bedroom={['bedroom','light','on']:['bedroom_light_on_only','bedroom_light_fan_on'],
                 ['bedroom','fan','on']:['bedroom_fan_on','bedroom_light_fan_on'],
                 ['bedroom','light','off']:['img_bedroom','bedroom_fan_on_only'],
                 ['bedroom','fan','off']:['img_bedroom','bedroom_light_on_only']
                 }

command_living_room={['living room','light','on']:['living_room_light_on_only','living_room_light_fan_on'],
                     ['living room','fan','on']:['living_room_fan_on_only','living_room_light_fan_on'],
                     ['living room','light','off']:['img_living_room','living_room_light_on_only'],
                     ['living room','fan','off']:['img_living_room','living_room_fan_on_only']}
