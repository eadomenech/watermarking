# -*- coding: utf-8 -*-
from Shivani2017F import Shivani2017F
from block_tools.blocks_class import BlocksImage

from tkinter import filedialog
from tkinter import *

from PIL import Image
import numpy as np

from evaluations.evaluations import Evaluations


def main():
    # Shivani2017F Instances
    wm = Shivani2017F('password')

    try:
        # Load cover image
        root = Tk()
        root.filename = filedialog.askopenfilename(
            initialdir="static/", title="Select file",
            filetypes=(
                ("all files", "*.*") ,("png files", "*.jpg"),
                ("jpg files", "*.png")
                )
            )
        watermarked_image = Image.open(root.filename).convert('RGB')
        root.destroy()

        wm.extract(watermarked_image).save('static/tamper_detection.png')
    except Exception as e:
        root.destroy()
        print("Error: ", e)
        print("The image file was not loaded")


if __name__ == '__main__':
    main()
