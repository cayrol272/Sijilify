# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 22:40:49 2023

@author: khairulakmal
"""
from sijilify import sijilify

# path to font
FONT = r'C:\windows\fonts\GILSANUB.ttf'
FILE_LIST = 'deposits/nama-baru.txt'
# path to sample certificate
CERTIFICATE = "deposits/Sijil Seminar Penyertaan.jpg"
Y_POS = 340
FONT_SIZE = 20
FONT_COLOR = "black"
    
#to create object using variable
# sijil = sijilify(FILE_LIST, CERTIFICATE, FONT, Y_POS, FONT_SIZE, FONT_COLOR)


#to create object using sijilify.ini
sijil = sijilify()
sijil.load_config('fasi')


#to register new template
# sijil.register('seminar')

#to list certificate available
# sijil.list_certificate()
# print(sijil.list_template())
read = sijil.read_template('fasi')

for keys, value in read.items():
   print(f'{keys} : {value}')

#modify parameter
# sijil.update('380', 'test', 'new', 'new', 'new', 'new', 'new')
# sijil.load_config('test')

#preview
# sijil.preview()


#generated
# sijil.generated()






    