# import dataclass for defining the node type
from dataclasses import dataclass
# import typing for defining the type of the element stored at the node
from typing import Generic, TypeVar, Optional


# Type for the element stored at the node
T = TypeVar("T")    # T can be any type


@dataclass
class sll_node(Generic[T]):
    """sll_node _summary_

    :param Generic: _description_
    :type Generic: _type_
    :return: _description_
    :rtype: _type_
    """
    info: T
    next_node: Optional["sll_node[T]"] = None

    def get_element(self) -> T:
        """get_element _summary_

        :return: _description_
        :rtype: T
        """        
        return self.info


@dataclass
class dll_node(Generic[T]):
    """dll_node _summary_

    :param Generic: _description_
    :type Generic: _type_
    :return: _description_
    :rtype: _type_
    """ 
    info: T
    next_node: Optional["dll_node[T]"] = None
    prev_node: Optional["dll_node[T]"] = None

    def get_element(self):
        """get_element _summary_

        :return: _description_
        :rtype: _type_
        """        
        return self.info


def get_element(node: sll_node[T] | dll_node[T]) -> T:    # T can be any type
    """get_element _summary_

    :param node: _description_
    :type node: sll_node[T] | dll_node[T]
    :return: _description_
    :rtype: T
    """
    return node.info


# def newSingleNode(element):
#         """
#         Estructura que contiene la información a guardar en una lista encadenada
#         """
#         node = {"info": element, "next": None}
#         return(node)


# def getElement(node):
#         """
#         Retorna la información de un nodo
#         Args:
#             node: El nodo a examinar
#         Returns:
#             La información almacenada en el nodo
#         """
#         return node["info"]


# def newDoubleNode(element):
#         """
#         Estructura que contiene la información a guardar en una lista encadenada
#         doblemente
#         """
#         node = {"info": element,
#                         "next": None,
#                         "prev": None
#                         }
#         return node
