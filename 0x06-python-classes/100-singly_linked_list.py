#!/usr/bin/python3
"""
This module implements a singly linked list
"""


class Node:
    """Defines node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """Initializes attributes"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node
    @next_node.setter
    def next_node(self, value):
        if value != None and type(value) != type(self):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """Class defines singly linked list"""
    def __init__(self):
        self.__head = None
    def sorted_insert(self, value):
        """Inserts a new node"""     
        new = Node(value)
        if self.__head is None:
            self.__head = new
        else:
            temp = self.__head
            while temp.next_node:
                if new.data < temp.data:
                    a = temp.next_node
                    temp = new
                    new.next_node = a
                temp = temp.next_node
            temp.next_node = new

    def __str__(self):
        string = ""
        printer = self.__head
        while printer.next_node:
            #if temp.data > temp.next_node.data:
             #   a = temp.data
              #  temp.data = temp.next_node.data
               # temp.next_node.data = a
            string += str(printer.data) + "\n"
            printer = printer.next_node
        #printer = temp
        #while (printer != None):
         #   string += str(printer.data) + "\n"
          #  printer = printer.next_node
        return string[:-1]
