#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Creates a node
class Node:
    def __init__(self, data):
        self.data = data
        # Empty next node
        self.next = None

# LinkedList Class
class LinkedList:
    
    # Constructor
    def __init__(self):
        # Empty head to start
        self.head = None
    
    # Inserts node at the start
    def insert_at_start(self, data):
        new_node = Node(data)
        
        # Check if there's no node at the beginning
        if self.head is None:
            self.head = new_node
        else:
            # Points the node to the current first node
            new_node.next = self.head
            # Turns the new node into the head of the list
            self.head = new_node
            
    # Inserts node at a given index        
    def insert(self, data, index):
        # Creates a node to be inserted
        insert_node = Node(data)
        
        # Navigating node
        nav_node = self.head
        position = 0
        
        # checks if it's at 0 first so we can use the insert at start function
        if index == 0:
            self.insert_at_start(data)
        else:
            # navigates to the position you want the node to be
            while(nav_node is not None and position+1 != index):
                position += 1
                nav_node = nav_node.next
                
            if nav_node is not None:
                insert_node.next = nav_node.next
                nav_node.next = insert_node
            # inserts it at the end if the index isn't available
            else:
                self.insert_at_end(data)
                
    # Inserts node at the end            
    def insert_at_end(self, data):
        end_node = Node(data)
        
        if self.head is None:
            self.head = end_node
            return
        
        nav_node = self.head
        
        while nav_node.next is not None:
            nav_node = nav_node.next
        
        # points the nav node next to the end node
        nav_node.next = end_node
    
    # Removes first node
    def remove_first_node(self):
        if self.head is not None:
            # Breaking off the head's chain
            self.head = self.head.next
    
    # Removes node at given index
    def remove_at_index(self, index):
        nav_node = self.head
        position = 0
        
        # checks if it's at 0 first so we can use the remove first node function
        if index == 0:
            self.remove_first_node()
        else:
            # navigates to the position you want the node to be
            while nav_node is not None and position+1 != index:
                position += 1
                nav_node = nav_node.next
                
            if nav_node is not None and nav_node.next is not None:
                nav_node.next = nav_node.next.next
            # Does nothing if we don't have that index
            else:
                return
    
    # Removes last node
    def remove_last_node(self):
        if self.head is None:
            return
        
        if self.head.next is None:
            self.head = None
            return
        
        nav_node = self.head
        while nav_node.next.next is not None:
            nav_node = nav_node.next
        
        nav_node.next = None
    
    # Finds index of a node based on its data
    def find_index(self, data):
        index = 0
        nav_node = self.head
        
        while(nav_node is not None):
            if(nav_node.data == data):
                return index
            else:
                index+=1
                nav_node = nav_node.next
        
        return 'This is not in the linked list'
        
    # Finds the sum of all of the nodes    
    def sum_nodes(self):
        nav_node = self.head
        sum_nodes = 0
        
        while(nav_node is not None):    
            # Checks to see if a string is in this
            if isinstance(nav_node.data, str):
                return 'There is an invalid data type'
            
            sum_nodes = sum_nodes + int(nav_node.data)
            nav_node = nav_node.next
            
        return sum_nodes
        
    # Prints the size of the LL
    def print_size(self):
        nav_node = self.head
        size = 0
        
        while nav_node is not None:
            size += 1
            nav_node = nav_node.next
            
        return size
    
    # Prints the list
    def print_LL(self):
        nav_node = self.head
        
        # Empty list
        ll_str = ''
        
        while nav_node is not None:
            ll_str += str(nav_node.data) + ' '
            nav_node = nav_node.next
            
        print(ll_str)

# create a new linked list
llist = LinkedList()
 
# add nodes to the linked list
llist.insert_at_start('b')
llist.print_LL()
llist.insert_at_start('a')
llist.print_LL()
llist.insert_at_end('d')
llist.print_LL()
llist.insert('c', 2)
# print the linked list
llist.print_LL()
# find the index of d
print(llist.find_index('d'))
print('\n')

# Numbers
llist2 = LinkedList()
llist2.insert_at_start(1)
llist2.print_LL()
llist2.insert_at_start(2)
llist2.print_LL()
llist2.insert_at_end(2)
llist2.print_LL()
llist2.sum_nodes()


# In[ ]:




