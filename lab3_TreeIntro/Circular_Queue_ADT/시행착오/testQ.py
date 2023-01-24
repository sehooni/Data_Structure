class BaseQueue:
    # 데이터의 추가
    def enqueue(self, data):
        raise NotImplemented

    # 데이터의 꺼내오기
    def dequeue(self):
        raise NotImplemented

    # 데이터 참조하기
    def peek(self):
        raise NotImplemented

    # 비어있는지 확인
    def is_empty(self):
        raise NotImplemented

    # 꽉 차있는지 확인
    def is_full(self):
        raise NotImplemented

    # 리스트 전체 출력
    def display(self):
        raise NotImplemented

class ArrayQueue(BaseQueue):
    def __init__(self, max=MAX):
        self.max = max
        self.list = [None] * self.max
        self.size = self.front = self.rear = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.next_idx(self.rear) == self.front

    def next_idx(self, idx):
        return (idx + 1) % self.max

    def enqueu(self, data):
        if self.is_full():
            raise Exception('큐가 꽉 찼습니다!')

        self.rear = self.next_idx(self.rear)
        self.list[self.rear] = data
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception('큐가 비었습니다!')

        self.front = self.next_idx(self.front)
        return self.list[self.front]

    def peek(self):
        return self.list[self.next_idx(self.front)]

    def display(self):
        current = self.front
        while current != self.rear:
            current = self.next_idx(current)
            print(self.list[current])