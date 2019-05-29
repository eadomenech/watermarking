# -*- coding: utf-8 -*-
from PIL import Image
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


