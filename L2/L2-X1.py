# -*- coding: utf-8 -*-
# Uppgift X1 Labb 2, Anton Möller
    
def triangleBaseUp(spacing,width):
    spacing = int(spacing)
    width = int(width)
    
    string = ''
    
    index = 0
    while width >= index:
        string += (spacing+index/2)*' ' + (width-index)*'*' + '\n'
        index += 2
    
    return string
    
def triangleBaseDown(spacing,width):
    spacing = int(spacing)
    width = int(width)
    
    string = ''
    index = 1
    while width >= index:
        totalspacing = spacing + (width+1)/2 - index/2 - 1
        string += totalspacing*' ' + index*'*' + '\n'
        index += 2
    
    return string

def rhomb(spacing,size):
    spacing = int(spacing)
    size = int(size)
    
    return triangleBaseDown(spacing,size) + triangleBaseUp(spacing+1,size-2)
    
    