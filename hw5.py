"""
Class for linked list node.
"""
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

"""
Will print the linked list for you.
Input:
	head - the head of the linked list.
"""
def print_list(head):
    while head:
        print(str(head.data) + "->")
        head = head.next_node



"""
The input and output examples that are provided in this homework will be drawn as follows:
Example: a -> b -> c
This means that the node who's data is 'a' has a next_node whose data is 'b'. And so forth.
Note, that the 'head' input for the following problems is of type 'Node'.


Hint: multiple nodes can hold the same data. So, be careful when comparing nodes.
"""



"""
Given the head of a linked list, insert the data at the given position
Note: The head is at position 0.

If the insertion index is not valid (too large or too small) simply return the original head.
Input:
    head - the head of the linked list.
    data - the item to add to the head of the linked list.
    position - position to insert

Output:
    Return the head of the resulting linked list

Example:
    Input:
    	a -> c -> d -> e, 'b', 1
    Output:
    	a -> b -> c -> d -> e

Example 2:
	Input:
		b -> c -> d -> e, 'a', 0
	Output:
		a -> b -> c -> d -> e
head is the refernce to the first node, data & position of the node to actually insert
"""

def add_position(head, data, position):
    # i think this is what the edge case is....
    if (head == None and position == 0):
        return Node(data, position)
    
    ##edges case test
    current = head
    previous = None
    found = False
    countPosition = 0 
    while not found:
        if (current != None):
            if (countPosition == position):
                new_node = Node(data)
                if head.next_node == None: 
                    new_node.next_node = None
                elif (previous != None):
                    new_node.next_node = previous.next_node
                    previous.next_node  = new_node
                else:
                    new_node.next_node = head
                    head = new_node
                found = True
            else:
                previous = current
                current = current.next_node
                countPosition += 1;
        else:
            #rip there is no solution
            break
    return head

"""
Given the head of a linked list and a position, remove the node at the given position.
Note: the head is at position 0.

If the remove index is invalid (too small or too large) simply return the head of the orignal linked list.

Input:
	head - the head of the linked list.
	position - the position to remove
Output:
	the head of the resulting linked list

Example:
	Input:
		a -> b -> c -> d -> e, 2
	Output:
		a -> b -> d -> e
"""
def remove_position(head, position):
    if head == None:
        return head
    if position == 0:
        head.next_node
        
    count = 0
    store = head
        
    
    
    
    while store.next_node is not None:
        count += 1
        store = store.next_node
        
    if position > count:
        return head
    
    
    
    
    temp = head
    if position == 0:
        return temp.next_node





    while position - 1 > 0:
        head = head.next_node
        position -= 1
    head.next_node = head.next_node.next_node
    return temp


"""
Given the head of two linked lists, returns the data at the merge point.
Returns None if they do not merge.
Input:
	head_a: head of the first linked list
	head_b: head of the second linked list
output:
	the data of the merge node
Example:
Input:
	a -> b -> c -> d, f -> c -> d
Output:
	'c'

Example 2:
Input:
	a -> b -> c -> d, e -> f -> g
Output:
	None
"""
def find_merge_point(head_a, head_b):
    #need O(n) non recursive complexity to pass.... i dont know how that possible unless 
    #the merging nodes have to be in the exact same index for both linked lists
    first = head_a
    
    while first is not None:
        second = head_b
        while second is not None:
            if first == second:
                    return first.data
                
            second = second.next_node 
            
        first = first.next_node

"""
Given the head of a linked list, determines whether or not there
is a cycle in the linked list.

Input:
    head - the head of the linked list.

Output:
    (bool) whether or not there is a cycle in the linked list.
Example:
	Input:
		a -> b -> c -> d -> e -> f -> g -> b (And so forth)
	Output:
		TRUE
"""
def find_cycle(head):
    try:
        one = head
        two = head.next_node
        while one is not two:
            one = one.next_node
            two = two.next_node.next_node
        if (one is two):
            return True
    except:
        return False
"""
Given the head of a linked list, reverse the linked list.

Input:
	head - The head of the linked list
Output:
	The head of the new linked list

Example:
	Input:
		a -> b -> c -> d -> e
	Output:
		e -> d -> c -> b -> a
"""
def reverse_list(head):
    previous = None
    current = head 
    while(current is not None): 
        next = current.next_node
        current.next_node = previous 
        previous = current 
        current = next
        head = previous
        
    return head

"""
Given the head of two sorted linked lists, merge them to form 1 sorted linked list.

Input:
	head_a - head of the first linked list
	head_b - the head of the second linked list
Output:
	the head of the merged sorted linked list

Example:
	Input:
		1 -> 3 -> 5 -> 7
		2 -> 4 -> 6 -> 8
	Output:
		1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
"""
def merge_lists(head_a, head_b):
    new = Node(0)
    current = new
    
    while head_a and head_b:
        if head_a.data < head_b.data:
            current.next_node = head_a
            head_a = head_a.next_node
            
        else:
            current.next_node = head_b
            head_b = head_b.next_node
            
        current = current.next_node
        
    current.next_node = head_a or head_b 
    return new.next_node
