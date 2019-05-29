# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw
import numpy as np
from scipy import misc


def copyRectangle(image, x0, y0, x1, y1, x, y):
    '''
    Copia una parte de la imagen (rectángulo) en otra ubicación
    x0: Valor correspondiente a las x del extreme superior izquierdo
    '''
    array = misc.fromimage(image)
    for itema, a in enumerate(range(x0, x1)):
        for itemb, b in enumerate(range(y0, y1)):
            array[x+itema, y+itemb] = array[a, b]
    return misc.toimage(array)


def underline(image, x0, y0, x1, y1):
    '''
    Line draw
    '''
    array = misc.fromimage(image)
    for a in range(x1-x0):
        for b in range(y1-y0):
            array[x0+a, y0+b] = [0, 0, 0]
    return misc.toimage(array)





