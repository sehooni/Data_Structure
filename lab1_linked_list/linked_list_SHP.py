'''
<Lab 3: Linked List>
This program has three functions as listed below.
1. Add students. The total enrollment should not exceed MAX_ENROLLMENT(=30).
Duplicate student ID should not be added to the list (you need to print an error message).
Your list should be sorted by student ID.
2. Delete students from the list when the student ID is in the list.
3. Print the student IDs and student names in the list.

Input/ Obtain a list of operations from the given input file, and execute the given operations in order.
A detailed specification of the operations is provided below. Each line represents a single operation.
Each operation and the necessary parameters are separated by a space.

- i  studentID  studentName : insert a new node with the student information.
- d  studentID  studentName : delete the node with the studentID.
- f  studentID : print the student name of the given student ID.
- p : print the entire list from the beginning to the end.
'''


class Node:
    def __init__(self, keydata=None, valuedata=None):
        self.__keydata = keydata
        self.__valuedata = valuedata
        self.__prev = None
        self.__next = None

    @property
    def keydata(self):
        return self.__keydata

    @property
    def valuedata(self):
        return self.__valuedata

    @keydata.setter
    def keydata(self, keydata):
        self.__keydata = keydata

    @valuedata.setter
    def valuedata(self, valuedata):
        self.__valuedata = valuedata

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, p):
        self.__prev = p

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, n):
        self.__next = n


class DoubleLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.d_size = 0

    def empty(self):
        if self.d_size == 0:
            return True
        else:
            return False

    def size(self):
        return self.d_size

    def add_first(self, keydata, valuedata):
        new_node = Node(keydata, valuedata)

        new_node.next = self.head.next
        new_node.prev = self.head

        self.head.next.prev = new_node
        self.head.next = new_node

        self.d_size += 1

    def add_last(self, keydata, valuedata):
        new_node = Node(keydata, valuedata)

        new_node.prev = self.tail.prev
        new_node.next = self.tail

        self.tail.prev.next = new_node
        self.tail.prev = new_node

        self.d_size += 1

    def insert_after(self, keydata, valuedata, node):
        new_node = Node(keydata, valuedata)

        new_node.next = node.next
        new_node.prev = node

        node.next.prev = new_node
        node.next = new_node

        self.d_size += 1

    def insert_before(self, keydata, valuedata, node):
        new_node = Node(keydata, valuedata)

        new_node.prev = node.prev
        new_node.next = node

        node.prev.next = new_node
        node.prev = new_node

        self.d_size += 1

    def search_forward(self, data):             # head에서부터 순차적으로 검색
        node = self.head
        count = 0
        while node:
            if node.keydata == data:
                return node
            count += 1
            node = node.next

    # tail에서부터 순차적으로 검색
    def search_backward(self, data):
        node = self.tail
        count = -1
        while node:
            if node.keydata == data:
                return node
            count += -1
            node = node.prev


    def delete_first(self):
        if self.empty():
            return
        self.head.next = self.head.next.next
        self.head.next.prev = self.head

        self.d_size -= 1

    def delete_last(self):
        if self.empty():
            return
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail

        self.d_size -= 1

    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        self.d_size -= 1

    def append(self, keydata, valuedata):
        new_node = Node(keydata, valuedata)
        if self.d_size == 0:
            self.head = new_node
            self.d_size = 1

        else:
            cur_node = self.head
            prev_node = None

            # cur_node의 data와 node의 data를 비교하며 삽입 위치 파악
            while (cur_node != None and cur_node.keydata <= new_node.keydata):
                prev_node = cur_node
                cur_node = cur_node.next

            # node의 next를 cur_node로 설정
            new_node.next = cur_node

            # cur_node가 마지막 노드가 아닌 경우 prev를 node로 설정
            if not (cur_node == None):
                cur_node.prev = new_node

            # node의 data가 가장 작아 head에 삽입되어야 하는 경우 node를 head로 설정
            if (prev_node == None):
                self.head = new_node
            # node가 리스트 중간에 삽입되어야 하는 경우 prev_node의 next를 node로 설정
            # node의 prev도 prev_node로 설정
            else:
                prev_node.next = new_node
                new_node.prev = prev_node
            self.d_size += 1

    def print_all(self):
        if self.d_size == 0:
            print('')
        else:
            tmp_node = self.head
            while (tmp_node != None):
                print(tmp_node.keydata, '', tmp_node.valuedata, end="  ")
                tmp_node = tmp_node.next
            print()


def read_file(file):
    f = open(file, 'r', encoding='UTF-8')
    content = f.readlines()
    return content


if __name__=="__main__":
    dlist = DoubleLinkedList()
    file = 'lab3_input.txt'
    documents = read_file(file)
    while dlist.size() < 30:
        for oper, line in enumerate(documents):
            line = line.strip()
            if len(line) != 1:
                line = line.split(maxsplit=2)
                keydata = line[1]

                if line[0] == 'i':
                    target = dlist.search_forward(keydata)
                    valuedata = line[2]
                    if target:
                        print(f"There already is an element with key {keydata}. Insertion failed.")
                    else:
                    # if keydata < dlist.
                    # dlist.add_first(keydata, valuedata)
                        dlist.append(keydata, valuedata)
                        print(f"Insertion Success : {keydata}")
                    # sorted(dlist, key=lambda key: keydata)

                elif line[0] == 'd':
                    target = dlist.search_forward(keydata)
                    if target:
                        dlist.delete_node(target)
                        print(f"Deletion Success : {keydata}")

                    else:
                        print(f"Deletion failed : element {keydata} is not in the list")

                elif line[0] == 'f':
                    target = dlist.search_forward(keydata)
                    if target:
                        name = target.valuedata
                        print(f"Searching Success : {name}")
                    else:
                        print(f"Searching Failed : element {keydata} is not in the list")

                print(f'Current List>', end="")
                dlist.print_all()

            if line[0] == 'p':
                dlist.print_all()

        break
