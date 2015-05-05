'''Contains the State class for the Turing Machine Simulator.

Author:
    Robert Merkel <robert.merkel@monash.edu>
'''

from transition import Transition

class State:
    '''Represents a state within a Turing Machine.'''
    
    def __init__(self):
        '''Create a new State with no transitions defined'''
        self.transitions={}

    def add_transition(self, seensym, writesym, newstate, move):
        '''Add a transition to this state

        Args:
            seensym (char) : the symbol under the tape to trigger the transition
            writesym (char): the new symbol to write
            newstate (char): the name of the state to transition to
            move (char): the direction to move ("L" or "R")
        '''
        transition=Transition(writesym, newstate, move)
        self.transitions[seensym] = transition

    def get_transition(self, seensym):
        ''' Get the appropriate transition to follow when you see seensym

        Args:
            seensym (char): the symbol we have seen

        Returns:
            the appropriate transition, or None if no transition defined
        '''
        if seensym in self.transitions:
            return self.transitions[seensym]
        else:
            return None
