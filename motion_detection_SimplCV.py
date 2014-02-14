from SimpleCV import *
from SimpleCV import Camera

cam = Camera()
while True:
        first = cam.getImage()   #getting First Image 
        second = cam.getImage()  #getting Second Image 
        diff = second-first           #substracting Second Image from First and stored in diff
        lines = diff.findLines(threshold=10, minlinelength=15)   #finding Lines in the Differenced image .
        lines.draw(width=3)                                                 #drawing Lines on the Diff image
        second.addDrawingLayer(diff.dl())                           #Drawing the lines to normal image .
        second.show()
