## Queue example: people standing in queue in ticket counter, the person coming first will be served first
## FIFO/LILO    First In First Out / Last In Last Out
## Real life example: Printer jobs, Call Center, Bank Teller, 
## Industry example: Job scheduling, Network traffic, Messaging Service(Rabbit MQ, Kafka, SQS), BFS
## ---------------------------------------------------------------------------------->
##        IN -> 8 8 8 8 8 -> OUT
##       REAR---------------FRONT
## enque: add element in queue
## deque: remove element from queue
## size: number of elements in queue
## isEmpty: check if queue is empty
## front: return the lement next to come out 

class QueueUsingList:
    def __init__(self):
        self.__queue=[] 

    def enque(self, data):
        return self.__queue.append(data)
    
    def size(self):
        if len(self.__queue)==0:
            return 0 
        return len(self.__queue)
    
    def isEmpty(self):
        return len(self.__queue)==0 

    def displayFront(self):
        if self.isEmpty():
            return None
        return self.__queue[0]

    def deque(self):
        if self.isEmpty():
            return None 
        return self.__queue.pop(0)

queue=QueueUsingList()
print(queue.isEmpty())
queue.enque(10)
queue.enque(20)
queue.enque(30)
queue.enque(40)
queue.enque(50)
print(queue.isEmpty())
print(queue.displayFront())
print(queue.size())
print(queue.deque())
print(queue.deque())
print(queue.deque())
print(queue.deque())
print(queue.deque())
print(queue.deque())