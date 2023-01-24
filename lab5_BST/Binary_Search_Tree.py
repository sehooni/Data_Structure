'''<Lab 7: Binary Search Tree>
we will implement binary search tree ADT with the three main functions, insert, delete, and find.
Additionally, we will have three print functions with different ways of traversal.

•	Input
Obtain a list of operations from the given input file, and execute the given operations in order.
A detailed specification of the operations is provided below. Each line represents a single operation.
Each operation and the necessary parameters are separated by a space.
You may assume that the input values (represented as x below) are any integer.

•	i  x: insert a new key “x” into the binary search tree without duplication.
        If x already exists in the tree, print an error message.
•	d  x: delete a key “x” in the binary search tree.
        If x does not exist in the tree, print an error message.
•	f  x: find the given key to check whether the key exists in the tree.
•	pi: print the tree by inorder traversal
•	pr: print the tree by preorder traversal
•	po: print the tree by postorder traversal
'''


class TreeNode:
    def __init__(self, key):
        self.__key=key
        self.__left=None
        self.__right=None
        self.__parent=None

    def __del__(self):
        return
        # print('key {} is deleted'.format(self.__key))
        # print(f'key {self.__key} is deleted')

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key):
        self.__key = key

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left=left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, p):
        self.__parent = p


class BST:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def preorder_traverse(self, cur, func):
        if not cur:
            return

        func(cur)
        self.preorder_traverse(cur.left, func)
        self.preorder_traverse(cur.right, func)

    # key가 정렬된 상태로 출력
    def inorder_traverse(self, cur, func):
        if not cur:
            return

        self.inorder_traverse(cur.left, func)
        func(cur)
        self.inorder_traverse(cur.right, func)

    def postorder_traverse(self, cur, func):
        if not cur:
            return
        self.postorder_traverse(cur.left, func)
        self.postorder_traverse(cur.right, func)
        func(cur)

    # 편의 함수
    # cur의 왼쪽 자식을 left로 만든다.
    def __make_left(self, cur, left):
        cur.left = left
        if left:
            left.parent = cur

    # 편의 함수
    # cur의 오른쪽 자식을 right로 만든다.
    def __make_right(self, cur, right):
        cur.right = right
        if right:
            right.parent = cur

    def insert(self, key):
        new_node = TreeNode(key)

        cur = self.root
        if not cur:
            self.root = new_node
            return

        while True:
            parent = cur
            if key < cur.key:
                cur = cur.left
                if not cur:
                    self.__make_left(parent, new_node)
                    return
            else:
                cur = cur.right
                if not cur:
                    self.__make_right(parent, new_node)
                    return

    def search(self, target):
        cur = self.root
        while cur:
            if cur.key == target:
                return cur
            elif cur.key > target:
                cur = cur.left
            elif cur.key < target:
                cur = cur.right
        return cur

    def __delete_recursion(self, cur, target):
        if not cur:
            return None
        elif target < cur.key:
            new_left = self.__delete_recursion(cur.left, target)
            self.__make_left(cur, new_left)
        elif target > cur.key:
            new_right = self.__delete_recursion(cur.right, target)
            self.__make_right(cur, new_right)
        else:
            if not cur.left and not cur.right:
                cur = None
            elif not cur.right:
                cur = cur.left
            elif not cur.left:
                cur = cur.right
            else:
                replace = cur.left
                replace = self.max(replace)
                cur.key, replace.key = replace.key, cur.key
                new_left = self.__delete_recursion(cur.left, replace.key)
                self.__make_left(cur, new_left)
        return cur

    def delete(self, target):
        new_root = self.__delete_recursion(self.root, target)
        self.root = new_root

    def min(self, cur):
        while cur.left != None:
            cur = cur.left
        return cur

    def max(self, cur):
        while cur.right != None:
            cur = cur.right
        return cur

    def prev(self, cur):
        # 왼쪽 자식이 있다면
        # 왼쪽 자식에서 가장 큰 노드
        if cur.left:
            return self.max(cur.left)

        # 부모 노드를 받아온다
        parent = cur.parent
        # 현재 노드가 부모 노드의 왼쪽 자식이면
        while parent and cur == parent.left:
            cur = parent
            parent = parent.parent

        return parent

    def next(self, cur):
        # 오른쪽 자식이 있다면
        # 오른쪽 자식에서 가장 작은 노드
        if cur.right:
            return self.min(cur.right)

        # 부모 노드를 받아온다
        parent = cur.parent
        # 현재 노드가 부모 노드의 오른쪽 자식이면
        # 루트에 도달하거나
        # 현재 노드가 부모 노드의 왼쪽 자식이 될 때까지
        # 계속 부모 노드로 이동
        while parent and cur == parent.right:
            cur = parent
            parent = parent.parent

        return parent


def read_file(file):
    f = open(file, 'r', encoding='UTF-8')
    content = f.readlines()
    return content


if __name__ == "__main__":
    file = 'input.txt'
    documents = read_file(file)

    bst = BST()

    for oper, line in enumerate(documents):
        line = line.strip()
        line = line.split(maxsplit=1)
        oper_key = line[0]
        if len(line) == 2:
            keydata = line[1]
            keydata = int(keydata)
            if oper_key == 'i':
                searched_node = bst.search(keydata)
                if searched_node:
                    print(f"Element {keydata} already exists")
                else:
                    bst.insert(keydata)

            elif oper_key == 'd':
                searched_node = bst.search(keydata)
                if searched_node:
                    bst.delete(keydata)
                else:
                    print(f"Element {keydata} not found")

            elif oper_key == 'f':
                searched_node = bst.search(keydata)
                if searched_node:
                    print(f"{keydata} is in the tree")
                else:
                    print(f"{keydata} is not in the tree")

        elif len(line) == 1:
            if line[0] == 'pi':
                f = lambda x: print(x.key, end=' ')
                bst.inorder_traverse(bst.get_root(), f)
                print()

            elif line[0] == 'pr':
                f = lambda x: print(x.key, end=' ')
                bst.preorder_traverse(bst.get_root(), f)
                print()
            elif line[0] == 'po':
                f = lambda x: print(x.key, end=' ')
                bst.postorder_traverse(bst.get_root(), f)
                print()