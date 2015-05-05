'''Contains the Tape class for the Turing Machine Simulator.

Author:
    Robert Merkel <robert.merkel@monash.edu>
'''

from collections import deque

class Tape:
    '''Implements a Turing machine tape.  Tape is infinite in both directions.
'''
    def __init__(self, initstring, blankchar):
        '''Make a new tape.

        Args:

            initstring (str): the initial contents of the tape
            blankchar (str): the blank symbol
        '''
        self.tape=deque(initstring)
        self.pos=0
        self.blankchar = blankchar
        
    def getsym(self):
        '''Get the symbol currently under the tape head.


        Returns:
            str: the symbol under the tape
        '''
        return self.tape[self.pos]
    
    def writeleft(self, newchar):
        '''Write a new symbol at the current tape position and move left

        Args:
            newchar (str): the symbol to be written
        '''
        self.tape[self.pos] = newchar
        if (self.pos == 0):
            self.tape.appendleft(self.blankchar)
        else:
            self.pos -= 1

    def writeright(self, newchar):
        '''Write a new symbol at the current tape position and move right

        Args:
            newchar (str): symbol to be written
        '''
        self.tape[self.pos] = newchar
        self.pos += 1
        if self.pos == len(self.tape):
            self.tape.append(self.blankchar)
        

    def gettape(self):
        '''get a string representation of the tape contents and position

        Returns:
            str: contents of the tape
        '''
        charlist=[]
        for i in range(0, len(self.tape)):
            if i==self.pos:
                charlist.append("*")
                charlist.append(self.tape[i])
                charlist.append("*")
            else:
                charlist.append(self.tape[i])
        return ''.join(charlist)
