"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *

 * Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
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
from DISClib.Utils import error as error
from DISClib.ADT import list as lt
assert config


"""
  Este módulo implementa el tipo abstracto de datos
  cola (Queue) sobre una lista.
"""

#* TODOs GENERALES *#
#TODO: Especifiar los tipos de errores que se pueden presentar en lugar de Exception
#TODO: Actualizar las pruebas unitarias luego de realizar los cambios


#TODO: Agregar documentación con las posibles estructuras de datos que se pueden utilizar para implementar la cola
def newQueue(datastructure='SINGLE_LINKED'):
    """ Crea una cola vacia basada en una lista.
    Args:
        datastructure:  Indica el tipo de estructura de datos a utilizar
                        para implementar la cola
    Returns:
        Una cola vacia
    Raises:
        Exception
    """
    try:
        return lt.newList(datastructure)
    except Exception as exp:
        error.reraise(exp, 'TADQueue->newQueue: ')

#FIXME: Cambiar "pila" por "cola" en la documentación
#FIXME: Cambiar el mensaje de error para que sea consistente con los demás mensajes de error
#TODO: Mejorar la documentación del output de la función
def enqueue(queue, element):
    """Agrega el elemento element en el tope de la pila
    Args:
        queue: La cola donde se insertará el elemento
        element:  El elemento a insertar

    Returns:
        La cola modificada
    Raises:
        Exception
    """
    try:
        lt.addLast(queue, element)
        return queue
    except Exception as ex:
        error.reraise(ex, 'enqueue ')

#FIXME: Cambiar la descripción para decir qué hace y no qué retorna
def dequeue(queue):
    """ Retorna el elemento en la primer posición de la cola, y lo elimina.
     Args:
        queue: La cola donde se eliminará el elemento

    Returns:
        El primer elemento de la cola
    Raises:
        Exception
    """
    try:
        return lt.removeFirst(queue)
    except Exception as exp:
        error.reraise(exp, 'eTADQueu->dequeue: ')

#FIXME: Cambiar la descripción para decir qué hace y no qué retorna
#FIXME: El return de la función no es consistente con la documentación (True o el elemento)
def peek(queue):
    """ Retorna el elemento en la primer posición de la cola sin eliminarlo
    Args:
        queue: La cola  a examinar

    Returns:
        True el primer elemento de cola sin eliminarlo
    Raises:
        Exception
    """
    try:
        return lt.firstElement(queue)
    except Exception as exp:
        error.reraise(exp, 'TADQueue->isEmpty: ')

#FIXME: Cambiar el nombre de la función para que siga los lineamientos de estilo de código de Python
def isEmpty(queue):
    """Informa si la cola es vacía o no
    Args:
        queue: La cola  a examinar

    Returns:
        True si la cola es vacia, False de lo contrario
    Raises:
        Exception
    """
    try:
        return lt.isEmpty(queue)
    except Exception as exp:
        error.reraise(exp, 'TADQueue->isEmpty: ')


def size(queue):
    """Informa el número de elementos en la cola
    Args:
        queue: La cola  a examinar

    Returns:
        Retorna el tamaño de la cola

    Raises:
        Exception
    """
    try:
        return lt.size(queue)
    except Exception as exp:
        error.reraise(exp, 'TADQueue->size: ')