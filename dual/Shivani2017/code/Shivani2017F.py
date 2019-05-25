# -*- coding: utf-8 -*-
from block_tools.blocks_class import BlocksImage
from image_tools.ImageTools import ImageTools
from helpers.utils import (
    base2decimal, decimal2base, base2base, sha256Binary)
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
        self.k1 = k1
        self.k2 = k2
        # Random vectors
        self.R1 = []
        self.R2 = []
        self.M = 0
        self.N = 0
    
    def generateR1andR2(self, M, N):
        sha1 = sha256Binary(self.k1)
        sha2 = sha256Binary(self.k2)
        posiR1 = [i for i in range((255*1000) % M)]
        posiR2 = [i for i in range((255*1000) % N)]

        i = 0
        while (len(self.R1) < M):
            if sha1[i % len(sha1)]:
                self.R1.append(posiR1[i % len(posiR1)])
            i += 1
        
        i = 0
        while (len(self.R2) < N):
            if sha2[i % len(sha2)]:
                self.R2.append(posiR2[i % len(posiR2)])
            i += 1
    
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
        a = len(array)
        b = len(array[0])
        # Runing all pixels
        for y in range(a):
            for x in range(b):
                most5Rq = self.beta(array[y, x])
                most5Pq = self.beta(array[self.R1[y], self.R2[x]])
                xor = self.xorList(most5Rq, most5Pq)
                Au = sum(xor) % 2
                if Au:
                    if (array[y, x] % 2) == 0:
                        array[y, x] += 1
                else:
                    if (array[y, x] % 2) == 1:
                        array[y, x] -= 1
        
        return Image.fromarray(array)
        

    def insert(self, cover_image):
        # Generate R1 and R2
        self.M, self.N = cover_image.size
        self.generateR1andR2(self.N, self.M)
        
        # Dividiendo en componentes RGB
        r, g, b = cover_image.split()
        
        # Marcando cada componente
        r = self.insertarEnComponente(r)
        g = self.insertarEnComponente(g)
        b = self.insertarEnComponente(b)

        return Image.merge("RGB", (r, g, b))
    
    def extractEnComponente(self, component_image):
        '''Extraer de una componente'''
        listE = []
        # Datos como array
        array = misc.fromimage(component_image)
        M = len(array)
        N = len(array[0])
        # Runing all pixels
        for m in range(M):
            for n in range(N):
                most5Rq = self.beta(array[m, n])
                most5Pq = self.beta(array[self.R1[m], self.R2[n]])
                xor = self.xorList(most5Rq, most5Pq)
                Au = sum(xor) % 2
                if Au:
                    if (array[m, n] % 2) == 0:
                        listE += [m*N + n]
                else:
                    if (array[m, n] % 2) == 1:
                        listE += [m*N + n]                  
        
        return listE
    
    def extract(self, watermarked_image):
        '''
        Retorna la imagen marcada con los pixeles modificados de
        color verde
        '''
        # Generate R1 and R2
        self.M, self.N = watermarked_image.size
        self.generateR1andR2(self.N, self.M)

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

        y = len(watermarked_array)
        x = len(watermarked_array[0])      
        
        for item in bm:
            fila = item // x
            columna = item % x
            watermarked_array[fila, columna] = [0, 255, 0]

        return misc.toimage(watermarked_array)
