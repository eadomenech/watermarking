# -*- coding: utf-8 -*-
import noises

from tkinter import filedialog
from tkinter import *

from PIL import Image
import numpy as np

from evaluations.evaluations import Evaluations


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
        
        # Text addition
        noised_image = noises.copyRectangle(noised_image, 2035, 400, 2235, 2500, 3470, 400)

        # Content removal
        noised_image = noises.copyRectangle(noised_image, 1180, 2500, 1470, 2690, 1180, 2280)

        # Word substitution
        noised_image = noises.copyRectangle(noised_image, 2660, 2328, 2770, 2485, 2660, 1600)

        # Underline words
        noised_image = noises.underline(
            noised_image, 2025, 450, 2030, 1370)

        # Save image
        noised_image.save("static/noised_image.png")
        
    except Exception as e:
        root.destroy()
        print("Error: ", e)
        print("The image file was not loaded")


if __name__ == '__main__':
    main()
