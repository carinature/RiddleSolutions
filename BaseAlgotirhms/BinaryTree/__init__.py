from BaseAlgotirhms.BinaryTree import DFS, BFS
# from BaseAlgotirhms.BinaryTree.DFS import dfs


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      a
    #    /  \
    #   b    c
    #  / \    \
    # d   e    f

    res = DFS.iterative(a)
    print(f'res: {res}')
    res = DFS.recursive(a)
    print(f'res: {res}')

    res = BFS.iterative(a)
    print(f'res: {res}')
    res = BFS.recursive(a)
    print(f'res: {res}')