'''<Lab 6: Binary max heap>
In a max heap, the keys of parents nodes are always greater than or equal to those of the children nodes.
The max key is in the root node. In max heap ADT, we will implement two main functions, insert and deleteMax.
Additioanlly, we will implement a print function, printHeap.

•	Insert: Insert a new key to the max heap. You should find the right position for the new key to maintain the max heap.
•	DeleteMax: Delete the max in root node and reconstruct the heap to maintain max heap. If your list does not have any element, just print an error message.
•	PrintHeap: Print the entire heap. When printing, each level of the max heap should be printed in a line. If your queue is empty, just print an error message.


1.	Input
Obtain a list of operations from the given input file, and execute the given operations in order.
A detailed specification of the operations is provided below.
Each line represents a single operation. Each operation and the necessary parameters are separated by a space.
You may assume that the input values (represented as x below) are any integer.

•	n  x: create a new heap with the size of x. The number x is the maximum size of the MaxHeap.
    This operation will always be given in the first line of the operations in your input file
•	i   x: insert a new key “x” into the max heap
•	d : delete the max key in the root node
•	p : print the entire max heap. Print each level of the max heap in a line
'''


class Element:
    def __init__(self, key):
        self.key = key


class MaxHeap:
    def __init__(self, max):
        self.max_elements = max
        self.arr = [None for i in range(self.max_elements + 1)]
        self.heapsize = 0

    def is_empty(self):
        if self.heapsize == 0:
            return True
        return False

    def is_full(self):
        if self.heapsize >= self.max_elements:
            return True
        return False

    def parent(self, idx):
        return idx >> 1

    def left(self, idx):
        return idx << 1

    def right(self, idx):
        return (idx << 1) + 1

    def push(self, item):
        if self.is_full():
            print("Insert : Max Heap is full!")
            return
        # 완전 이진 트리를 유지하기 위해
        # 마지막 원소의 다음 인덱스
        self.heapsize += 1
        cur_idx = self.heapsize

        # cur_idx가 루트가 아니고
        # item의 key가 cur_idx의 부모의 키보다 크면
        while cur_idx != 1 and item.key > self.arr[self.parent(cur_idx)].key:
            self.arr[cur_idx] = self.arr[self.parent(cur_idx)]
            cur_idx = self.parent(cur_idx)
        self.arr[cur_idx] = item

    def pop(self):
        if self.is_empty():
            print("Delete : Max Haep is empty")
            return
        rem_elem = self.arr[1]      # 삭제된 후 반환될 원소

        # 맨 마지막에 위치한 원소를 받아 온 후 힙 사이즈를 줄이면 완전 이진 트리 특성 유지 가능
        temp = self.arr[self.heapsize]
        self.heapsize -= 1
        cur_idx = 1                 # 루트에서 시작
        child = self.left(cur_idx)  # 루트의 왼쪽 자식

        while child <= self.heapsize:   # child > heapsize면 arr[cur_idx]는 리프노드
            if child < self.heapsize and self.arr[self.left(cur_idx)].key < self.arr[self.right(cur_idx)].key :
                child = self.right(cur_idx)

            if temp.key >= self.arr[child].key:
                break

            self.arr[cur_idx] = self.arr[child]
            cur_idx = child
            child = self.left(cur_idx)

        self.arr[cur_idx] = temp

        return rem_elem

def print_heap(h):
    if h.is_empty():
        print("Print : Max Heap is empty")
    else:
        for i in range(1, h.heapsize+1):
            print(f"{h.arr[i].key}", end=" ")
        print()


def read_file(file):
    f = open(file, 'r', encoding='UTF-8')
    content = f.readlines()
    return content


if __name__ == "__main__":
    file = 'input.txt'
    documents = read_file(file)
    starting_points = documents[0].strip()
    starting_points = starting_points.split()
    MaxSize = starting_points[1]
    hp = MaxHeap(int(MaxSize))

    order = documents[1:]
    for i, line in enumerate(order):
        line = line.strip()
        line = line.split()
        operation = line[0]

        if operation == 'd':
           hp.pop()

        elif operation == 'p':
            print_heap(hp)

        elif operation == 'i':
            num = line[1]
            hp.push(Element(int(num)))



