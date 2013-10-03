'''
Created on 2 de Out de 2013

@author: xama
'''
import binascii
class resource_block:
    
    
    
    def __init__(self, start_index, end_index, fullData, ids):
        
        self.ids = ids
        self.start = start_index
        self.end = end_index
        
        self.name = None
        self.name_description = None
        
        #calculo do valor a usar
        if(end_index != None):
            self.resource = fullData[start_index: end_index]
        else:
            self.resource = fullData[start_index:]
        
        #self.uId = idU
        self.data = fullData
        
        self.calc_signature()
        self.calc_unic_id()
        
        
        pass
    
    def calc_signature(self):
        
        
        self.signature = self.resource[0:4]
        
        signature_unpack = "".join(self.signature)
        self.signature = signature_unpack
        
        
        
        pass
    def get_signature(self):
        print "###################################"
        print "Assinatura - "  + self.signature
        pass
    
    
    ###############################################
    
    def calc_unic_id(self):
        
        
        self.uniq_id = self.resource[4:6]
        uniq_id_unpack = binascii.hexlify(self.uniq_id)
        self.uniq_id = int(uniq_id_unpack, 16)
  
        if str(self.uniq_id) in self.ids:
            self.size_of_id = self.ids[str(self.uniq_id)].get_dimension()
            description = self.ids[str(self.uniq_id)].get_description()
            self.calc_name(description)
        
        
        pass
    def get_unic_id(self):
        print "ID Unico - "+ str(self.uniq_id)
        pass
    
  ################################################
    def calc_name(self, description):
        self.name = self.resource[6: (6 + self.size_of_id)]
        name_unpack = binascii.hexlify(self.name)
        self.name = int(name_unpack, 16)
        self.name_description = description
    
        pass
    def get_name(self):
        print str(self.name_description) + " - "+ str(self.name)
        pass
    

class resource_ids(object):
    
    def __init__(self, dimension, number, description):
        self.number = number
        self.dimesion = dimension
        self.description = description
        pass
    
    def get_dimension(self):
        
        return self.dimesion
    pass

    def get_description(self):
        
        return self.description
    pass
    
    
