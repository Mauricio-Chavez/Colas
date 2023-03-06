class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Queue:
    def __init__(self):
        self.first=None
        self.length=0

    def enqueue(self,value):
        new_node=Node(value)
        if self.first==None:
            self.first=new_node
            self.last=new_node
        else:
            self.last.next=new_node
            self.last =new_node

        self.length +=1
        return
    def print_queue(self):
        tem=self.first
        while tem is not None:
            print(tem.value)
            tem = tem.next
        return
    def dequeue(self):
        tem = self.first
        if self.first==self.last:
            self.first=None
            self.last=None
        else:
            self.first=tem.next
            tem.next=None

        self.length-=1
        return tem.value

    def getvalue(self,i):
        tem = self.first
        if i<=self.length and i>0:
            for j in range(1,i):
                tem=tem.next
            print(tem.value)

        else:
            print(("El indice ingresado no existe"))

my_queue=Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.print_queue()
print("----------------------------------")
my_queue.dequeue()
my_queue.print_queue()
print("----------------------------------")
my_queue.getvalue(2)

