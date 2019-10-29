def custom_tree(sym_branches, sym_trunk, sym_bg, tree_height):
    '''(str, str, str, int) -> str
    Precondition: len(sym_branches) > 0 and len(sym_trunk) > 0
                    and len(sym_bg) > 0 and tree_height > 1

    Returns a string representing a tree with sym_branches as symbol for the
    branches, sym_trunk for the trunk, and sym_bg for the background. The
    tree_height will be split as 2/3 for the crown (i.e. branches) and the
    remaining for the trunk.
    '''
    trunk = []
    tree = []
    z = tree_height
    tree_height = int(round((tree_height * 2)/3))
    trunk_height = int(round((z * 1)/3))
    branchess = 0
    x = 1
    lenght = tree_height * 2 - 1
    
    for i in range(tree_height):
        tree.append(((x * sym_branches).center( lenght, sym_bg))+ '\n')
        branchess += 1
        x += 2
        if (branchess == tree_height):
            break
    for j in range(trunk_height):
        trunk.append((sym_trunk.center( lenght, sym_bg)))
    for z in tree:
        branches = ''.join(tree)
    for x in trunk:
        trunkk = '\n'.join(trunk)
    return branches + trunkk
# You can play here
def test_custom_tree():
    print (custom_tree('Z', '@', ' ', 10))
