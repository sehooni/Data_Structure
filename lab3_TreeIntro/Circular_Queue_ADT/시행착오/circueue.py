class CircularQueue:

#큐 초기화
    def __init__(self, max):
        self.maxQsize = max
        self.data = [None] * self.maxQsize
        self.qsize = 0
        self.front = 0
        # self.first = 0
        self.rear = 0

    # # 현재 큐 길이를 반환
    # def size(self):
    #     return self.qsize

    def __len__(self):
        return (self.rear - self.front + self.maxQsize) % self.maxQsize

    # 큐가 비어있는지
    def isEmpty(self):
        # if self.qsize == 0:
        #     return True
        #
        # return False

        # return self.qsize == 0
        return self.front == self.rear
        # if self.front == self.rear:
        #     if self.rear == None:
        #         return False
        #     return True
        # return False

    # 큐가 꽉 차있는지
    def isFull(self):
        return self.front == (self.rear+1)%self.maxQsize
        # if self.rear == None:
        #     self.rear = 0
        #     # return False
        # # return self.qsize == self.maxQsize
        # # return self.next_index(self.rear) == self.front
        #     next = self.next_index(self.rear)
        #     if next == self.front:
        #         return True
        # else:
        #     next = self.next_index(self.rear)
        #     if next == self.front:
        #         return True
        # return False
        # next = self.next_index(self.rear)
        # if next == self.front:
        #     if self.rear != None:
        #         return True
        # return False

    def next_index(self, idx):
        return (idx + 1) % self.maxQsize
        # idx += 1
        # if idx >= self.maxQsize:
        #     idx = 0
        # return idx

    # 데이터 원소 추가
    def enqueue(self, x):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.maxQsize
            self.data[self.rear] = x
        # if self.isFull():
        #     print('Queue is full')
        #
        # # 시작 index를 0으로 한다
        # if self.rear == None:
        #     self.rear = 0
        # else:
        #     self.rear = self.next_index(self.rear)
        #
        # self.data[self.rear] = x
        # self.qsize += 1
        # return self.data[self.rear]

        # self.rear = (self.rear + 1) % self.maxQsize
        # self.data[self.rear] = x
        # self.qsize += 1
        # else:
        #     self.data[self.rear % self.maxQsize] = x
        #     self.rear = self.next_index(self.rear % self.maxQsize)
        #     self.qsize += 1

    #데이터 원소 제거
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.maxQsize
            return self.data[self.front]
        else:
            print('Queue is empty')
        # if self.isEmpty():
        #     # raise IndexError('Queue empty')
        #     print('Queue is empty')
        # ret = self.data[self.front % self.maxQsize]
        # self.data[self.front % self.maxQsize] = None
        # self.front = self.next_index(self.front % self.maxQsize)
        # self.qsize -= 1
        # return ret
        # self.front = (self.front + 1) % self.maxQsize
        # x = self.data[self.front]
        # # self.qsize -= 1
        # self.front = self.next_index(self.front)
        # return x

    # # 큐의 맨 앞 원소 반환
    # def PrintFirst(self):
    #     if self.isEmpty():
    #         print('Queue empty')
    #
    #     return self.data[(self.front + 1) % self.maxQsize]
    #     # return self.data[self.next_index(self.front)]
    #
    # 큐의 맨 앞 뒤 원소 반환
    def PrintRear(self):
        if not self.isEmpty():
            print(self.data[(self.rear + 1) % self.maxQsize])
        else:
            print('Queue is empty')
        # if self.isEmpty():
        #     print('Queue is empty')
        # # return self.data[(self.rear - 1) % self.maxQsize]
        # else:
        #     print(self.data[self.rear % self.maxQsize])

    def peek(self):
        if not self.isEmpty():
            print(self.data[(self.front+1)%self.maxQsize])
        else:
            print('Queue is empty')
        # if self.isEmpty():
        #     print('Queue is empty')
        # else:
        #     # print(self.data[self.next_index(self.front)])
        #     print(self.data[(self.front) % self.maxQsize])
        #     # print(self.data[self.front])

    def display(self):
        print(self.data)
        # out = []
        # if self.front < self.rear:
        #     out = self.data[self.front+1:self.rear+1]
        # else:
        #     out = self.data[self.front+1:self.maxQsize] + self.data[0:self.rear+1]
        #
        # print("[f=%s, r=%d] ==> "%(self.front, self.rear), out)


    def clear(self):    # 큐를 초기화
        self.front = self.rear


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
        print(f"횟수 : {i + 1}")
        line = line.strip()
        # if len(line) != 1:                   # n이나 e로 input 값과 같이 들어오는 경우
        line = line.split()
        operation = line[0]
        # print(operation)
        #
        # if operation == 'n':
        #     MaxSize = line[1]
        #
        #     continue

        if operation == 'f':
            cq.peek()
            # cq.display()

        elif operation == 'r':
            cq.PrintRear()
            # cq.display()

        elif operation == 'e':
            enqueue = line[1]
            cq.enqueue(enqueue)
            cq.display()

        elif operation == 'd':
            cq.dequeue()
            cq.display()




