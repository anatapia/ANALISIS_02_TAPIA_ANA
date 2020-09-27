# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 12:51:02 2020

@author: analaura
"""

import csv
archivo=[]
with open ("synergy_logistics_database.csv","r") as archivo_csv:
    lector=csv.reader(archivo_csv)
    
    for linea in lector:
        archivo.append(linea)
        
###############################################################################
#1
def rutas_mas_demandadas(direccion):
    
    rutas=[] #En esta lista vamos a agregar las diferentes rutas que hay en la
    #dirección dada (exportación o importación)
    rutas_contabilizadas=[] #En esta lista vamos a agregar cada ruta, el número
    #de veces que se usó la ruta y el valor total que generó la ruta.
    
    for x in archivo:
        if x[1]==direccion:
            ruta=[x[2],x[3]]
            
            if ruta not in rutas:
                rutas.append(ruta)
                contador=0
                suma=0
                for y in archivo:
                    if y[1]==direccion:
                        ruta_a_comparar=[y[2],y[3]]
                        if ruta==ruta_a_comparar:
                            contador+=1
                            suma+=int(y[9])
                rutas_contabilizadas.append([ruta,contador,suma])
    
    #Vamos a ordenar rutas_contabilizadas de mayor a menor respecto al número
    #de veces que se usó la ruta
    rutas_contabilizadas.sort(reverse=True,key=lambda x: x[1])
    print()
    print(f"Las 10 rutas más demandadas para {direccion} son: ")
    for i in range(0,10):
        print(f"{i+1}.La ruta {rutas_contabilizadas[i][0]} fue utilizada: {rutas_contabilizadas[i][1]} veces")
   
    #Vamos a ordenar rutas_contabilizadas de mayor a menor respecto al número
    #total de valor por ruta.
    print()
    rutas_contabilizadas.sort(reverse=True,key=lambda x: x[2])
    print(f"Las 10 rutas que generan más valor para {direccion} son: ")
    for i in range(0,10):
        print(f"{i+1}.La ruta {rutas_contabilizadas[i][0]} generó un valor de: {rutas_contabilizadas[i][2]}")





rutas_mas_demandadas("Exports")
rutas_mas_demandadas("Imports")




##############################################################################
#2
transportes=[] #En esta lista vamos a ir añadiendo los diferentes transportes
#que se utilizan
for x in archivo:
    if x[7]=="transport_mode":
        continue
    if x[7] not in transportes:
        transportes.append(x[7])

#En esta función, a través de un ciclo for vamos a sumar el valor que generó
#cada transporte ya sea para exportaciones o importaciones.
def transportes_mas_importantes(direccion):
    
    transportes_valores=[] #Esta lista contendrá otras listas que indicarán
    #cada transporte y el valor que este generó.
    for transporte in transportes:
            suma=0
            for x in archivo:
                if x[1]==direccion:
                    if x[7]==transporte:
                        suma+=int(x[9])
            transportes_valores.append([transporte,suma])
    
    #Vamos a ordenar transportes_valores de mayor a menor respecto al valor 
    #total para poder ver cuáles son los 3 transportes más importantes.
    transportes_valores.sort(reverse=True,key=lambda x:x[1])    
    print()
    print(f"Los 3 medios de transporte más importantes para {direccion} son: ")
    for i in range(0,3):
        print(f"{i+1}.{transportes_valores[i][0]} generó un valor de: {transportes_valores[i][1]}")





transportes_mas_importantes("Exports")
transportes_mas_importantes("Imports")



##############################################################################
#3
#En esta función vamos a hacer una lista de los países que generan el 80% del
#valor ya sea para exportaciones o importaciones.
def paises_mas_importantes(direccion):
    
    paises=[] #A través de un ciclo for vamos a ir añadiendo a la lista "paises"
    #los diferentes países, en el caso de las exportaciones añadiremos
    #los distintos países de origen y en el caso de las importaciones, los 
    #distintos países de destino.
    
    pais_valor_total=[] #De igual manera, a través del ciclo for vamos a añadir
    #a esta lista el nombre del país con el valor total que generó dicho país
    total=0 #Esta variable será la suma total de los valores que generó cada país,
    #Es decir, el valor total de TODAS las exportaciones o TODAS las importaciones.
    for x in archivo:
        if direccion=="Exports":
            if x[1]==direccion:
                if x[2] not in paises:
                    paises.append(x[2])
                    suma=0
                    for y in archivo:
                        if y[1]==direccion:
                            if x[2]==y[2]:
                              suma+=int(y[9])                        
                    pais_valor_total.append([x[2],suma])
                    total+=suma
        else: #Si direccion== "Imports":
            if x[1]==direccion:
                if x[3] not in paises:
                    paises.append(x[3])
                    suma=0
                    for y in archivo:
                        if y[1]==direccion:
                            if x[3]==y[3]:
                              suma+=int(y[9])
                    pais_valor_total.append([x[3],suma])
                    total+=suma
    #Es una codigote porque en el caso de las exportaciones necesitamos la 
    #columa 3 y en el caso de las importaciones la columna 4 del archivo.
    
    #Ya que tenemos la lista de cada país (ya sea para importación o exportación),
    #vamos a ordenarla de mayor a menor respecto al valor total para saber cuáles
    #son los países más importantes
    pais_valor_total.sort(reverse=True,key=lambda x:x[1])
    
    #Queremos saber qué países general el 80% del valor total ya sea de importaciones
    #o exportaciones, por lo que multiplicamos por 0.80 la suma total
    p=total*0.80
    
    #Ahora vamos a ver qué países son los que generan el 80% del valor total
    #Sumaremos el porcentaje que representa cada país, hasta que lleguemos a 80%
    #Recordemos que los países ya están ordenados de mayor a menor, así que vamos
    #a calcular qué porcentaje representa el valor de cada país respecto al 
    #valor total general
    suma=0
    paises_80=[] #En esta lista añadiremos unicamente el nombre de los países
    #que se van sumando hasta que lleguemos a 80%
    paises_y_porcentajes=[] #En esta lista vamos a añadir el nombre del país y
    #su porcentaje respecto al valor total de todas las exportaciones o importaciones
    contador=0
    while suma<p: #Este ciclo irá sumando los valores de los países hasta que lleguemos al 80%
        #La variable suma irá sumando los valores que generó cada país    
        suma+=pais_valor_total[contador][1]
        paises_y_porcentajes.append([pais_valor_total[contador][0],pais_valor_total[contador][1]/total*100])
        paises_80.append(pais_valor_total[contador][0])
        contador+=1
    
    #No precisamente tendremos el 80% exacto, se va a pasar un poquito, así que
    #mostraremos el porcentaje real que representan los países de la lista paises_80
    porcentaje=(suma/total)*100
    print()
    print(f"De un total de {total}, los siguientes países generan el {porcentaje}% del valor de las {direccion}")
    i=1
    for pais in paises_y_porcentajes:
        print(f"{i}.{pais[0]} genera el:{pais[1]}%")
        i+=1    
    
    #Ahora vamos a ver cuáles son los productos que los países de paises_80 más
    #exportan o importan dependiendo el caso
     
    productos=[]
    for x in archivo:
        if direccion=="Exports":
            if x[1]==direccion:
                if x[2] in paises_80:
                    if x[6] not in productos:
                        productos.append(x[6])
        else:
            if x[1]==direccion:
                if x[3] in paises_80:
                    if x[6] not in productos:
                        productos.append(x[6])
                        
    print()
    print(f"Los productos más comercializados son: {productos}")
            
                    
                
        
            
    
       
paises_mas_importantes("Exports")
paises_mas_importantes("Imports")                  
                    
                    
                    
                    