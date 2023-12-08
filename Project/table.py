# A binary search based dictionary imlementation 
# only using list of length 4.

# Each node is a list of length four where positions
# 0 = key, 1 = value, 2 = left-child, 3 = right-child


# Creates and returns the root to a new empty table.
# The complete function is given and should not be changed.
def new_empty_root():
    return [None,None,None,None]

# Add a new key-value pair to table if the key doean't already exist.
# Update value if already key exists in the table.
def add(root,key,value):
    if root[0] == None: #if like this [None,None,None,None], then add the value to 0 and 1
        root[0] = key
        root[1] = value
    elif root[0] != None: # if 0 is not None, then check key if is same
        if root[0] == key: # update the key's value if key is same
            root[1] = value
        elif root[0] != key: # if not same, then choose to add to 2 or 3
            if key < root[0]: # key is smaller than 0 , left-child
                if root[2] == None: # if None then use it
                    root[2] = new_empty_root() # by creating a new empty list
                    add(root[2],key,value)
                elif root[2] != None: # if not None then 
                    add(root[2],key,value) # using recursion to create a new one
            elif key > root[0]:
                if root[3] == None:
                    root[3] = new_empty_root()
                    add(root[3],key,value)
                elif root[3] != None:
                    add(root[3],key,value)

# Returns a string representation of the table content.
# That is, all key-value pairs
def to_string(node):
    pair=get_all_pairs(node)
    lst = "{"
    for p in pair:
        lst = lst + "(" + str(p[0]) + "," + str(p[1]) + ")"
    return  lst + "}"

# Returns the value for the given key. Returns None if key doesn't exists.
def get(node,key):
    
    if key == node[0]:
        return node[1]
    else:
        if key < node[0]:
            if node[2] != None:
                return get(node[2],key)
        elif key > node[0]:
            if node[3] != None:
                return get(node[3],key)
    return None


# Returns the maximum depth (an integer) of the tree.
# That is, the length of longest root-to-leaf path.
def max_depth(node):        #The longest path between the node and the leaf
    if node != None :    
        left = max_depth(node[2]) 
        right = max_depth(node[3]) 
        return max (left,right) + 1
    else:
        return 0

# Returns the number og key-value pairs currently stored in the table
def count(node):
    if node != None:
        left = count(node[2])
        right = count(node[3])
        return left + right + 1                # +1 for root itself
    else:
        return 0
    

# Returns a list of all key-value pairs as tuples 
# sorted as left-to-right, in-order
def get_all_pairs(root):
    # return if the current node is empty
    if root is None:
        return []
    else:
        left = get_all_pairs(root[2])
        right = get_all_pairs(root[3])
        return  left + [(root[0],root[1])] + right

