class CircularQueue:
    # MAXSIZE = int(max)
#큐 초기화
    def __init__(self, max):
        self.maxQsize = max
        self.data = [None for _ in range(self.maxQsize)]
        # self.qsize = 0
        self.front = 0
        # self.first = 0
        self.rear = 0

    # 현재 큐 길이를 반환
    def size(self):
        return self.qsize

    # 큐가 비어있는지a
    def isEmpty(self):
        # if self.qsize == 0:
        #     return True
        #
        # return False

        # return self.qsize == 0

        if self.front == self.rear:
            return True
        return False

    def __step_forward(self, x):
        x += 1
        if x >= self.maxQsize:
            x = 0
        return x

    # 큐가 꽉 차있는지
    def isFull(self):
        next = self.__step_forward(self.rear)
        if next == self.front:
            return True
        return False
        # if self.rear == None:
            # return False
        # return self.qsize == self.maxQsize
        # return self.next_index(self.rear) == self.front
        #
        # next = self.next_index(self.rear)
        # if next == self.front:
        #     return True
        # return False

    # def next_index(self, idx):
    #     # return (idx + 1) % self.maxQsize
    #     idx += 1
    #     if idx >= self.maxQsize:
    #         idx = 0
    #     return idx

    # 데이터 원소 추가
    def enqueue(self, x):
        if self.isFull():
            print('Queue is full')

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

        self.data[self.rear] = x
        self.rear = self.__step_forward(self.rear)

    #데이터 원소 제거
    def dequeue(self):
        if self.isEmpty():
            # raise IndexError('Queue empty')
            print('Queue is empty')
        # self.data[self.front] = None
        # self.front = self.next_index(self.front)
        # return self.data[self.front]
        # self.front = (self.front + 1) % self.maxQsize
        ret = self.data[self.front]
        # x = self.data[self.front]
        # self.qsize -= 1
        self.front = self.__step_forward(self.front)
        return ret

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
        if self.isEmpty():
            print('Queue is empty')
        # return self.data[(self.rear - 1) % self.maxQsize]
        else:
            print(self.data[self.rear])

    def peek(self):
        if self.isEmpty():
            print('Queue is empty')
        # else:
        #     # print(self.data[self.next_index(self.front)])
        #     # print(self.data[(self.front + 1) % self.maxQsize])
        #     print(self.data[self.front])
        return self.data[self.front]


    def display(self):
        print(self.data)


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


