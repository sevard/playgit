# // Create a new node, with val as its contained value and next as
# // the value of the next pointer
# function make-node(v, node next): node
#   let result := new node {v, next}
#   return result
# end
def make_node(val, node_next):
    result = {val: node_next}
    return result


# // Returns the value contained in node n
# function get-value(node n): element
#   return n.value
# end
def get_value(node): # element
    return next(iter(node))


# // Returns the value of node n's next pointer
# function get-next(node n): node
#   return n.next
# end
def get_next(node): # node
    next_node = node.get(next(iter(node)))
    return next_node


# Sets the contained value of n to be v
# function set-value(node n, v)
#   n.value := v
# end
def set_value(node, val):
    key = next(iter(node))
    node_next = node.get(key)
    del node[key]
    node[val] = node_next


# Sets the value of node n's next pointer to be new-next
# function set-next(node n, new-next)
#   n.next := new-next
#   return new-next
# end
def set_next(node, new_next):
    key = next(iter(node))
    node[key] = new_next


node_one = make_node(1, 'a')
print("Node { v: next }: ", node_one)

val_node_one = get_value(node_one)
print("Node value: ", val_node_one)

# Returns the value of node n's next pointer
next_node_val = get_next(node_one)
print("Next node pointer: ", next_node_val)

# Sets the contained value of n to be v
set_value(node_one, 2)
print("New Node val  { v: next }: ", node_one)

# Sets the value of node n's next pointer to be new-next
set_next(node_one, 'b')
print("New Node next { v: next }: ", node_one)