'''<Lab 9: Hashing>
we will implement an open hashing using multiplication method.
Use the function "h(k)= [(m(kA mod 1))]" to calculate the h(k) where “kA mod 1” means the fractional part of kA.
We will implement five main functions, insert, delete, find, print and quit.

1. Input
Obtain a list of operations from the given input file, and execute the given operations in order.
A detailed specification of the operations is provided below.
Execute the given operations in order.
Each line represents a single operation.
Each operation and the necessary parameters are separated by a space.
The first line of the operations in your input file represents the hash table size value and the second line represents the “A”(constant float between 0 and 1) value.
You may assume that the input values (represented as x below) are any integer.
- i x : insert a value “x” to the hash table and print “x” and where you put “x” in the hash table. If the “x” already exist in the hash table, nothing happens.
- d x : delete a value “x” in the hash table and print “x” and where you delete “x” in the hash table. If the “x” doesn’t exist in the hash table, nothing happens.
- f x : find a value “x” in the hash table. Print the hash table index if the “x” exist, else print “null”
- p : print the hash table from index 0 to (hash table size – 1). Print all numbers at index in order. If there is no value at any index, print “null”.
- q : quit the program.
'''


class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashMap:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * self.size

    def hash_value(self, key: int) -> int:
        if isinstance(key, int):
            temp = key * A
            temp = temp - int(temp)
            index = int(self.size * temp)
            return index

    def put(self, key: int, A: float) -> None:
        temp = key * A
        temp = temp - int(temp)
        index = int(self.size * temp)

        if self.hash_table[index] == None:
            self.hash_table[index] = ListNode(key)
        else:
            temp_node = None
            curr_node = self.hash_table[index]
            while True:
                if curr_node.key == key:
                    # curr_node.value = value
                    print("null")
                    return
                if curr_node.next == None: break
                curr_node = curr_node.next
            curr_node.next = ListNode(key)

    def get(self, key: int, A) -> int:
        temp = key * A
        temp = temp - int(temp)
        index = int(self.size * temp)

        curr_node = self.hash_table[index]

        while curr_node:
            if curr_node.key == key:
                return curr_node.key
            else:
                curr_node = curr_node.next

        return -1

    def search(self, key: int) -> int:
        hash = self.hash_value(key)  # 검색하는 키의 해시값
        p = self.hash_table[hash]  # 노드를 노드

        while p is not None:
            if p.key == key:
                return hash  # 검색 성공
            p = p.next  # 뒤쪽 노드를 주목

        # 검색 실패
        return

    def remove(self, key: int, A) -> None:
        temp = key * A
        temp = temp - int(temp)
        index = int(self.size * temp)

        curr_node = prev_node = self.hash_table[index]

        if not curr_node: return

        if curr_node.key == key:
            self.hash_table[index] = curr_node.next
        else:
            curr_node = curr_node.next

            while curr_node:
                if curr_node.key == key:
                    prev_node.next = curr_node.next
                    break
                else:
                    prev_node, curr_node = prev_node.next, curr_node.next

    def dump(self) -> None:
        for i in range(self.size):
            p = self.hash_table[i]
            if p is None:
                print("null", end='')
                print()
            else:
                temp_list = []
                while p is not None:
                    temp_list.append(p.key)
                    p = p.next
                temp_list.reverse()
                for i, p_key in enumerate(temp_list):
                    print(f"{p_key}", end=' ')
                print()

def read_file(file):
    f = open(file, 'r', encoding='UTF-8')
    content = f.readlines()
    return content


if __name__ == "__main__":
    file = 'input9.txt'
    documents = read_file(file)
    list = [line.rstrip() for line in documents]

    size = int(list[0])
    print(f"Hash table size : {size}")
    A = float(list[1])
    print(f"A : {A}")
    hash = MyHashMap(size)
    for oper, line in enumerate(list[2:]):
        line = line.split()
        operation = line[0]
    #
        if len(line) == 2:
            if operation == 'i':
                key = int(line[1])
                found = hash.search(key)
                if found == None:
                    hash.put(key, A)
                    print(f"inserted : {key} in node{hash.search(key)}")
                else:
                    print("null")

            elif operation == 'f':
                key = int(line[1])
                found = hash.search(key)
                if found != None :
                    print(f"found {key} : {found}")
                else:
                    print("null")

            elif operation == 'd':
                key = int(line[1])
                found = hash.search(key)
                if found != None:
                    print(f"deleted: {key} in node{hash.search(key)}")
                    hash.remove(key, A)
                else:
                    print("null")

        elif len(line) == 1:
            if operation == 'p':
                hash.dump()

            elif operation == 'q':
                break
