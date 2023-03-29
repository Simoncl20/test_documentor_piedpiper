"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribución de:
 *
 * Dario Correal
 *
 """

import config
import importlib
assert config

"""
  Este módulo implementa el tipo abstracto de datos
  (TAD) Map sin orden. Se puede implementar sobre una estructura
  de datos Hash Table, con resolución de colisiones: Linear Probing
  o separate chaining
"""
# GENERAL
#FIXME Cambiar todas las funciones y variables al formato snake_case
#TODO Explicar más a profundidad que tipo de excepciones y errores puede generar cada función

#FIXME Modificar documentación del numelements
def newMap(numelements=17,
           prime=109345121,
           maptype='CHAINING',
           loadfactor=0.5,
           cmpfunction=None):
    """Crea una tabla de simbolos (map) sin orden

    Args:
        numelements: Tamaño inicial de la tabla
        prime: Número primo utilizado en la función MAD
        maptype: separate chaining ('CHAINING' ) o linear probing('PROBING')
        loadfactor: Factor de carga inicial de la tabla
        cmpfunction: Funcion de comparación entre llaves
    Returns:
        Un nuevo map
    Raises:
        Exception
    """
    ht = mapSelector(maptype)
    return ht.newMap(numelements,
                     prime,
                     loadfactor,
                     cmpfunction,
                     ht)


def put(map, key, value):
    """ Ingresa una pareja llave,valor a la tabla de hash.
    Si la llave ya existe en la tabla, se reemplaza el valor

    Args:
        map: El map a donde se guarda la pareja
        key: la llave asociada a la pareja
        value: el valor asociado a la pareja
    Returns:
        El map
    Raises:
        Exception
    """
    return map['datastructure'].put(map, key, value)

#TODO Especificar que la pareja <llave,valor> es de tipo mapentry
def get(map, key):
    """ Retorna la pareja llave, valor, cuya llave sea igual a key
    Args:
        map: El map a donde se guarda la pareja
        key: la llave asociada a la pareja

    Returns:
        Una pareja <llave,valor>
    Raises:
        Exception
    """
    return map['datastructure'].get(map, key)

#TODO Modificar documentación para que siga los lineamientos de las demás funciones
def remove(map, key):
    """ Elimina la pareja llave,valor, donde llave == key.
    Args:
        map: El map a donde se guarda la pareja
        key: la llave asociada a la pareja

    Returns:
        El map
    Raises:
        Exception
    """
    return map['datastructure'].remove(map, key)

#TODO Indicar en el retorno cuando es True y cuando es False, similar a la documentación de isEmpty
def contains(map, key):
    """ Retorna True si la llave key se encuentra en el map
        o False en caso contrario.
    Args:
        map: El map a donde se guarda la pareja
        key: la llave asociada a la pareja

    Returns:
        True / False
    Raises:
        Exception
    """
    return map['datastructure'].contains(map, key)


def size(map):
    """  Retorna  el número de entradas en la tabla de hash.
    Args:
        map: El map
    Returns:
        Tamaño del map
    Raises:
        Exception
    """
    return map['datastructure'].size(map)


def isEmpty(map):
    """ Informa si la tabla de hash se encuentra vacia
    Args:
        map: El map
    Returns:
        True: El map esta vacio
        False: El map no esta vacio
    Raises:
        Exception
    """
    return map['datastructure'].isEmpty(map)

#TODO Indicar que esta es una lista de DISCLib
def keySet(map):
    """
    Retorna una lista con todas las llaves de la tabla de hash

    Args:
        map: El map
    Returns:
        lista de llaves
    Raises:
        Exception
    """
    return map['datastructure'].keySet(map)

#TODO Indicar que esta es una lista de DISCLib
def valueSet(map):
    """
    Retorna una lista con todos los valores de la tabla de hash

    Args:
        map: El map
    Returns:
        lista de valores
    Raises:
        Exception
    """
    return map['datastructure'].valueSet(map)

#FIXME Corregir error de ortografía
"""
Selector dinamico de la estructua de datos solicitada
"""

switch_module = {
    "CHAINING": ".chaininghashtable",
    "PROBING": ".probehashtable",
}

#FIXME Agregar parámetros y retorno a la documentación
def mapSelector(datastructure):
    """
    Carga dinamicamente el import de la estructura de datos
    seleccionada
    """
    ds = switch_module.get(datastructure)
    module = importlib.import_module(ds, package="DISClib.DataStructures")
    return module
