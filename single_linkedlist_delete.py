#Write a program to delete a node in a single linkedlist.
class Node:
    def __init__(self,data):
        self.info=data
        self.link=None
class single_linkedlist:
    def __init__(self):
        self.head=None
    def delete_from_beg(self):
        if(self.head is None):
            print("Nothing to delete")
        else:
            temp=self.head
            x=temp.info
            self.head=self.head.link
            temp=None
            print("Deleted data is:",x)
    def delete_from_end(self):
        if(self.head is None):
            print("Nothing to delete")
        else:
            last=self.head
            temp=self.head
            while(last.link):
                temp=last
                last=last.link
            x=last.info
            temp.link=None
            last=None
            print("Deleted data is:",x)
    def delete_from_pos(self,pos):
        if(pos<1):
            print("Enter a valid position")
        elif(pos==1):
            if(self.head is None):
                print("Nothing to delete")
            else:
                temp=self.head
                x=temp.info
                self.head=self.head.link
                temp=None
                print("Deleted data is:",x)
        else:
            prev=self.head
            temp=self.head
            for i in range(1,pos):
                prev=temp
                temp=temp.link
            x=temp.info
            prev.link=temp.link
            temp=None
            print("Deleted data is:",x)
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
        print("Press 1 for delete from begining\nPress 2 for delete from end\nPress 3 for delete from any position\nPress 4 for display\nPress 5 for exit")
        x=int(input("Enter your choice:"))
        if(x==1):
            sl.delete_from_beg()
        elif(x==2):
            sl.delete_from_end()
        elif(x==3):
            a=int(input("Enter the position you want to delete:"))
            sl.delete_from_pos(a)
        elif(x==4):
            sl.display()
        elif(x==5):
            print("You have successfully exited")
            break
        else:
            print("WRONG CHOICE!!!|")
    
            
