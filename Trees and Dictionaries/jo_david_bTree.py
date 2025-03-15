# David Jo. Assignment 5 "Trees and Dictionaries" Part 1
# Program prupose: To implement a binary tree data structure as shown in his week's lectures
def tree(label, branches=[]):
    return [label] + branches

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

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



if __name__ == "__main__":
    main()