cdef class Node:
    cdef int val
    cdef Node left
    cdef Node right

    def __init__(self, int key):
        self.val = key
        self.left = None
        self.right = None

cpdef Node insert(Node root, int key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

cpdef int search(Node root, int key):
    if root is None:
        return 0
    if root.val == key:
        return 1
    elif key < root.val:
        return search(root.left, key)
    else:
        return search(root.right, key)
