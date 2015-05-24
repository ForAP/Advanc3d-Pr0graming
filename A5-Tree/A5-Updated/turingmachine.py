#!/usr/bin/python2
'''The core of the Turing Machine simulator:
Author:
    Robert Merkel <robert.merkel@monash.edu>
'''


import xml.etree.cElementTree as ET
import sys

from transition import Transition
from state import State
from tape import Tape


# experimental code, commented out.
##class noTransition(Exception):
##    '''Class to represent a
##    def __init__(self, state, symbol, tape):
##        self.state=state
##        self.symbol=symbol

class TuringMachine:
    '''Class to represent a Turing machine'''




    def __init__(self, alphabet, initialstate, initialtape, finalstates, blank):
        '''Construct a Turing machine

        Args:

            alphabet (str): The alphabet
            initialstate (str): The name of the initial state
            initialtape (str): The initial contents of the state
            finalstates (List): A list of the names of the final states
            blank (str): The blank symbol for this TM
        '''
        self.alphabet = alphabet
        self.initialstate = initialstate
        self.states = {}
        self.currentstate = self.initialstate
        self.tape = Tape(initialtape, blank)
        self.finalstates = finalstates
        self.halted = ''
        self.finaltape = ''

    def addstate(self, statename, state):
        '''Add a state to the TM
        Args:
            statename(str) : name of the state
            state(State) : the state
        '''

        self.states[statename] = state

    def set_alphabet_in_TM(self,alphabet):
        self.alphabet = alphabet

    def set_tape_in_TM(self, tape, blank):
        self.tape = Tape(tape, blank)

    def set_initialstate(self, _state):
        self.initialstate = _state
        self.currentstate = str(self.initialstate)

    def set_finalstates(self, _final):
        self.finalstates.add(_final)

    # def set_alphabet(self, alphabet):
    #     self.alphabet = alphabet
    #
    # def set_initialstate(self, initialstate):
    #     self.initialstate = initialstate
    #
    # def add_finalstate(self, statename):
    #     self.finalstates.append()

    def removestate(self, statename):
        '''Removes a state from the TM
        Args:
            statename(str) : name of the state
        '''
        del self.states[statename]

    def getstate(self):
        '''Get the current state

        Returns:
            str: the name of the current state
        '''
        return self.currentstate

    def gettape(self):
        '''Get the current tape as a string

        Returns:
            str: the current tape
        '''
        return self.tape.gettape()

    def step(self):
        '''Executes one execution step on the TM

        Returns:
            bool: False if there was no transition defined, True otherwise
        '''
        cursym = self.tape.getsym()
        state= self.states[self.currentstate]
        transition = state.get_transition(cursym)
       # print transition
        if transition is None:
            return False
        self.currentstate = transition.get_next_state()
        if (transition.get_next_direction() == "R"):
            self.tape.writeright(transition.get_write_sym())
        else:
            self.tape.writeleft(transition.get_write_sym())

        return True


def run_turing(filename):
    '''Loads and runs a Turing Machine As required by Assignment 1 spec

    Args:
        filename (str): Name of an XML file
    '''
    tm = parseTuringMachine(filename)
    tm.runtohalt()

if __name__ == "__main__":
    run_turing(sys.argv[1])
