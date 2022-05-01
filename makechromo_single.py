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
red= (255,0,0)
blu = (0,0,255)

dapple_p=0.30
minr=50

i=0

minr=45

#annumulus
maxr=60+minr
    
#initialise image
blank_image = np.zeros((height,width,3), np.uint8)
blank_image[:,:] = background


from skimage.io import imread
from skimage.color import rgba2rgb


#eye=rgba2rgb(imread('eye2.png'))
eye=imread('eye2.png')


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

        #lids        
        x_shift=-110
        y_shift=5
        try:
            if x>abs(x_shift):
                if sum(eye[x+x_shift,y])<700:
                    if np.random.rand()<(dapple_p*1.0):
                        blank_image[x,y]=blu
        except:
            #print(x)
            rec=x
            
        if annulus(x,y,center,0,maxr+20):
        #blank middle
            blank_image[x,y]=background
        if annulus(x,y,center,minr,maxr):
        #small red ring
            if np.random.rand()<(dapple_p*1.0):
                blank_image[x,y]=red
        #large blue ring
        if annulus(x,y,center,maxr,maxr+20):
            if np.random.rand()<(dapple_p*1.0):
                blank_image[x,y]=blu
            
#show and save image
fig=plt.imshow(blank_image)

plt.axis('off')
plt.savefig('blu.png',bbox_inches='tight',pad_inches=0)
    
