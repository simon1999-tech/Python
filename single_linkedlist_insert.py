#Write a program to insert a node in a single linkedlist.
class Node:
    def __init__(self,data):
        self.info=data
        self.link=None
class single_linkedlist:
    def __init__(self):
        self.head=None
    def insert_at_beg(self,item):
        new_node=Node(item)
        if(self.head is None):
            self.head=new_node
            print("You have successfully entered the number")
            return
        else:
            new_node.link=self.head
            self.head=new_node
            print("You have successfully entered the number")
    def insert_at_end(self,item):
        new_node=Node(item)
        if(self.head is None):
            self.head=new_node
            print("You have successfully entered the number")
        else:
            temp=self.head
            while(temp.link):
                temp=temp.link
            temp.link=new_node
            print("You have successfully entered the number")
    def insert_at_position(self,item,pos):
        new_node=Node(item)
        if(pos<1):
            print("Please enter the valid position")
        elif(pos==1):
            new_node.link=self.head
            self.head=new_node
            print("You have successfully entered the number")
        else:
            temp=self.head
            for i in range(1,pos):
                temp=temp.link
            new_node.link=temp.link
            temp.link=new_node
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
        print("##########MENU##########")
        print(" Press 1 for insert at begining\n Press 2 for insert at end\n Press 3 for insert at any position\n Press 4 for display\n Press 5 for exit")
        x=int(input("Enter your choice:"))
        if(x==1):
            a=int(input("Enter the number you want to insert:"))
            sl.insert_at_beg(a)
        elif(x==2):
            a=int(input("Enter the number you want to insert:"))
            sl.insert_at_end(a)

        elif(x==3):
            a=int(input("Enter the number you want to insert:"))
            b=int(input("Enter the position:"))
            sl.insert_at_position(a,b)
        elif(x==4):
            sl.display()
        elif(x==5):
            print("You have successfully exited")
            break
        else:
            print("WRONG CHOICE!!!")
