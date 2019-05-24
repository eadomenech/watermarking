# -*- coding: utf-8 -*-
from Shivani2017F import Shivani2017F

from tkinter import filedialog
from tkinter import *

from PIL import Image
import numpy as np

from evaluations.evaluations import Evaluations


def main():
    # Liu2018R Instances
    wm = Shivani2017F()

    try:
        # Load cover image
        root = Tk()
        root.filename = filedialog.askopenfilename(
            initialdir="static/", title="Select file",
            filetypes=(
                ("all files", "*.*"), ("png files", "*.png"), ("jpg files", "*.jpg"),
                )
            )
        cover_image = Image.open(root.filename).convert('RGB')
        root.destroy()
        watermarked_image = wm.insert(cover_image)
        watermarked_image.save("static/watermarked_image.png")

        # PSNR
        cover_image = Image.open(root.filename)
        stego_image = Image.open("static/watermarked_image.png").convert('RGB')
        print("Calculando PSNR")
        print(Evaluations().PSNR_RGB(cover_image, stego_image))
        
    except Exception as e:
        root.destroy()
        print("Error: ", e)
        print("The image file was not loaded")


if __name__ == '__main__':
    main()
