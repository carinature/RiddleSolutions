# class Node:
#     def __init__(self, val=None, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def iterative(root):
    res = []
    st = [root]
    while st:
        node = st.pop(0)
        if node:
            res.append(node.val)
            st.append(node.left)
            st.append(node.right)
    return res


def recursive(root):
    pass
    return ('please read the following answer re recursive BFS:\t'
            'https://stackoverflow.com/a/2550084')

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
#   #
#   #        a
#   #       / \
#   #      b   c
#   #     / \   \
#   #    d   e   f
#   #
#
#     dfs(a)
