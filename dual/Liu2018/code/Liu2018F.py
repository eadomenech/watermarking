# -*- coding: utf-8 -*-
# from helpers.image_class import Block_RGBImage
from block_tools.blocks_class import BlocksImage
from helpers.utils import md5Binary, base2decimal, decimal2base, base2base
from PIL import Image
from scipy import misc
import numpy as np
import cv2


class Liu2018F():
    """
    This scheme is a blind dual watermarking mechanism for digital color images in which invisible fragile watermarks are embedded for image authentication.
    """

    def __init__(self, key, n=2):

        # Variables
        self.n = n
        self.wsize = 256        
        
        # Building the fragile watermark
        self.fw_binary = md5Binary(str(key))
        self.fw_decimal = base2decimal(self.fw_binary, 2)
        self.fw_3n = decimal2base(self.fw_decimal, 3 ** self.n)
    
    def calculate_E(self, U):
        '''
        This equation is equivalent to extract the LSB of unit
        U in 3^n base notational system
        '''
        suma = 0
        for i in range(len(U)):
            suma += (3 ** i) * U[i]
        E = suma % (3 ** self.n)
        return E

    def calculate_t(self, s, E):
        '''
        A temporary value t is generated for adjusting the original unit U
        '''
        import math
        t = (s - E + (3 ** self.n - 1)/2) % (3 ** self.n)
        return t
    
    def insertarEnComponente(self, component_image):
        '''Insertar en una componente'''
        # Datos como array
        array = misc.fromimage(component_image)
        # Datos como lista
        lista = array.reshape((1, array.size))[0]
        # Recorriendo los U
        for i in range(len(lista)//self.n):
            # print("{} de {}".format(i, len(lista)//self.n))
            # Get the bit to mark 
            s = self.fw_3n[i % len(self.fw_3n)]
            # Get U
            U = lista[i*self.n:(i+1)*self.n]
            # Calculate LSB of unit of U
            E = self.calculate_E(U)
            # Calculate a temporary value t
            t = self.calculate_t(s, E)
            # The temporary value t is transformed into a sequence t'
            # by using a 3-base
            t_3 = decimal2base(t, 3)
            for h in range(len(U)-len(t_3)):
                t_3.insert(0, 0)
            # Each digit in sequence t' is then reduced by 1
            t_3 = [(t_3[k] - 1) for k in range(len(t_3))]
            # Each pixel of the original n-pixel unit U is added to a
            # corresponding digit of subtracted sequence
            Up = []
            while(len(t_3) < self.n):
                t_3.insert(0, 0)
            for l in range(self.n):
                v = U[l] + t_3[(l*-1)-1]
                v = min(v, 255)
                v = max(v, 0)
                Up.append(v)
            
            lista[i*self.n:(i+1)*self.n] = Up

        array = lista.reshape(array.shape)

        return Image.fromarray(array)

    def insert(self, cover_image):
        # Dividiendo en componentes RGB
        r, g, b = cover_image.split()
        
        # Marcando cada componente
        r = self.insertarEnComponente(r)
        g = self.insertarEnComponente(g)
        b = self.insertarEnComponente(b)

        return Image.merge("RGB", (r, g, b))
    
    def extractEnComponente(self, component_image):
        '''Insertar en una componente'''
        listE = []
        # Datos como array
        array = misc.fromimage(component_image)
        # Datos como lista
        lista = array.reshape((1, array.size))[0]
        # Recorriendo los U
        for i in range(len(lista)//self.n):
            # Get U
            U = lista[i*self.n:(i+1)*self.n]
            # Calculate LSB of unit of U
            E = self.calculate_E(U)
            if E != self.fw_3n[i % len(self.fw_3n)]:
                listE += [2*i + k for k in range(self.n)]             
        
        return listE
            

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
