import gc
from node import Node

class Stack:

    def __init__(self) -> None:
        self.top = None
        self.size = 0
        self.__current__ = None
    

    def __iter__(self):
        self.__current__ = self.top
        return self

    def __next__(self):
        if not self.__current__:
            raise StopIteration
        else:
            next_node = self.__current__
            self.__current__ = next_node.next
        return next_node

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        return_data = 'Empty stack'
        if self.top:
            return_data = self.top.data
            self.top = self.top.next
            self.size -= 1
        return return_data
    
    def add(self, stack2):
        if len(stack2) > 0:
            for node2 in stack2:
                self.push(node2.data)
        else:
            print(f'Parameter stack is empty')


    def __contains__(self, data):
        if self.size > 0:
            return_node = self.top
            while return_node and return_node.data != data:
                return_node = return_node.next
        return return_node

    def clear(self):
        self.size = 0
        self.top = None
        gc.collect()

    def peek(self):
        return_data = 'Empty stack'
        if self.top:
            return_data = self.top.data
        return return_data
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        node = self.top
        position = 1
        return_str = '(\r\n'
        while(node):
            return_str += f'\tPosition {position} - dato {node.data}'
            position += 1
            node = node.next
        return_str += '\r\n)'
        return return_str