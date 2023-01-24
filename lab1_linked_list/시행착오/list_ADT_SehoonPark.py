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
class Node(object):
    def __init__(self, key=None, value=None, pointer=None):
        self.key = key          # 데이터 (key)
        self.value = value      # 데이터 (value)
        self.pointer = pointer  # 뒤쪽 포인터

class Linked_List(object):
    def __init__(self):
        self.head = None        # 머리 노드
        self.current = None     # 주목 노드
        self.length = 0         # 노드의 개수

    def __len__(self) -> int:
        """연결 리스트의 노드 개수를 반환"""
        return self.length

    def find(self, key) -> int:
        """데이터(key)와 값이 같은 노드를 검색"""
        cnt = 0
        ptr = self.head
        while ptr is not None:
            if ptr.key == key:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1

    def __contains__(self, key) -> bool:
        """연결 리스트에 key가 포함되어 있는지 확인"""
        return self.find(key) >= 0

    def add_first(self, key, value) -> None:
        """맨 앞에 노드를 삽입"""
        ptr = self.head                 # 삽입하기 전의 머리 노드
        self.head = self.current = Node(key, value, ptr)
        self.length += 1

    def add_last(self, key, value):
        """맨 끝에 노드를 삽입"""
        if self.head is None:           # 리스트가 비어 있으면
            self.add_first(key, value)  # 맨 앞에 노드를 삽입
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = self.current = Node(key, value, None)
            self.length += 1



        # if self.isEmpty():
        #     print("List is empty")
        #     return
        # target_node = self.head
        # while target_node != Node:
        #     if target_node.value == key:
        #         print(f"There already in an element with key {key}. Insertion failed")
        #         break
        #     target_node = target_node.next
        # else:
        #     print(f"The key {key} doesn't exist in the list")


    def isEmpty(self):
        return not bool(self.head)

    # def add_last(self, key, value):
    #     if not self.isEmpty():
    #         node = self.head
    #         while node.pointer:
    #             node = node.pointer
    #         node.pointer = (Node(key))
    #         print(f'Insertion Success : {key} {value}')
    #         print(f"Current list>{self}")
    #     else:
    #         self.head = Node(key)
    #         print(f'Insertion Success : {key} {value}')
    #         print(f"Current list>{self}")
    #     self.length += 1

    def insert(self, pos, key, value):

        if not self.isEmpty():
            if pos == 0:
                node = Node(key)
                if not self.isEmpty():
                    node.pointer = self.head
                    self.head = node
                    print(f'Insertion Success : {key} {value}')
                    print(f"Current list>{self}")
                else:
                    self.head = node
                    print(f'Insertion Success : {key} {value}')
                self.length += 1

            elif pos == self.length:
                if not self.isEmpty():
                    node = self.head
                    while node.pointer:
                        node = node.pointer
                    node.pointer = (Node(key))
                    print(f'Insertion Success : {key}')
                else:
                    self.head = Node(key)
                self.length += 1

            else:
                node = self.head
                cnt = 0
                while pos > 0 and pos < self.length:
                    if cnt == pos - 1:
                        new_node = Node(key, node.pointer)
                        node.pointer = new_node
                        break
                    node = node.pointer
                    cnt += 1
                self.length += 1
        else:
            print('list is empty')


    # def delete(self, key):
    #     if not self.isEmpty():
    #         node = self.head
    #         if node.value == key:
    #             self.head = node.pointer
    #             self.length -= 1
    #             return True
    #         else:
    #             prev = node
    #             node = node.pointer
    #             while node:
    #                 if node.value == key:
    #                     prev.pointer = node.pointer
    #                     node = None
    #                     self.length -= 1
    #                     return True
    #                 prev = node
    #                 node = node.pointer
    #             return False
    #     else:
    #         print('list is empty')
    #         return False
    def remove_first(self) -> None:
        """머리 노드를 삭제"""
        if self.head is not None:   # 리스트가 비어 있지 않다면
             self.head = self.current = self.head.next
        self.length -= 1

    def remove_last(self):

    def delete(self, p:Node) -> None:
        """노드 p 삭제"""
        if self.head is not None:
            if p is self.head:          # p가 머리 노드이면
                self.remove
    def PositionFind(self, pos):
        if not self.isEmpty():
            cnt = 0
            node = self.head
            while node:
                if cnt == pos:
                    return node.value
                node = node.pointer
                cnt += 1
            return False
        else:
            print('list is empty')
            return False
    # def DeleteList(self):

    def isLast(self, pos):
        if self.length < 30:


    # #------------------------ Node class ------------------------
    # class _Node:
    #     __slots__ = '_element', '_next'     # streamline memory usage
    #
    #     def __init__(self, element, next):  # initialize node's fields
    #         self._element = element         # reference to user's element
    #         self._next = next               # reference to next node
    # # ------------------------ stack methods ------------------------
def main(file):
    for i in range(len(file[:,0])):
        if file[i,0] == 'p':
            break
        elif file[i,0] == 'i':
            print('Insertion Success : {}'.format(file[i,1]))
            List_ADT.append(file[i,1:])

            print('Current List >{}'.format(List_ADT))
        elif file[i,0] == 'd':
            print('Deletion Success : {}'.format(file[i,i]))
            if file[i,0] in List_ADT:
                List_ADT.remove(file[i,1:])

    print(List_ADT)



