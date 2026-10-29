from myqueue import Queue
from stack import Stack
from ticket import Ticket

def show_panel():
    print("\n Welcome to Thibodeaux's Tech Triage\n "+ 
          "---------------------------------- \n" +
        "Type the number for the action you wish to perform and then hit Enter.\n"+
         "1. Open a new ticket\n"+
         "2. List All Open Tickets\n"+
         "3. Close ticket\n"+
         "4. Review All Closed Tickets \n"+
         "5. Review Previously Closed Tickets\n"+
         "6. Quit\n")
          
    
my_queue = Queue()
my_stack = Stack()

def open_ticket(): #open a ticket using a queue
    try:
        number = int(input("Provide 4 digits ticket number: ")) 
        info = str(input("Provide ticket details: ")).strip()  #strip() method is for eliminate blank spaces between the string.      

 
    except ValueError:
        print("I'm sorry, the ticket number should have a 4 digits.")
        return
    number = str(number) #convert to string to check the length 
    length = len(number)
        
    if length == 4: #check if the ticket number have 4 digits 
        new_ticket = Ticket(number,info)
        my_queue.enqueue(new_ticket)
        print("Ticket added to the system successfully.") 
    else:
        print("I'm sorry, the ticket number should have a 4 digits.")
        return
    
    
def list_open_tickets():
    if my_queue.front is not None:
        #print("Tickets on the system:\n")  
        print(my_queue)
    else: 
        print("There are no open tickets to show.\n")

def close_ticket():
    ticket = my_queue.dequeue()    
    my_stack.push(ticket) #add every closed ticket to the stack
    if ticket is not None: #verify if there is any ticket
        print("#"+ ticket.get_number()+ " " + ticket.get_info())
        print("The ticket was succesfully closed!")        
    else:
        print("There are no tickets on the system!")   

def list_all_closed_tickets():
    if my_stack.top is not None: #another way to check if the stack is empty
        print(my_stack)
    else: 
        print("There are no closed tickets to show!\n")
    
def review_previous_closed_ticket():
    temp = my_stack.peek() #hold the last ticket on the stack
    if temp is not None: #if the element is not empty it show the ticket data.
        print("The last closed ticket is: ")
        print("#"+temp.get_number()+ " "+ temp.get_info())  
        print("\n---------------------------------- \n")
    else:
        print("There are no closed tickets!\n")            
    
while True:
    show_panel()
    selection = input("What do you want to do? ").strip() 

    if selection == "1":
        open_ticket()

    elif selection == "2":
        list_open_tickets()

    elif selection == "3":
        close_ticket()      

    elif selection == "4":
        list_all_closed_tickets()    

    elif selection == "5":
        review_previous_closed_ticket()

    elif selection == "6":
        print("You just QUIT the program!")
        break

    else:
        print("I'm sorry, that is not an allowed action.\n")  