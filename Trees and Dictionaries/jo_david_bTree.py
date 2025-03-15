# David Jo. Assignment 5 "Trees and Dictionaries" Part 1
# Program prupose: To implement a binary tree data structure as shown in his week's lectures
def tree(label, branches=[]):
    return [label] + branches

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

def num_leaves(tree):
    if is_leaf(tree):
        return 1
    return sum([num_leaves(branch) for branch in branches(tree)])

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def print_tree(t, indent=0):
    print(' ' * indent + str(label(t)))
    for branch in branches(t):
        print_tree(branch, indent+1)

def main():
    the_tree = tree(4, [tree(2, [tree(1), tree(3)]), tree(6, [tree(5)])])
    print_tree(the_tree)
    print(f"Tree label: {label(the_tree)}")
    print(f"The branches: {branches(the_tree)}")
    print(f"The number of leaves: {num_leaves(the_tree)}")


if __name__ == "__main__":
    main()