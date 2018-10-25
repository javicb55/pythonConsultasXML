# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 13:50:59 2018

@author: Andrew
"""
import descargarWeb
import json
from arbolDirectorios import arbol_directorios
from formateo_xml import formatearXML



def crearJson(lista_num, lista_title, lista_desc):
    #Se genera una lista con el número de consultas que se desean recuperar en este caso 99
    lista_numeros=[]
    for j in range(100):
        lista_numeros.append(j)
    
    #ve lanzando las consultas y guardando el json resultante en el arbol de directorios, si
    #la busqueda se ha realizado en una iteración anterior no vuelve a hacerse
    #la busqueda se hace con title y desc
    
    lista_busqueda = []

    for i in range(len(lista_num)):
        if lista_title[i] + " " + lista_desc[i] in lista_busqueda:
            print("La búsqueda ya se ha realizado anteriormente...")
        else:
            lista_busqueda.append(lista_title[i] + lista_desc[i])
            #consulta=descargarWeb.descargarWeb("http://clueweb.adaptcentre.ie/WebSearcher/search?query="+listaQueries[0]+"&selection=[1,2,3,4,5,6]")
            consulta = descargarWeb.descargarWeb("http://clueweb.adaptcentre.ie/WebSearcher/search?query="+lista_title[0]+lista_desc[0]+ "&selection=" +str(lista_numeros))
            commit_data = consulta.json()

            ruta = 'data/' + lista_num[i] + '/' + 'search.json'

            with open(ruta, 'w', encoding='utf8') as file:
                json.dump(commit_data, file)
            print(i, lista_num[i], "->")

