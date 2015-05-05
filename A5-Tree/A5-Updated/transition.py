'''Contains the Transition class for the Turing Machine Simulator.

Author:
    Robert Merkel <robert.merkel@monash.edu>
'''

class Transition:
    '''Represents a transition in a Turing machine'''
    
    def __init__(self, writesym, newstate, direction):
        '''Define a new transition

        Args:
            writesym (str): the symbol to write
            newstate (str): name of the state to transition to
            direction (str): direction to move ("L" or "R")
        '''
        self.writesym = writesym
        self.newstate = newstate
        self.direction = direction

    def get_write_sym(self):
        '''Getter for the symbol to write
        Returns:
            The symbol to write on the tape
        '''
        return self.writesym

    def get_next_state(self):
        '''Get the name of the next state

        Returns:
            The name of the next state
        '''    
        return self.newstate

    def get_next_direction(self):
        '''Get the direction to move

        Returns:
            The direction to move ("L" or "R")
        '''    
        return self.direction

