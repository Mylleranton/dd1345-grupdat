# -*- coding: utf-8 -*-
# Uppgift 2,3,4,5 Labb 2, Anton Möller

def rectangle(spacing,rows,cols,sign):
    spacing = int(spacing)
    rows = int(rows)
    cols = int(cols)
    for i in range(rows):
        print(spacing*' ' + cols*sign)
        
        
def frame(rows,cols,framewidth):
    rows = int(rows)
    cols = int(cols)
    framewidth = int(framewidth)
    for i in range(rows):
        if rows-i <= framewidth or i+1 <= framewidth:
            print(cols*'*')
        else:
            print(framewidth*'*' + (cols-2*framewidth)*' ' + framewidth*'*')
    
def triangleBaseUp(spacing,width):
    spacing = int(spacing)
    width = int(width)
    
    index = 0
    while width >= index:
        print((spacing+index/2)*' ' + (width-index)*'*')
        index += 2
    
def triangleBaseDown(spacing,width):
    spacing = int(spacing)
    width = int(width)
    
    index = 1
    while width >= index:
        totalspacing = spacing + (width+1)/2 - index/2 - 1
        print(totalspacing*' ' + index*'*')
        index += 2

def rhomb(spacing,size):
    spacing = int(spacing)
    size = int(size)

    triangleBaseDown(spacing,size)
    triangleBaseUp(spacing+1,size-2)
    
    