class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def printlist(self):
        temp = self.head

        # Print Directly
        print(temp.value)
        print(temp.next.value)
        print(temp.next.next.value)

        # Can use while loop
        while temp:
            print(temp.value,end=" ")
            temp = temp.next  


if __name__=='__main__':
 
    # Start with the empty list
    linklist = SingleLinkedList()

    # Creating the Nodes
    first = Node(1)
    second = Node(2)
    third = Node(3)
 
    linklist.head = first
    linklist.head.next = second; # Link first node with second
    second.next = third; # Link second node with the third node
 
    linklist.printlist()