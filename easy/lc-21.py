"""
<<<<<<< HEAD
merge two sorted lists

merge two sorted linked lits and return it as a new sorted list. 
new lis should be made by spilcing together the nodes of the first two lists
"""

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class Sol:
    def merge(self, x: ListNode, y: ListNode) -> ListNode:
        
        if x[0] > y[0]:
            temp = x
            x = y
            y = temp 
        
        print(f"{x=}, {y=}")
        
        return None
    
    
x = [2, 2, 4]   
y = [1, 3, 4]

z = Sol().merge(x, y)
print(z)

=======
Merge two sorted lists

merge two sorted linked lists nd return is aas a nwe sorted list.
the new list should be made by spliicing together the nodes of the first two lists


x = [1,2,4]
y = [1,3,4]


"""
>>>>>>> 91b24299c70f659fff267d6a523a35213cc147ea
