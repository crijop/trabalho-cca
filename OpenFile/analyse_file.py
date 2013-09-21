# -*- coding:utf-8 -*-
'''
Created on 21 de Set de 2013

@author: António Baião & Carlos Palma
'''
from psd_tools import PSDImage


class AnalyseFile(object):
    
    
    def __init__(self, file_psd):
        
       
        self.file_analyse = PSDImage.load(file_psd)
        
        self.extract_header()
        
        pass
    
    def extract_header(self):
        
        print self.file_analyse.header
        
        pass
        
    
    pass
