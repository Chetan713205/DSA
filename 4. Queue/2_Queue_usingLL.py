class Node:
    def __init__(self, data):
        self.data=data 
        self.next=None 

class QueueUsingLL:
    def __init__(self):
        self.head=head
        self.tail=tail
        self.count=count 

    def size(self):
        return self.count 

    def isEmpty(self):
        return self.size()==0  

    def enque(self, data):
        new_node=Node(data) 
        if self.size()==0:
            self.head=new_node
            self.tail=new_node 
            count+=1 
        self.tail.next=new_node
        self.tail=new_node
        count+=1 
        return f"Inserted {data} to the queue"
    
    def front(self):
        if self.size()==0:
            return f"Queue is empty"
        return self.head.data 

    def deque(self):
        if self.isEmpty():
            return f"Queue is empty"
        data_to_be_deleted=self.head.data 
        self.head=self.head.next
        self.count-=1
        return data_to_be_deleted 
