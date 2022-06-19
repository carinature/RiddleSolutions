# class Node:
#     def __init__(self, val=None, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#


# BFS
def iterative(root, val: str) -> bool:
    st = [root]
    while st:
        node = st.pop()
        if node:
            if val == node.val:
                return True
            st += [node.left, node.right]
    return False


# DFS
def recursive(root, val: str) -> bool:
    if not root:
        return False
    if root.val == val:
        return True
    return recursive(root.left, val) or recursive(root.right, val)

# if __name__ == '__main__':
#     a = Node('a')
#     b = Node('b')
#     c = Node('c')
#     d = Node('d')
#     e = Node('e')
#     f = Node('f')
#
#     a.left = b
#     a.right = c
#     b.left = d
#     b.right = e
#     c.right = f
#
#     #      a
#     #    /  \
#     #   b    c
#     #  / \    \
#     # d   e    f
#
#     dfs(a)
