# -*- coding: utf-8 -*-
from tkinter import filedialog
from tkinter import *

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
            array[x+itema, y+itemb] = [255, 255, 255]
    return misc.toimage(array)


def underline(image, x0, y0, x1, y1):
    '''
    Line draw
    '''
    array = misc.fromimage(image)
    for a in range(x1-x0):
        for b in range(y1-y0):
            array[x0+a, y0+b] = [255, 255, 255]
    return misc.toimage(array)


def main():

    try:
        # Load cover image
        root = Tk()
        root.filename = filedialog.askopenfilename(
            initialdir="static/", title="Select file",
            filetypes=(("all files", "*.*"),)
        )
        noised_image = Image.open(root.filename).convert('RGB')
        root.destroy()

        array = misc.fromimage(noised_image)
        for x in range(len(array)):
            for y in range(len(array[0])):
                array[x, y] = [0, 0, 0]
        
        noised_image = misc.toimage(array)
        
        # Text addition
        noised_image = copyRectangle(
            noised_image, 2035, 400, 2235, 2500, 3470, 400)

        # Content removal
        noised_image = copyRectangle(
            noised_image, 1180, 2500, 1470, 2690, 1180, 2280)

        # Word substitution
        noised_image = copyRectangle(
            noised_image, 2660, 2328, 2770, 2485, 2660, 1600)

        # Underline words
        noised_image = underline(noised_image, 2025, 450, 2030, 1370)

        # Save image
        noised_image.save("static/tamper_zone.png")
        
    except Exception as e:
        root.destroy()
        print("Error: ", e)
        print("The image file was not loaded")


if __name__ == '__main__':
    main()
