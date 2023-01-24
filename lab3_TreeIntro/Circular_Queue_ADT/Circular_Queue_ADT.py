'''<Lab 5-2: Circular Queue ADT>
Implement Circular Queue ADT using an array. Your Circular Queue ADT has two main operations, Enqueue and Dequeue.
In addition, you should implement two more functions for printing the first element and the last element.
- Enqueue / a new element at the end of the element in the queue. If your queue is full, just print an error message.
- Dequeue / the node in the front. If your list does not have any element, just print an error message.
- PrintFirstElem / print the first element in the queue.  If your queue is empty, just print an error message.
- PrintLastElem / print the last element in the queue.  If your queue is empty, just print an error message.
1. Input
Obtain a list of operations from the given input file, and execute the given operations in order.
A detailed specification of the operations is provided below.
Each line represents a single operation.
Each operation and the necessary parameters are separated by a space.
You may assume that the input values (represented as x and y below) are any integers.
Note that max_queue_size is the number of elements that can be stored in the queue.
    - e x: enqueue a new element with the key “x” after the last element
    - d : dequeue the first element in the queue
    - f : print the first element in the queue
    - r: print the last element in the queue
    - n x: create a new queue with the size of x. The number x is the maximum size of the queue.
        This operation will always be given in the first line of the operations in your input file. '''


class CircularQueue:

#큐 초기화
    def __init__(self, max):
        self.maxQsize = max
        self.data = [None] * self.maxQsize
        self.qsize = 0
        self.front = 0
        self.rear = -1

    # 현재 큐 길이를 반환
    def __len__(self):
        return self.qsize

    # 큐가 비어있는지
    def isEmpty(self):
        return self.qsize == 0

    # 큐가 꽉 차있는지
    def isFull(self):
        return self.qsize == self.maxQsize

    def next_index(self, idx):
        idx += 1
        if idx >= self.maxQsize:
            idx = 0
        return idx

    # 데이터 원소 추가
    def enqueue(self, x):
        if self.isFull():
            print('Queue is full')
            return self.data[self.rear]

        # 시작 index를 0으로 한다
        if self.rear == None:
            self.rear = self.front
        else:
            self.rear = self.next_index(self.rear)

        self.data[self.rear] = x
        self.qsize += 1
        return self.data[self.rear]

    #데이터 원소 제거
    def dequeue(self):
        if not self.isEmpty():
            ret = self.data[self.front]
            self.data[self.front] = None
            self.front = self.next_index(self.front)
            self.qsize -= 1
            print(ret)
        else:
            print("Queue is empty")

    # 큐의 맨 앞 뒤 원소 반환
    def PrintLastElem(self):
        if self.isEmpty():
            print('Queue is empty')
        else:
            print(self.data[(self.rear) % self.maxQsize])

    def PrintFirstElem(self):
        if not self.isEmpty():
            print(self.data[(self.front)%self.maxQsize])
        else:

            print('Queue is empty')

    def display(self):
        print(self.data)

    def MakeEmpty(self):    # 큐를 초기화
        self.front = self.rear
        self.qsize = 0


def read_file(file):
    f = open(file, 'r', encoding='UTF-8')
    content = f.readlines()
    return content


if __name__ == "__main__":
    file = 'expr_input.txt'
    documents = read_file(file)
    starting_points = documents[0].strip()
    starting_points = starting_points.split()
    MaxSize = starting_points[1]
    cq = CircularQueue(int(MaxSize))
    cq.display()

    order = documents[1:]
    for i, line in enumerate(order):
        line = line.strip()
        line = line.split()
        operation = line[0]


        if operation == 'f':
            cq.PrintFirstElem()

        elif operation == 'r':
            cq.PrintLastElem()

        elif operation == 'e':
            enqueue = line[1]
            cq.enqueue(enqueue)
            cq.display()

        elif operation == 'd':
            cq.dequeue()
            # cq.display()




