#!/usr/bin/python2
'''The core of the Turing Machine simulator:
Author:
    Robert Merkel <robert.merkel@monash.edu>
'''


import xml.etree.ElementTree as ET
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
        
    def addstate(self,statename, state):
        '''Add a state to the TM
        Args:
            statename(str) : name of the state
            state(State) : the state
        '''
        
        self.states[statename] = state

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

    def runtohalt(self):
        '''Run the machine to completion.  Prints an execution trace
        Returns:
            nothing
        '''
        print "initial state=", self.currentstate
        print "initial tape=", self.gettape()
        print " "
        steps = 0
        while self.step():
            steps += 1
            print "steps = ", steps
            print "state = ", self.currentstate
            print "tape = ", self.gettape()
            print " "
        if self.currentstate in self.finalstates:
            print "halted with answer yes"
        else:
            print "halted with answer no"
            
            
def parseTuringMachine(infile):
    '''Parses a Turing machine from an XML file

    Args:
        infile(str): name of an XML input file
    Returns:
        A TuringMachine
    '''
    ep = ET.parse(infile)
    tm = ep.getroot()
  #  tm = etree.find('turingmachine')
    
    alpha=tm.find("alphabet").text
    tape=tm.find("initialtape").text
    blank=tm.find("blank").attrib['char']
    initialstate=tm.find("initialstate").attrib['name']

    finalstates=set()
    fs=tm.findall("finalstates/finalstate")
    for state in fs:
        finalstates.add(state.attrib['name'])

    tmobj = TuringMachine(alpha,initialstate, tape, finalstates, blank)
    
    states = tm.findall("states/state")

    for state in states:
        statename = state.attrib['name']
        stateobj = State()
        transitions = state.findall("transition")
        for transition in transitions:
            stateobj.add_transition(transition.attrib['seensym'],
                                    transition.attrib['writesym'],
                                    transition.attrib['newstate'],
                                    transition.attrib['move'])
        tmobj.addstate(statename, stateobj)
        
    
    return tmobj

def run_turing(filename):
    '''Loads and runs a Turing Machine As required by Assignment 1 spec

    Args:
        filename (str): Name of an XML file
    '''
    tm = parseTuringMachine(filename)
    tm.runtohalt()
    
if __name__ == "__main__":
    run_turing(sys.argv[1])
