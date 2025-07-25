# DO NOT MODIFY THE NODE CLASS
class Node:
    def __init__(self, value, next=None):
        self.value = value 
        # if next is None, this is the last element in the list
        self.next = next 

def is_palindrome(head):
    values = []
    current = head

    while current is not None: 
        vals.append(current.value)
        current = current.next

    return vals == list(reversed(vals))


# 5->4->2
list_1 = Node(5, Node(4, Node(2)))
assert not is_palindrome(list_1)

# 5->4->5
list_2 = Node(5, Node(4, Node(5)))
assert is_palindrome(list_2)

# a->b->c->c->b->a
list_3 = Node("a", Node("b", Node("c", Node("c", Node("b", Node("a"))))))
assert is_palindrome(list_3)

# a->b->c->E->b->a
list_4 = Node("a", Node("b", Node("c", Node("E", Node("b", Node("a"))))))
assert not is_palindrome(list_4)

# 3->3
list_5 = Node(3, Node(3))
assert is_palindrome(list_5)

# 5 (only one element in list)
list_6 = Node(5)
assert is_palindrome(list_6)

# (empty list)
list_7 = None
assert is_palindrome(list_7)

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
