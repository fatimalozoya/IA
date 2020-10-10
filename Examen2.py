#Lista adyacente de estados
estados = {
    'Nuevo Leon': {'Coahuila', 'Tamaulipas', 'San Luis Potosi'},
    'Coahuila': {'Chihuahua', 'Durango', 'Zacatecas', 'Nuevo Leon'},
    'Chihuahua': {'Sonora', 'Sinaloa', 'Coahuila', 'Durango'},
    'Sonora': {'Baja California Norte', 'Sinaloa', 'Chihuahua'},
    'Baja California Norte': {'Baja California Sur', 'Sonora'},
    'Sinaloa': {'Nayarit', 'Durango', 'Chihuahua', 'Sonora'},
    'Durango': {'Nayarit', 'Zacatecas', 'Coahuila', 'Chihuahua', 'Sinaloa'},
    'Tamaulipas': {'Veracruz', 'San Luis Potosi', 'Nuevo Leon'},
    'San Luis Potosi': {'Hidalgo', 'Queretaro', 'Guanajuato', 'Zacatecas', 'Veracruz', 'Nuevo Leon'},
    'Zacatecas': {'Aguascalientes', 'San Luis Potosi', 'Coahuila', 'Durango', 'Jalisco'},
    'Nayarit': {'Jalisco', 'Durango', 'Sinaloa'},
    'Guanajuato': {'Michoacan','Jalisco', 'San Luis Potosi', 'Queretaro',},
    'Jalisco': {'Colima', 'Michoacan', 'Guanajuato', 'Aguascalientes', 'Zacatecas'},
    'Hidalgo': {'Estado de Mexico', 'Tlaxcala', 'Puebla', 'San Luis Potosi', 'Queretaro', 'Veracruz'},
    'Queretaro': {'Michoacan', 'Guanajuato', 'San Luis Potosi', 'Hidalgo', 'Estado de Mexico'},
    'Michoacan': {'Guerrero', 'Queretaro', 'Guanajuato', 'Estado de Mexico', 'Colima', 'Jalisco'},
    'Baja California Sur': {'Baja California Norte'},
    'Estado de Mexico': {'Ciudad de Mexico', 'Guerrero', 'Michoacan', 'Morelos', 'Hidalgo', 'Puebla', 'Tlaxcala', 'Queretaro'},
    'Ciudad de Mexico': {'Morelos', 'Estado de Mexico'},
    'Puebla': {'Oaxaca', 'Morelos', 'Tlaxcala', 'Estado de Mexico', 'Veracruz', 'Guerrero'},
    'Aguascalientes': {'Jalisco', 'Zacatecas'},
    'Veracruz': {'Tabasco', 'Chiapas', 'Oaxaca', 'Puebla', 'Hidalgo', 'San Luis Potosi', 'Tamaulipas'},
    'Tabasco': {'Chiapas', 'Campeche', 'Veracruz'},
    'Campeche': {'Yucatan', 'Tabasco', 'Quintana Roo'},
    'Oaxaca': {'Guerrero', 'Chiapas', 'Veracruz', 'Puebla'},
    'Quintana Roo': {'Campeche', 'Yucatan'},
    'Tlaxcala': {'Hidalgo', 'Puebla', 'Estado de Mexico'},
    'Colima': {'Michoacan', 'Jalisco'},
    'Morelos': {'Puebla', 'Ciudad de Mexico', 'Guerrero', 'Estado de Mexico'}, 
    'Guerrero': {'Morelos', 'Michoacan', 'Estado de Mexico', 'Oaxaca', 'Puebla'},
    'Yucatan': {'Campeche', 'Quintana Roo'},
    'Chiapas': {'Oaxaca', 'Tabasco', 'Veracruz'}
}

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pylab

v = [] # Lista para record de nodos visitados.
q = [] # Inicializa una cola

def busqanchura(v, estados, nodo):
  v.append(nodo)
  q.append(nodo)

  while q:
    b = q.pop(0) 
    print (b, end = "\n\n") 

    if estados[b]=="Nuevo Leon":
     print (b, end = "Amarillo\n") 

    for neighbour in estados[b]:
      if neighbour not in v:
        v.append(neighbour)
        q.append(neighbour)

busqanchura(v, estados, 'Nuevo Leon')