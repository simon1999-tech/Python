#Write a program to create a single linkedlist and display it.
class Node:
    def __init__(self,data):
        self.info=data
        self.link=None
class single_linkedlist:
    def __init__(self):
        self.head=None
        self.last_node=None
    def create(self,item):
        if self.head is None:
            self.head=Node(item)
            self.last_node=self.head
            print("You have successfully entered the number")
        else:
            self.last_node.link=Node(item)
            self.last_node=self.last_node.link
            print("You have successfully entered the number")
    def display(self):
        temp=self.head
        if temp is None:
            print("Linked list is empty")
        else:
            print("Element of the linked list are:")
            while(temp is not None):
                print(temp.info,end=" ")
                temp=temp.link
if __name__=="__main__":
    sl=single_linkedlist()
    while(1):
        print()
        print("####MENU####")
        print("Press 1 for insert\nPress 2 for display\nPress 3 for exit")
        x=int(input("Enter your choice:"))
        if(x==1):
            x=int(input("How many node you want to insert:"))
            for i in range(x):
                data=int(input("Enter the value of data:"))
                sl.create(data)
        elif(x==2):
            sl.display()
        elif(x==3):
            print("You have successfully exited")
            break
        else:
            print("WRONG CHOICE!!!")
