#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 19:56:48 2022


chromostereopsis?

@author: tom

Uses conda env in imging.yml

conda env create --name imging --file imging.yml

#export conda env with 
#conda env export > environment.yml


"""

#set up environment

import socket #to get host machine identity
import os #file and folder functions
import numpy as np #number function
import matplotlib.pyplot as plt #plotting function
#matplotlib named colours https://matplotlib.org/stable/gallery/color/named_colors.html


print("identifying host machine")
#test which machine we are on and set working directory
if 'tom' in socket.gethostname():
    os.chdir('/home/tom/t.stafford@sheffield.ac.uk/A_UNIVERSITY/toys/chromo')
else:
    print("I don't know where I am! ")
    print("Maybe the script will run anyway...")

#clear frames directory
os.system('rm frames/*')

#image params
height=512
width=512
center=(width/2,height/2)

#colours
background=(0,0,0)
red = (255,0,0)
blu = (0,0,255)

dapple_p=0.50
minr=50

i=0

for minr in range(-160,380,5):
    i=i+1
    filename='frame'+str(i).zfill(4)

    #annumulus
    maxr=50+minr
    
    #initialise image
    blank_image = np.zeros((height,width,3), np.uint8)
    blank_image[:,:] = background
    
    
    #colour image
    def annulus(x,y,center,minr,maxr):
        '''returns true if x,y is inside annulus'''
        distance=np.sqrt((x-center[0])**2+(y-center[1])**2) #of point from center
        
        if (distance > minr) & (distance < maxr):
            return True
        else:
            return False
            
    for x in range(width):
        for y in range(height):
            if annulus(x,y,center,minr,maxr):
            #small red ring
                if np.random.rand()<dapple_p:
                    blank_image[x,y]=red
            #large blue ring
            if annulus(x,y,center,minr+100,maxr+100):
                if np.random.rand()<dapple_p:
                    blank_image[x,y]=blu
    
    #show and save image
    fig=plt.imshow(blank_image)
    
    plt.axis('off')
    plt.savefig('frames/'+filename,bbox_inches='tight',pad_inches=0)
    

#this only works if you have ffmpeg installed (and probably if you are on linux)
os.system('convert -delay 9 frames/*.png fname.gif')

'''to make loop gif
https://legacy.imagemagick.org/Usage/anim_mods/#reverse

convert fname.gif -coalesce   -duplicate 1,-2-1 \
          -quiet -layers OptimizePlus  -loop 0 patrol_cycle.gif
          
'''