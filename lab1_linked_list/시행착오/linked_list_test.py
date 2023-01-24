# from linked_list import LinkedList
#
# operation = ['i', 'd', 'f', 'p']
#
# def operation_menu(oper) -> operation:
#     s = [f'{m.name}'for m in operation]
#     while True:
#         n = str(input(oper))
#         if n == s:
#            return operation(n)
#
#
# def read_file(file):
#     f = open(input(file), 'r', encoding='UTF-8')
#     content = f.readlines()
#     return content
#
# def main(file):
#
#
#         # for i in range(len(file[:,0])):
#         # if file[i,0] == 'p':
#         #     break
#         # elif file[i,0] == 'i':
#         #     print('Insertion Success : {}'.format(file[i,1]))
#         #     List_ADT.append(file[i,1:])
#         #
#         #     print('Current List >{}'.format(List_ADT))
#         # elif file[i,0] == 'd':
#         #     print('Deletion Success : {}'.format(file[i,i]))
#         #     if file[i,0] in List_ADT:
#         #         List_ADT.remove(file[i,1:])
#
#
# if __name__=='__main__':
#     lst = LinkedList  # 연결 리스트 생성
#     file = 'lab3_input.txt'
#     documents = read_file(file)
#
#     while len(lst) < 30:
#         for line in documents:
#             line = line.strip()  # 줄 끝의 줄 바꿈 문자를 제거한다.
#             for i, e in enumerate(line):
#                 paramater = operation_menu(e[i])
#                 if e[i] == paramater.i:
#                     lst.add_first(str(e[1:]))
#                     print(f'Insertion Success : {e[i]}')
#                     print(f"Current List>{lst.print()}")
#                 elif e[i] == paramater.d:
#                     lst.remove_current_node(int(e[1:]))
#                     print()


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

    # def get_next(self):
    #     return self.next
    #
    # def has_next(self):
    #     if self.next is None:
    #         return False
    #     return True
    #
    # def get_data(self):
    #     return self.keydata, self.valuedata


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


    def search_forward(self, target):
        cur = self.head.next

        while cur is not self.tail:
            if cur.keydata == target:
                return cur
            cur = cur.next
        return None

    def search_backward(self, target):
        cur = self.tail.prev
        while cur is not self.head:
            if cur.keydata == target:
                return cur
            cur = cur.prev
        return None

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

    # def show_list(dlist):
    #     cur = dlist.head.next
    #     while cur is not dlist.tail:
    #         print(cur.keydata, ' ', cur.valuedata, end="  ")
    #         cur = cur.next
    #     print()

    # def search_backward(self, target):
    #     cur = self.tail.prev
    #     while cur is not self.head:
    #         if cur.keydata == target:
    #             return cur
    #         cur = cur.prev
    #     return None
