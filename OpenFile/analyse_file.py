# -*- coding:utf-8 -*-
'''
Created on 21 de Set de 2013

@author: António Baião & Carlos Palma
'''
from psd_tools import PSDImage
import binascii
import struct


class AnalyseFile(object):
    
    
    def __init__(self, file_psd):
        
        
        self.special_file = open(file_psd, 'rb')
        
        
        
        list_hex = self.special_file.read()
           
        print self.special_file.readline()
        #print list_hex[0]
            
               
        self.file_analyse = PSDImage.load(file_psd)
       
        self.extract_header(list_hex)
        lastIndex = self.color_mode(list_hex)
        self.image_resource(list_hex, lastIndex)
       
        pass
    
    def extract_header(self, list_hex):
        
        header_psd = list_hex[0:26]
        
        #print header_psd
        
        signature = header_psd[0:4]
        signature_unpack = "".join(signature)
        
        ############################################################
        
        
        version = header_psd[4:6]
        
        version_unpack = binascii.hexlify(version)
        version = int(version_unpack, 16)
       
        
        print "Versão - "+ str(version)
        
        ############################################################
        
        channels = header_psd[12:14]
        
        channels_unpack = binascii.hexlify(channels)
        channels = int(channels_unpack, 16)
       
        
        print "Nº Canais - "+ str(channels)
        
        ############################################################
        
        height = header_psd[14:18]
        
        height_unpack = binascii.hexlify(height)
        height = int(height_unpack, 16)
       
        
        print "Altura - "+ str(height)
        
        ############################################################
        
        width = header_psd[18:22]
        
        width_unpack = binascii.hexlify(width)
        width = int(width_unpack, 16)
       
        
        print "Largura - "+ str(width)
        
        ############################################################
        
        depth = header_psd[22:24]
        
        depth_unpack = binascii.hexlify(depth)
        depth = int(depth_unpack, 16)
       
        
        print "Profundidade - "+ str(depth)
        
        ############################################################
        
        colorMode = header_psd[24:26]
        
        colorMode_unpack = binascii.hexlify(colorMode)
        colorMode = int(colorMode_unpack, 16)
       
        
        print "Modo de Cor - "+ str(colorMode)
        #print version_unpack
       
        
        #signature_unpack = struct.unpack("cccc",signature)
        
        
        #print signature_unpack
        
        
        #header = unpack('L', self.special_file)
        #print "ola"
        #print header
        #print self.file_analyse.header
        
        pass
    
    def color_mode(self, list_hex):
        
        
        lenght_color_mode = list_hex[26:30]
        
        lenght_color_mode_unpack = binascii.hexlify(lenght_color_mode)
        lenght_color_mode = int(lenght_color_mode_unpack, 16)
       
        
        print "Comprimento do Modo de Cor - "+ str(lenght_color_mode)
        
        pass
    
        return 30
    
    def image_resource(self, list_hex, last_index):
        
        lenght_image_resource = list_hex[last_index:last_index+4]
 
        lenght_image_resource_unpack = binascii.hexlify(lenght_image_resource)
        lenght_image_resource = int(lenght_image_resource_unpack, 16)
       
        
        print "Comprimento dos recursos da imagem - "+ str(lenght_image_resource)
        
        ########################################################
        
        begin = last_index+4
        
        image_resource = list_hex[last_index+4:last_index+4 + lenght_image_resource]
        
        #######################################################
        signature = image_resource[0:4]
        signature_unpack = "".join(signature)
        print signature_unpack
        
        #######################################################
        uniq_id = image_resource[4:2]
        uniq_id_unpack = binascii.hexlify(uniq_id)
        uniq_id = int(lenght_image_resource_unpack, 16)
        print "ID Unico - "+ str(uniq_id)
        
        
    
    pass
