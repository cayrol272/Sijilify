#config-parser.py
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 07:11:49 2023

@author: khairulakmal
"""
import configparser

def create_config():
    
    config = configparser.ConfigParser()
    config['path'] = {'font_dir' : 'c:/windows/fonts/',
                      'depo_dir' : 'deposits/'}
    config['generated-certificates'] = {'font' : 'bahnschrift.ttf',
                                        'font_size' : 20,
                                        'font_color' : 'black',
                                        'file_list' : 'sijil-fasi.txt',
                                        'file_certificate' : 'SIJIL FASI.jpg',
                                        'y_position' : 390}
  
    with open('sijilify.ini', 'w') as configfile:
        config.write(configfile)
        
# Driver Code
if __name__ == "__main__":
    
    create_config()
