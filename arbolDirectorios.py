# -*- coding: utf-8 -*-
"""
Creamos un arbol de directorios de un archivo xml
"""

import os
import unicos
import json
 
def arbol_directorios(listadicc):
    
    lista_num   = []
    lista_title = []
    lista_desc  = []
    lista_auth  = []
    lista_lang  = []

    #Llenamos la lista del archivo xml

    for reg in listadicc:
        lista_num.append(reg['num'])
        lista_title.append(reg['title'])
        lista_desc.append(reg['desc'])
        lista_auth.append(reg['auth'])
        lista_lang.append(reg['lang'])

    #print(listadicc[12]['num'])
    #print(listadicc[12]['title'])
    #print(listadicc[12]['desc'])
    #print(listadicc[12]['auth'])
    #print(listadicc[12]['lang'])

    #Sacamos la lista de consultas unicas
    query_unicos = unicos.unicos(lista_num)
    print(query_unicos)

    #Si el directorio existe no lo crea, si existe crea el árbol de directorios

    if os.path.exists('data'):
        print("El árbol de directorios ya existe")
    else:
        print("Creado Árbol Directorios")
        os.mkdir('data')
        for reg in query_unicos:
            os.makedirs('data/' + reg)
        
        #Averiguando las sesiones de cada usuario y crear árbol

        for num in query_unicos:
            for reg in listadicc:
                if reg['num']== num:
                    #print(num, reg['num'])
                    if os.path.exists('data/' + num + '/' + 'query_datos.json'):
                        print("El directorio ya esta creado")
                    else:
                        #Creamos un archivo json para guardar la consulta en formato utf8
                        ruta= 'data/'+ num + '/' + 'consulta.json'
                        with open(ruta, 'w', encoding='utf8') as file:
                            json.dump(reg, file, ensure_ascii=False)
    return lista_num, lista_title, lista_desc, lista_auth, lista_lang                         

