# sijilify.py
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 19:41:42 2023
version 1.03
@author: khairulakmal

add variable for ini file
"""

# imports
import os
from PIL import Image, ImageDraw, ImageFont
import random
import configparser
import re


class sijilify:

    

    def __init__(self, list_file = '' , certificate = '', font = '', y_pos = '', 
                 font_size = '', font_color = ''):
        """
        The constructor of the object.

        Parameters
        ----------
        list_file : TYPE, optional
            DESCRIPTION. The default is ''.
        certificate : TYPE, optional
            DESCRIPTION. The default is ''.
        font : TYPE, optional
            DESCRIPTION. The default is ''.
        y_pos : TYPE, optional
            DESCRIPTION. The default is ''.
        font_size : TYPE, optional
            DESCRIPTION. The default is ''.
        font_color : TYPE, optional
            DESCRIPTION. The default is ''.

        Returns
        -------
        None.

        """
        self.list_var = []
        self.__config = configparser.ConfigParser()
        self.directory = 'generated-certificates'
        self.__mkdir(self.directory)
        self._ini = 'sijilify.ini'
        
        if not os.path.isfile(self._ini):
            self.__create_config()
        
        if list_file:
            self.list_file = list_file        
        if certificate:
            self.certificate = certificate
        if font:
            self.font = font
        if font_size:
            self.font_size = font_size
        if font_color:
            self.font_color = font_color
        if y_pos:
            self.y_pos = y_pos

    
    def __delete_old_data(self):
        # for i in os.listdir("generated-certificates/"):
        #     os.remove("generated-certificates/{}".format(i))
        self.__mkdir(self.directory)
        for i in os.listdir(f"{self.directory}/"):
            os.remove(f"{self.directory}/{i}")
    
    def __cleanup_data(self):
        with open(self.list_file) as f:
            for line in f:
                self.list_var.append(line.strip())

    def __coupons(self, names: list):

        for index, name in enumerate (names):

            # adjust the position according to
            # your sample
            #text_y_position = 900
    
            # opens the image
            img = Image.open(self.certificate, mode ='r').convert('RGB')
    
            # gets the image width
            image_width = img.width
    
            # gets the image height
            #image_height = img.height
    
            # creates a drawing canvas overlay
            # on top of the image
            draw = ImageDraw.Draw(img)
    
            # gets the font object from the
            # font file (TTF)
            font = ImageFont.truetype(
                self.font,
                self.font_size # change this according to your needs
            )
    
            # fetches the text width for
            # calculations later on
            text_width, _ = draw.textsize(name, font = font)
    
            draw.text(
                (
                    # this calculation is done
                    # to centre the image
                    (image_width - text_width) / 2,
                    self.y_pos
                ),
                name,
                fill = self.font_color,           
                font = font	 )
            
            # try:
            #     # saves the image in jpg format
            #     img.save("generated-certificates/{}.jpg".format(name))
            #     print("Processing {} / {}".format(index + 1,len(names)))
            
            # except:
            #     # saves the image in jpg format for prohibited format name
            #     img.save("generated-certificates/unknown-{}.jpg".format(index))
            #     print("Processing {} / {}".format(index + 1,len(names)))
                
            try:
                # saves the image in jpg format
                img.save(f"{self.directory}/{name}.jpg")
                print("Processing {} / {} of {}".format(index + 1,len(names),self.directory))
            
            except:
                # saves the image in jpg format for prohibited format name
                img.save(f"{self.directory}/unknown-{index}.jpg")
                print("Processing {} / {} of {}".format(index + 1,len(names), self.directory))


    def preview(self, int_list = -1):
        # self.load_config(load_config)
        self.__delete_old_data()
        self.__cleanup_data()
        if int_list == -1:
            name = random.choice(self.list_var)
        else:
            name = self.list_var[int_list]
        print(f'Preview for {name}')
        local_name = [name]
        self.__coupons(local_name)
            
    def generated(self):
        # self.load_config(load_config)
        self.__delete_old_data()
        self.__cleanup_data()
        self.__coupons(self.list_var)
    
    def __create_config(self):
        self.__config[self.directory] = {'font_dir' : 'c:/windows/fonts/%(font)s',
                                                   'depo_dir' : 'deposits',
                                                   'font' : 'bahnschrift.ttf',
                                                   'file_list' : '%(depo_dir)s/sijil-fasi.txt',
                                                   'file_certificate' : '%(depo_dir)s/SIJIL FASI.jpg',
                                                   'font_size' : 20,
                                                   'font_color' : 'black',
                                                   'y_position' : 390}
      
        with open(self._ini, 'w') as configfile:
            self.__config.write(configfile)
        
    def load_config(self, section = None):
        """
        Load sijilify.ini configuration in order to preview or generated certificate

        Returns
        -------
        None.

        """
        if section == None:
            section = self.directory
         
        self.__config.read(self._ini)
        parameter = self.__config[section]
        self.list_file = self.__config.get(section, 'file_list')
        self.certificate = self.__config.get(section, 'file_certificate')
        self.font = self.__config.get(section, 'font')
        self.font_size = int(parameter['font_size'])
        self.font_color = parameter['font_color']
        self.y_pos = int(parameter['y_position'])
        self.directory = section
        

    def test(self):
        self.__config.read(self._ini)
        self.list_file = self.__config.get(self.directory, 'file_list')
        self.certificate = self.__config.get(self.directory, 'file_certificate')
        self.font = self.__config.get(self.directory, 'font')
        print(self.list_file)
        print(self.certificate)
        print(self.font)
        
    def register(self, new_cert, font = 'bahnschrift.ttf', file_list = '', file_certificate = '', 
                 font_size = '20', font_color = 'black', y_position = '200'):
        self.__config.read(self._ini)
        self.__config[new_cert] = {}
        
        if not file_list:
            file_list = new_cert
        if not file_certificate:
            file_certificate = new_cert
        
        nc = self.__config[new_cert]
        nc['font_dir'] = 'c:/windows/fonts/%(font)s'
        nc['depo_dir'] = 'deposits'
        nc['font'] = font
        nc['file_list'] = f'%(depo_dir)s/{file_list}.txt'
        nc['file_certificate'] = f'%(depo_dir)s/{file_certificate}.jpg'
        nc['font_size'] = font_size
        nc['font_color'] = font_color
        nc['y_position'] = y_position
      
        with open(self._ini, 'w') as configfile:
            self.__config.write(configfile)
        
        print(f'{new_cert} succesfully registered')
        self.__mkdir(new_cert)
         
    def __mkdir(self, directory:str):
        """
        to check directory exits or not in order to create one

        Parameters
        ----------
        directory : STRING
            name of the directory

        Returns
        -------
        None.

        """ 
        try:
            
            isExist = os.path.exists(directory)
            
            if not isExist:
                os.mkdir(directory)
                print(f'Directory {directory} created')
        except OSError as error:
            print(error) 
        
    def list_certificate(self):
        """
        to list the certificate registered in sijilify

        Returns
        -------
        None.

        """
        self.__config.read(self._ini)
        print(self.__config.sections())
        
    def list_template(self):
        """
        to list the certificate registered in sijilify

        Returns
        -------
        None.

        """
        self.__config.read(self._ini)
        lst = []
        lst = self.__config.sections()
        # for key in section:
        #     lst = key
        #print(self.__config.sections())
        return lst
    
    def read_template(self, section):
        self.__config.read(self._ini)
        lst = dict(self.__config.items(section))
        return lst

    
    def update(self, y_position = '', section = None, font = '', file_list = '', 
               file_certificate ='', font_size = '', font_color = ''):
        self.__config.read(self._ini)
        
        if section == None:
            section = self.directory

        parameter = self.__config[section]
        
        if y_position:
            if self.__validation(y_position, 'integer'):
                parameter['y_position'] = y_position
            else:
                print(f'{y_position} is not valid. Expected not more than 5000.')
                
        if font:
            if self.__validation(font, 'font'):
                parameter['font'] = font
            else:
                print(f'{font} is not valid. Expected with extention of *.ttf.')
                
        if file_list:
            if self.__validation(file_list, 'name'):
                parameter['file_list'] = f'%(depo_dir)s/{file_list}'
            else:
                print(f'{file_list} is not valid. Expected with extention of *.txt.')
                 
        if file_certificate:
            if self.__validation(file_certificate, 'image'):
                parameter['file_certificate'] = f'%(depo_dir)s/{file_certificate}'
            else:
                print(f'{file_certificate} is not valid. Expected with extention of *.jpg.')
                
        if font_size:
            if self.__validation(font_size, 'integer'):
                parameter['font_size'] = font_size
            else:
                print(f'{font_size} is not valid. Expected not more than 5000.')
            
        if font_color :
            if self.__validation(font_color, 'color'):
                parameter['font_color'] = font_color
            else:
                print(f'{font_color} is not valid. Expected only this color black, red, green, yellow, blue, magenta, cyan and white.')
        
        with open(self._ini, 'w') as configfile:
            self.__config.write(configfile)
        
    def __validation(self, value, type_value):
        
        result = False
        if type_value ==  'name':
            patern = r"^.*\.(txt)$"
            valid = re.compile(patern)
            if valid.search(value):
                result = True
        
        if type_value == 'image':
            patern = r"^.*\.(jpg|JPG)$"
            valid = re.compile(patern)
            if valid.search(value):
                result = True
                
        if type_value == 'font':
            patern = r"^.*\.(ttf)$"
            valid = re.compile(patern)
            if valid.search(value):
                result = True
                
        if type_value == 'integer':
            value = int(value)
            if 0 < value < 5000:
                result = True
                
        if type_value == 'color':
            patern= r"black|red|green|yellow|blue|magenta|cyan|white"
            valid = re.compile(patern)
            if valid.search(value):
                result = True
                
        return result
                  

# Driver Code
if __name__ == "__main__":
    
    # path to font
    FONT = r'C:\windows\fonts\bahnschrift.ttf'
    FILE_LIST = 'deposits/sijil-fasi.txt'
    
    # path to sample certificate
    CERTIFICATE = "deposits/SIJIL FASI.jpg"
    Y_POS = 390
    FONT_SIZE = 20
    FONT_COLOR = "black"
    
    #define
    #sijil = sijilify(FILE_LIST, CERTIFICATE, FONT, Y_POS, FONT_SIZE, FONT_COLOR)
    sijil = sijilify()
    sijil.load_config('seminar')
    # sijil.read_template()
    # print(sijil.list_template())
    
    #generated
    sijil.preview()
    #sijil.generated()
    #sijil.test()
    # sijil.register('test')
