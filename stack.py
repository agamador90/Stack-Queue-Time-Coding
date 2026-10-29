from node import Node

class Stack(): #create a stack to hold the closed tickets
    
    def __init__(self):
        self.top = None
        self.size = 0 # just in case we need to have the stack size
        
    def push(self, data):
        temp = Node(data)
        temp.next = self.top
        self.top = temp
        self.size += 1  #this a way to add a counter to the stack, but is not used in this assignment.

    def pop(self):
        if self.top == None:
            print("There are no closed Tickets.\n")
        else:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            return temp.data
        
    def __str__(self): #modify the dunder method
        string = "Closed tickets on the system: \n"
        traverser = self.top

        while traverser != None:
            string += "#"+ str(traverser.data.get_number()) +" "+ str(traverser.data.get_info()) + "\n"
            traverser = traverser.next

        string += " -------------------------\n"
        return string       
    
    def peek(self): #to inspect the top of the stack without pop
        if self.top is not None:
            return self.top.data
        return None
