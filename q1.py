class IntervalTree:

    '''An interval tree.'''
    
    def __init__(self: 'IntervalTree', lst: list) -> None:
        '''Initialize this interval tree.'''
        self._lst = lst
        self._root = build(lst, 0, len(lst) - 1)
  
    def min_in_range(self: 'IntervalTree', start_index: int, end_index: int) -> int:
        '''Return index of minimum from start_index to end_index.'''
        # TODO: implementation needed
        
        current_index = self._root.min_index
        hold = self._root
        
        #print(current_index)
        if start_index == end_index:
            return start_index
        
        if current_index <= end_index and current_index >= start_index:
            return current_index        
        
        
        if self._root.left == None and self._root.right == None:
            return start_index
        #GO LEFT

        
        hold_l = self._root.left
        self._root = hold_l
        left = self.min_in_range(start_index, end_index)
        #left = self.min_in_range(start_index, (start_index + end_index)//2)
        #print(left)
        
    
        self._root = hold

        #GO RIGHT
        hold_r = self._root.right
        self._root = hold_r
        right = self.min_in_range(start_index, end_index)
        #right = self.min_in_range((start_index + end_index)//2 + 1, end_index)


        #RESET tree
        self._root = hold

        if self._lst[left] < self._lst[right]:            
            return left
        else:       
            return right
        
    
    def __repr__(self: 'IntervalTree') -> str:
        '''Return str representation of IntervalTree.'''
        return 'IntervalTree({})'.format(repr(self._root))
    
class IntervalNode:
    '''A node in an interval tree.'''

    def __init__(self: 'IntervalNode', min_index: int, 
                 left: 'IntervalNode' =None, right: 'IntervalNode' =None) -> None:
        '''Initialize this IntervalNode.
        '''
        self.min_index, self.left, self.right = min_index, left, right

    def __repr__(self: 'IntervalNode') -> str:
        '''Return str representation of IntervalNode.'''
        return 'IntervalNode({}, {}, {})'.format(
                repr(self.min_index),
                repr(self.left),
                repr(self.right)
                )


def build(lst, start, end):
    '''(list of int, int, int) -> IntervalNode
  
    Return the root IntervalNode for an interval tree that represents lst[start:end+1].
    '''
    if start == end:
        return IntervalNode(start)
    left = build(lst, start, (start + end) // 2)
    right = build(lst, (start + end) // 2 + 1, end)
    if lst[left.min_index] < lst[right.min_index]:
        smallest = left.min_index
    else:
        smallest = right.min_index
    return IntervalNode(smallest, left, right)
  

if __name__ == '__main__':
    
    tree = IntervalTree([25, 24, 5, 20, 7, 4, 30])
    
    finale = tree.min_in_range(2,4)
    print(finale)