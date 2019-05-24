# -*- coding: utf-8 -*-
from Liu2018F import Liu2018F
from block_tools.blocks_class import BlocksImage

from tkinter import filedialog
from tkinter import *

from PIL import Image
import numpy as np
from scipy import misc

import cv2

from evaluations.evaluations import Evaluations


def main():
    # Liu2018R Instances
    wm = Liu2018F('password')

    try:
        # Load cover image
        root = Tk()
        root.filename = filedialog.askopenfilename(
            initialdir="static/", title="Select file",
            filetypes=(
                ("png files", "*.jpg"), ("jpg files", "*.png"),
                ("all files", "*.*")))
        watermarked_image = Image.open(root.filename).convert('RGB')
        root.destroy()
        modifiedPixels = wm.extract(watermarked_image)
        print("Tamper detection: ", modifiedPixels)
        
        # Dividing in 1x1 blocks
        watermarked_array = misc.fromimage(watermarked_image)
        blocks = BlocksImage(watermarked_array, 1, 1)        
        
        for item in modifiedPixels:
            coord = blocks.get_coord(item)
            cv2.rectangle(
                watermarked_array, (coord[1], coord[0]),
                (coord[3], coord[2]), (0, 255, 0), 1)
        misc.toimage(watermarked_array).show()
    except Exception as e:
        root.destroy()
        print("Error: ", e)
        print("The image file was not loaded")


if __name__ == '__main__':
    main()
