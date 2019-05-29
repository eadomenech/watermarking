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
            filetypes=(("all files", "*.jpg"),)
        )
        cover_image = Image.open(root.filename).convert('RGB')
        root.destroy()
        
        noises.copyRectangle(cover_image, 2035, 400, 2235, 2500, 3470, 400).save("static/noised_image.jpg")
        
    except Exception as e:
        root.destroy()
        print("Error: ", e)
        print("The image file was not loaded")


if __name__ == '__main__':
    main()
