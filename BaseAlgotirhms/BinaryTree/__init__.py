from BaseAlgotirhms.BinaryTree import DFS, BFS, Search


# from BaseAlgotirhms.BinaryTree.DFS import dfs


class Node:
    def __init__(self, val: str = None, left=None, right=None):
        self.val: str = val
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

    #
    #     a
    #    / \
    #   b   c
    #  / \   \
    # d   e   f
    #

    print(f'DFS.iterative(a): {DFS.iterative(a)}')
    print(f'DFS.recursive(a): {DFS.recursive(a)}')

    print(f'BFS.iterative(a): {BFS.iterative(a)}')
    print(f'BFS.recursive(a): {BFS.recursive(a)}')

    print(f'Search.iterative(a): {Search.iterative(a, "e")}')
    print(f'Search.recursive(a): {Search.recursive(a, "e")}')
    print(f'Search.iterative(a): {Search.iterative(a, "x")}')
    print(f'Search.recursive(a): {Search.recursive(a, "x")}')
