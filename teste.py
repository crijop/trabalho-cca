# -*- coding:utf-8 -*-
#!/usr/bin/python
# Program to read and format binary files. 
# 'rb' - read binary mode
# Use of struct.unpack
# Read 64k of memory locations.
# Write only 3 X 256 byte pages. 
# Calling functions from a class. 

from OpenFile.struct_psd import resource_block, resource_ids
from psd_tools.user_api.psd_image import PSDImage
import binascii
import commands
import re
import struct
import sys

class AnalyseFile(object):
    
    
    def __init__(self):
        
        
        self.special_file = open("teste.psd", 'rb')
        
        self.resource_list = []
        
        
        list_hex = self.special_file.read()
           
        t  = self.special_file.readline(100)
        #t_u = binascii.hexlify(t)
        #t = int(t_u, 16)
        ''''c = 0
        for a in list_hex:
            print a.encode("hex")
            if c == 50:
                break
            c += 1
            pass'''
        
        
        
            
               
        self.file_analyse = PSDImage.load("teste.psd")
       
        self.resource_ids_maker()
        
        
        self.extract_header(list_hex)
        lastIndex = self.color_mode(list_hex)
        self.image_resource(list_hex, lastIndex)
        
        
       
        pass 
    
    def resource_ids_maker(self):
        
        self.r_ids = {}
        
        self.r_ids['1061'] =  resource_ids(16, 1061, "Caption digest")
        
        print  self.r_ids.keys()
        pass
    
    def extract_header(self, list_hex):
        
        header_psd = list_hex[0:26]
        
        #print header_psd
        
        signature = header_psd[0:4]
        signature_unpack = "".join(signature)
        print "Assinatura File Header - " + signature_unpack
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
 
        #print last_index 
        lenght_image_resource_unpack = binascii.hexlify(lenght_image_resource)
        lenght_image_resource = int(lenght_image_resource_unpack, 16)
        print "Comprimento dos recursos da imagem - "+ str(lenght_image_resource)
        
        resource_info = []
        count = 0
        for a in list_hex:
            
            if(a =="8"):
                
                
                c = list_hex[count + 1]
                d = list_hex[count + 2]
                e = list_hex[count + 3]
                if(c == "B"):
                    if(d == "I"):
                        if(e == "M"):
                            #print a + c +  d+ e
                            if(count > lenght_image_resource):
                                break
                            else:
                                
                                resource_info.append(count)
                    pass
                pass
            
            count += 1
        
        #print resource_info
        
      
        
        for index in resource_info:
            
            nextIndex = resource_info.index(index)
            nextIndex += 1
            if(nextIndex >=  len(resource_info)):
                
                self.resource_list.append(resource_block(index, None, list_hex, self.r_ids))
            
            else:
                
                self.resource_list.append(resource_block(index, (resource_info[nextIndex] - 1), list_hex, self.r_ids))
            
            pass
        
       
        for resource in self.resource_list:
            resource.get_signature()
            resource.get_unic_id()
            resource.get_name()
            pass
        ########################################################
        
        begin = last_index+4
        
        image_resource = list_hex[last_index+4:last_index+4 + lenght_image_resource]
        
        #######################################################
       
        '''
     
        
        
        #######################################################
        
        
        #######################################################
        size_next_resource = image_resource[28:32]
        size_next_resource_unpack = binascii.hexlify(size_next_resource)
        
        size_next_resource = int(size_next_resource_unpack, 16)
        print "Tamanho proximo - "+ str(size_next_resource) '''           
    
    pass

AnalyseFile()