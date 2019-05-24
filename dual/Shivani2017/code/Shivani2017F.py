# -*- coding: utf-8 -*-
from block_tools.blocks_class import BlocksImage
from image_tools.ImageTools import ImageTools
from helpers.utils import base2decimal, decimal2base, base2base
from PIL import Image
from scipy import misc
import numpy as np
import pywt
import cv2
import math
import random


class Shivani2017F():
    """
    The aim of the proposed scheme in this paper is to
    embed fragile watermark into the host image.
    """

    def __init__(self, k1='password1', k2='password2'):

        # Random vectors
        self.R1 = []
        self.R2 = []
        self.M = 0
        self.N = 0
    
    def generateR1andR2(self, M, N):
        for i in range(M):
            self.R1.append(random.randint(0, 255)*1000 % M)
        for i in range(N):
            self.R2.append(random.randint(0, 255)*1000 % N)
    
    def beta(self, pixel):
        '''
        Lista de 5 elementos binarios correspondientes a los 5 bit mas significativos
        '''
        binary = decimal2base(pixel, 2)
        for n in range(8-len(binary)):
            binary.insert(0, 0)
        
        return binary[:5]
    
    def xorList(self, list1, list2):
        d1 = base2decimal(list1, 2)
        d2 = base2decimal(list2, 2)
        xor = decimal2base(d1^d2, 2)
        for i in range(5-len(xor)):
            xor.insert(0, 0)
        return xor


    def insertarEnComponente(self, component_image):
        '''Insertar en una componente'''
        # Datos como array
        array = misc.fromimage(component_image)
        # Datos como lista
        lista = array.reshape((1, array.size))[0]
        # Runing all pixels
        for item, p in enumerate(lista):
            most5Rq = self.beta(p)
            most5Pq = self.beta(
                lista[self.R1[item // self.M]*self.N + self.R2[item // self.N]])
            print(self.xorList(most5Rq, most5Pq))
        
        return component_image
        

    def insert(self, cover_image):
        # Generate R1 and R2
        self.M, self.N = cover_image.size
        self.generateR1andR2(self.M, self.N)
        
        # Dividiendo en componentes RGB
        r, g, b = cover_image.split()
        
        # Marcando cada componente
        r = self.insertarEnComponente(r)
        g = self.insertarEnComponente(g)
        b = self.insertarEnComponente(b)

        return Image.merge("RGB", (r, g, b))
    
    def extractEnComponente(self, component_image):
        '''Insertar en una componente'''

        pass                   
        
        return []
    
    def extract(self, watermarked_image):
        '''
        Retorna la imagen marcada con los pixeles modificados de
        color verde
        '''
        # Dividiendo en componentes RGB
        r, g, b = watermarked_image.split()
        
        # Bloques modificados en componente Red
        bmr = self.extractEnComponente(r)
        # Bloques modificados en componente Green
        bmg = self.extractEnComponente(g)
        # Bloques modificados en componente Blue
        bmb = self.extractEnComponente(b)

        bm = list(set(bmr+bmg+bmb))

        # Dividing in 1x1 blocks
        watermarked_array = misc.fromimage(watermarked_image)
        blocks = BlocksImage(watermarked_array, 1, 1)        
        
        for item in bm:
            coord = blocks.get_coord(item)
            cv2.rectangle(
                watermarked_array, (coord[1], coord[0]),
                (coord[3], coord[2]), (0, 255, 0), 1)

        return misc.toimage(watermarked_array)
