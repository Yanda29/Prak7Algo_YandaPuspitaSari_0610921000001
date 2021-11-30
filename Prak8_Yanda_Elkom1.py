# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 20:25:27 2021

@author: Yanda Puspita Sari
"""

def index_ganjil(karakter):
    isian = [karakter[i] for i in range(len(karakter)) if i%2==1]
    print('Karakter Index Ganjil: ',''.join(isian))
    return(isian)

bacavalidinput=input('Masukan sebuah kata: ')
index_ganjil(bacavalidinput)
