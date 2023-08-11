from datetime import datetime
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

class queue:
    def __init__(self):
        self.list1=list()
        self.count=0
    def enqueue(self,value):
        self.list1.append(value)
        self.count=self.count+1
    def dequeue(self):
        self.list1.remove(self.list1[0])
        self.count=self.count-1

class node:
    def __init__(self,value=0):
        self.value=value
        self.next=None

class priority_queue:
    def __init__(self):
        self.binary_heap=list()
        self.size=-1
    def parent(self,i):
        return (i-1)//2
    def leftchild(self,i):
        return ((2*i)+1)
    def rightchild(self,i):
        return ((2*i)+2)
    def shiftUp(self,i):
        while((i>0) and (self.binary_heap[self.parent(i)].priority>self.binary_heap[i].priority)):
            self.swap(self.parent(i),i)
            i=self.parent(i)
    def shiftDown(self,i):
        minIndex=i
        l=self.leftchild(i)
        if((l<=self.size) and (self.binary_heap[l].priority<self.binary_heap[minIndex].priority)):
            minIndex=l
        r=self.rightchild(i)
        if(r<=self.size and self.binary_heap[r].priority < self.binary_heap[minIndex].priority):
            minIndex=r
        if(i != minIndex):
            self.swap(i,minIndex)
            self.shiftDown(minIndex)
    def insert(self,priority_queue_pcb):
        self.size=self.size+1
        self.binary_heap.append(priority_queue_pcb)
        self.shiftUp(self.size)
    def extractMin(self):
        result=self.binary_heap[0]
        self.binary_heap[0]=self.binary_heap[self.size]
        self.size=self.size-1
        self.shiftDown(0)
        return result
    def changePriority(self,i,p):
        oldp=self.binary_heap[i].priorityval
        self.binary_heap[i].priorityval=p
        if(p>oldp):
            self.shiftUp(i)
        else:
            self.shiftDown(i)
    def getmin(self):
        return self.binary_heap[0].priorityvalue
    def remove(self,i):
        self.binary_heap[i]=self.getMax()+1
        self.shiftUp(i)
        self.extractMax()
    def swap(self,i,j):
        temp=self.binary_heap[i]
        self.binary_heap[i]=pcb(self.binary_heap[j].pid,self.binary_heap[j].arrival,self.binary_heap[j].remaining,self.binary_heap.priority)
        self.binary_heap[j]=pcb(temp.pid,temp.arrival,temp.remaining,temp.priority)

class pcb:
    def __init__(self,processid,arrival_time,remaining_time,priorityvalue=0):
        self.pid=processid
        self.arrival=arrival_time
        self.remaining=remaining_time
        self.priority=arrival_time

class processor:
    def __init__(self,timesharing,preemptive,pcbobject=None):
        self.current_process=pcbobject
        self.sharing=timesharing
        self.preemptive=preemptive


class process:
    def __init__(self,pcblist,processorobj,processcount,scheduling_algorithm=1):
        self.process_heap=priority_queue()
        self.processpcblist=pcblist
        self.processorobject=processorobj
        self.schedulingalgorithm=scheduling_algorithm
        self.process_count=processcount
# scheduling algorithm 1 stands for first come first serve based scheduling algorithm which means that the priority valueof a particular process would be equal to the time elapsed since the starting of the execution of the processess until the time passed till now 

    def CPU_processing(self,process_obj):
        process_entry_time=datetime.now()
        processor_obj.currentprocess=process_obj
        process_obj.remaining=process_obj.remaining-(datetime.now()-process_entry_time).seconds
        plt.plot(datetime.now().second,process_obj.pid)

    def insertion_of_arrived_process_to_queue(self,pcbobj):
        self.process_heap.insert(pcbobj)



    #Round of putting the processes into the priority queue as well as simultaneously executing the processes according to the scheduling algorithm defined by the user
    def initialaddition(self):
        temp=self.processpcblist
        self.insertion_of_arrived_process_to_queue(temp.value)
        while(temp.next.next is not None):
            start=datetime.now()
            tempextraction=self.process_heap.extractMin()
            seconds_before_next_process=temp.next.value.arrival
            while(datetime.now()-start != (temp.next.value.arrival -temp.value.arrival)):
                self.CPU_processing(tempextraction)
            if(tempextraction.remaining >0):
                self.insertion_of_arrived_process_to_queue(tempextraction)
            temp=temp.next
            self.insertion_of_arrived_process_to_queue(temp.value)




process_number=int(input("Enter the number of unique processes"))
pcb_list=node()
temp=pcb_list
for i in range(process_number):
    arrival_time_process=int(input("Enter the arrival time of process"))
    estimated_processing_time=int(input("Enter the estimated processing time"))
    temp.value=pcb(i+1,arrival_time_process,estimated_processing_time)
    newnode=node()
    temp.next=newnode
    temp=temp.next
    

pcount=int(input("Enter the number of processors"))
processors_obj_list=list()
timesharing=int(input("Enter the timesharing if applicable , else enter 0"))
emptive=input("Enter y for preemptive and n for non preemptive")
if(emptive == 'y'):
    preemptive=True
elif(emptive == 'n'):
    preemptive=False
for i in range(pcount):
    processor_obj=processor(timesharing,preemptive)
    processors_obj_list.append(processor_obj)

process_execution=process(pcb_list,processors_obj_list[0],process_number)
process_execution.initialaddition()



