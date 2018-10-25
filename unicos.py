# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 11:08:45 2018

@author: Andrew
"""

def unicos(valores):
    
    repetido = []
    unico = []
     
    for x in valores:
    	if x not in unico:
    		unico.append(x)
    	else:
    		if x not in repetido:
    			repetido.append(x)
         
    return unico