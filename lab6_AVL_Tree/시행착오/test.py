# class TreeNode:
#     def __init__(self, val, left=None, right=None, height=0):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.height = height  # 높이를 뜻하는 height 속성 추가 기본값=1
#
#
# class AVLtree:
#     def __init__(self, val):
#         self.root = TreeNode(val)
#
#     def insert(self, val):
#         self.root = self._insert_node(self.root, val)
#
#     def delete(self, val):
#         self.root = self._delete_node(self.root, val)
#
#     def _insert_node(self, cur, val):
#         if not cur:
#             return TreeNode(val)
#         elif val < cur.val:
#             cur.left = self._insert_node(cur.left, val)
#         elif val > cur.val:
#             cur.right = self._insert_node(cur.right, val)
#
#         cur.height = 1 + max(self._get_height(cur.left),
#                              self._get_height(cur.right))
#
#         balance = self._get_balance(cur)
#         if balance > 1 and val > cur.left.val:  # Left-Right case
#             cur.left = self._left_rotate(cur.left)
#             cur = self._right_rotate(cur)
#
#         elif balance > 1 and val < cur.left.val:  # Left-Left case
#             cur = self._right_rotate(cur)
#
#         elif balance < -1 and val > cur.right.val:  # Right-Right case
#             cur = self._left_rotate(cur)
#
#         elif balance < -1 and val < cur.right.val:  # Right-Left case
#             cur.right = self._right_rotate(cur.right)
#             cur = self._left_rotate(cur)
#         return cur
#
#     def _delete_node(self, cur, val):
#         if not cur:
#             return False
#         elif cur == self.root and cur.val == val:
#             if cur.left and cur.right:
#                 pre_val = self._find_predecessor(cur.left)
#                 self._delete_node(cur, pre_val)
#                 cur.val = pre_val
#             elif cur.left or cur.right:
#                 if cur.left:
#                     self.root = cur.left
#                 elif cur.right:
#                     self.root = cur.right
#             else:
#                 self.root = None
#
#         elif cur.left and cur.left.val == val:
#             if cur.left.left and cur.left.right:
#                 pre_val = self._find_predecessor(cur.left.left)
#                 self._delete_node(cur, pre_val)
#                 cur.left.val = pre_val
#                 cur.left.height = 1 + \
#                                   max(self._get_height(cur.left.left),
#                                       self._get_height(cur.left.right))
#             elif cur.left.left or cur.left.right:
#                 if cur.left.left:
#                     cur.left = cur.left.left
#                 elif cur.left.right:
#                     cur.left = cur.left.right
#                 cur.left.height = 1 + \
#                                   max(self._get_height(cur.left.left),
#                                       self._get_height(cur.left.right))
#             else:
#                 cur.left = None
#             cur.height = 1 + max(self._get_height(cur.left),
#                                  self._get_height(cur.right))
#
#         elif cur.right and cur.right.val == val:
#             if cur.right.left and cur.right.right:
#                 pre_val = self._find_predecessor(cur.right.left)
#                 self._delete_node(cur, pre_val)
#                 cur.right.val = pre_val
#                 cur.right.height = 1 + \
#                                    max(self._get_height(cur.right.left),
#                                        self._get_height(cur.right.right))
#             elif cur.right.left or cur.right.right:
#                 if cur.right.left:
#                     cur.right = cur.right.left
#                 elif cur.right.right:
#                     cur.right = cur.right.right
#                 cur.right.height = 1 + \
#                                    max(self._get_height(cur.right.left),
#                                        self._get_height(cur.right.right))
#             else:
#                 cur.right = None
#             cur.height = 1 + max(self._get_height(cur.left),
#                                  self._get_height(cur.right))
#
#         elif cur.val > val:
#             cur.left = self._delete_node(cur.left, val)
#
#         elif cur.val < val:
#             cur.right = self._delete_node(cur.right, val)
#
#         balance = self._get_balance(cur)
#         # Left-Left case
#         if balance > 1 and self._get_balance(cur.left) >= 0:
#             cur = self._right_rotate(cur)
#         # Left-Right case
#         elif balance > 1 and self._get_balance(cur.left) < 0:
#             cur.left = self._left_rotate(cur.left)
#             cur = self._right_rotate(cur)
#         # Right-Left case
#         elif balance < -1 and self._get_balance(cur.right) > 0:
#             cur.right = self._right_rotate(cur.right)
#             cur = self._left_rotate(cur)
#         # Right-Right case
#         elif balance < -1 and self._get_balance(cur.right) <= 0:
#             cur = self._left_rotate(cur)
#         return cur
#
#     def _find_predecessor(self, cur):
#         if cur.right:
#             return self._find_predecessor(cur.right)
#         else:
#             return cur.val
#
#     def _left_rotate(self, cur):
#         v = cur
#         w = cur.right
#         t = w.left
#         cur = w
#         w.left = v
#         v.right = t
#         v.height = 1 + max(self._get_height(v.left), self._get_height(v.right))
#         w.height = 1 + max(self._get_height(w.left), self._get_height(w.right))
#         return cur
#
#     def _right_rotate(self, cur):
#         v = cur
#         w = cur.left
#         t2 = w.right
#         cur = w
#         w.right = v
#         v.left = t2
#         v.height = 1 + max(self._get_height(v.left), self._get_height(v.right))
#         w.height = 1 + max(self._get_height(w.left), self._get_height(w.right))
#         return cur
#
#     def _get_height(self, cur):
#         if not cur:
#             return 0
#         return cur.height
#
#     def _get_balance(self, cur):
#         if not cur:
#             return 0
#         return self._get_height(cur.left) - self._get_height(cur.right)
#
#     def traverse(self):
#         return self._print(self.root, [])
#
#     def _print(self, cur, result):
#         if cur:
#             self._print(cur.left, result)
#             result.append(cur.val)
#             self._print(cur.right, result)
#         return result
#
#
# def read_file(file):
#     f = open(file, 'r', encoding='UTF-8')
#     content = f.readlines()
#     return content
#
#
# if __name__ == "__main__":
#     file = 'input8.txt'
#     documents = read_file(file)
#     documents = str(documents[0])
#     num = documents.split()
#     # print(num)
#     AVLT = AVL()

# Generic tree node class
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


# AVL tree class which supports the
# Insert operation
class AVL_Tree(object):

    # Recursive function to insert key in
    # subtree rooted with node and returns
    # new root of subtree.
    def insert(self, root, key):

        # Step 1 - Perform normal BST
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Step 3 - Get the balance factor
        balance = self.getBalance(root)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)

        # Case 2 - Right Right
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)

        # Case 3 - Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Case 4 - Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):

        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        # Return the new root
        return y

    def rightRotate(self, z):

        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        # Return the new root
        return y

    def getHeight(self, root):
        if not root:
            return 0

        return root.height

    def getBalance(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    def preOrder(self, root):

        if not root:
            return

        print("{0} ".format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self, root):

        if not root:
            return

        self.inOrder(root.left)
        print("{0} ".format(root.val), end="")
        self.inOrder(root.right)


def read_file(file):
    f = open(file, 'r', encoding='UTF-8')
    content = f.readlines()
    return content


if __name__ == "__main__":
    file = 'input8.txt'
    documents = read_file(file)
    documents = str(documents[0])
    num = documents.split()
    # print(num)
    AVLT = AVL_Tree()
    root = None

    for oper, line in enumerate(num):
        root = AVLT.insert(root, int(line))
        print(f"height : {AVLT.getHeight(root)}")
        AVLT.inOrder(root)
        print()

