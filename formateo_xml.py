# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

from arbolDirectorios import arbol_directorios
from bs4 import BeautifulSoup
import os

def formatearXML():

    tree = ET.parse('NEWSELUJA_queries_spanish.xml')
    root = tree.getroot()
    listaConsultas = []
    
    for child in root:
        #print(child.tag)
        query = child
        dic = {}
        for neighbor in query:
            #print(neighbor.tag, neighbor.text) sacamos los nietos de root
            dic[neighbor.tag] = neighbor.text
        listaConsultas.append(dic)
        #print(dic)
        #print(listaConsultas)

    #se saca lista de num
    lista_num = []
    for reg in listaConsultas:
        lista_num.append(reg['num'])
    
    #arbol directorios que contendrá los ficheros
    if os.path.exists('dataFormat'):
        print("El arbol de directorios ya existe...")
    else:
        print("El arbol de directorios creado")
        os.mkdir('dataFormat')
        for reg in listaConsultas:
            if os.path.exists('dataFormat/' + reg['num']):
                print("Directorio de usuarios ya existe...")
            else:
                os.makedirs('dataFormat/' + reg['num'])
    
    arbol_directorios(listaConsultas)

    return listaConsultas

formatearXML()