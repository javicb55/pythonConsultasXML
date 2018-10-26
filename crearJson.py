# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 13:50:59 2018

@author: Andrew
"""
import descargarWeb
import json
import os

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
            consulta = descargarWeb.descargarWeb("http://clueweb.adaptcentre.ie/WebSearcher/search?query="+lista_title[i]+lista_desc[i]+ "&selection=" +str(lista_numeros))
            commit_data = consulta.json()
            #print("valores commit_data", commit_data)
            ruta = 'data/Q' + lista_num[i].strip() + '/' + 'search.json'

            with open(ruta, 'w', encoding='utf8') as file:
                json.dump(commit_data, file, ensure_ascii=False)
            
       
            if os.path.exists('data/Q' + lista_num[i].strip() + '/documentos/'):
                print("Carpeta de los 100 DOCS ya esta creado")
            else:
                os.mkdir('data/Q' + lista_num[i].strip() + '/documentos/')
            
            counter = 1

            for doc in commit_data:
            #print(doc)
                with open('data/Q' + lista_num[i].strip() + '/documentos/' + '/DOC'+ str(counter) + '.json', 'w', encoding='utf8') as file:
                    json.dump(doc,file, ensure_ascii=False)
                counter += 1
                
          #print(i, lista_num[i], "->", lista_busqueda[i])

