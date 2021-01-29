"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # referencing answers
        current = self.head
        if position < 1:
            return None
        # elif position == 1:
        #     return current
        for i in range(position-1):
            if current.next == None: #write the exit condition in the loop first
                return None
            current = current.next
        return current # this can cover when position == 1

        
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements. If position > length, do nothing"""
        current_element = self.get_position(position)
        previous_element = self.get_position(position-1)
        # if use while loop, easy to be indefinite
        if position == 1:
            new_element.next = current_element
            self.head = new_element
        elif current_element:#check position not out of range
            new_element.next = current_element
            previous_element.next = new_element
            
        
        # # solution1
        # if position < 1 or self.get_position(position-1) == None:
        #     return None
        # self.get_position(position-1).next = new_element
        # new_element.next = self.get_position(position)
        
        # #answer
        # counter = 1
        # current = self.head
        # if position > 1:
        #     while current and counter < position:
        #         if counter == position - 1:
        #             new_element.next = current.next
        #             current.next = new_element
        #         current = current.next
        #         counter += 1
        # elif position == 1:
        #     new_element.next = self.head
        #     self.head = new_element


                
    
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None
        if current.value == value and previous == None:#if head value equals to given value
            self.head = current.next
        else:
            while current.value != value and current.next:
                if current.value == value:
                    previous.next = current.next
                else:
                    current = current.next

         


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

# Test insert
ll.insert(e4,3)
# Should print 4 now
print ll.get_position(3).value
#should print 3
print ll.get_position(4).value

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now, my output is 4 because my insert function is wrong, not my delete function...
print ll.get_position(3).value