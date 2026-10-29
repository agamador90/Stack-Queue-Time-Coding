from node import Node

class Queue(): #create a queue to hold the opened tickets 
    
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        temp = Node(data)

        if self.rear == None:
            self.front = self.rear = temp
        else:
            self.rear.next = temp
            self.rear = temp        
        
    def dequeue(self):
        if self.front == None:
            print("There are no open tickets!")
        else:
            temp = self.front
            self.front = temp.next
            if self.front == None:
                self.rear = None
            return temp.data        
        
    def __str__(self): #modify the dunder method
        string = "Opens tickets:  \n"
        traverser = self.front

        while traverser != None:
            string += "#"+ str(traverser.data.get_number()) + " " + str(traverser.data.get_info()) + "\n"
            traverser = traverser.next

        string += " -------------------------\n"
        return string
        