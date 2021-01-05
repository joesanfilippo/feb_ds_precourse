'''
This exercise is to implement a stack class in Python. Generally, if you need
to use a Stack in Python, you can just use a list with the .append() and .pop()
methods. Also, you can len() to find the length and lst[-1] for the .peek()
method.

This however, does not provide much insight into how a stack is implemented
under the hood.

In the class you're defining, do not use any of these methods (except what was
mentioned for peek()), and instead write your own. You'll have to use lists to
implement the stack, but each method needs to be implemented from scratch.

HINT: You'll need to instantiate "empty lists" of the appropriate length,
and then "fill" the lists with the values from the original list.
'''

class Stack():
    def __init__(self, lst):
        '''
        Constructor method

        Attributes
        ----------
        stack : []
            A list, representing a stack of objects

        length : int
            An integer representing the number of objects in the stack

        Parameters
        ----------
        lst : []
            The list that is to be converted to a stack
        '''
        self.stack = lst
        
        counter = 0 
        for i in lst:
            counter += 1
        
        self.length = counter

    def __len__(self):
        '''
        Returns the number of objects in the stack, when len() is invoked

        Parameters
        ----------
        self : Stack
            The stack whose length is being returned

        Returns
        -------
        length : int
            An integer representing the number of objects in the stack
        '''
        counter = 0
        for i in lst:
            counter += 1
        return counter
        

    def push(self, obj):
        '''
        Adds a new object to the top of the stack.

        Parameters
        ----------
        self : Stack
            The stack which the object is being added to

        obj : Any
            The object being added to the top of the stack
        '''
        self.stack = self.stack + obj.stack
        

    def peek(self):
        '''
        This method returns the object at the top of the stack, but DOES NOT
        REMOVE IT

        Parameters
        ----------
        self : Stack
            The stack you are peeking the top item from

        Returns
        -------
        obj : Any
            The object from the top of the stack
        '''
        return self.stack[-1]

    def pop(self):
        '''
        Removes the object at the top of the stack and returns it

        Parameters
        ----------
        self : Stack
            The stack you are removing the object from

        Returns
        -------
        obj : Any
            The object being returned from the top of the stack
        '''
        pop_item = self.stack[-1]
        del self.stack[-1]
        return pop_item

    def empty(self):
        '''
        This method empties the stack.

        Parameters
        ----------
        self : Stack
            The stack which is to be cleared

        Returns
        -------
        stack : Stack
            An empty stack
        '''
        self.stack = []
        return self.stack