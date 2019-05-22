# -*- coding: utf-8 -*-
from AvilaDomenech2019F import AvilaDomenech2019F

from tkinter import filedialog
from tkinter import *

from PIL import Image
import numpy as np

from evaluations.evaluations import Evaluations


def main():
    # AvilaDomenech2019F Instances
    wm = AvilaDomenech2019F('password')

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

        # Watermark extracting
        watermark_extracted = wm.extract(watermarked_image)
        # Save watermark image
        dir_water_im = "watermark_" + root.filename.split("/")[-1][:-4]  + ".png"
        watermark_extracted.save("static/" + dir_water_im)
    except Exception as e:
        root.destroy()
        print("Error: ", e)
        print("The image file was not loaded")


if __name__ == '__main__':
    main()
