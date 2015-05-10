# File name: generaloptions.py
import kivy
kivy.require('1.7.0')
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.properties import NumericProperty, ListProperty
from turingmachine import TuringMachine
from transition import Transition
from state import State

class GeneralOptions(BoxLayout):
    set_state = False
    final_states = False
    add_transitions = False
    translation = ListProperty(None)
    alphabet = ''
    initialstate = ''
    initialtape = ''
    finalstates = set()
    blank = 'b'
    tm = TuringMachine(alphabet, initialstate, initialtape, finalstates, blank)
    nameCounter = 0


    def add_state(self, state):
        self.tm.addstate(str(self.nameCounter), state)
        self.nameCounter += 1
        print self.tm.states

    def run_tm(self, instance):
        self.tm.runtohalt()
        self.statusbar.finished(self.tm.halted, self.tm.finaltape)

    # def clear(self, instance):
    #     self.drawing_space.clear_widgets()

    def set_alphabet(self,alphabet):
        self.tm.set_alphabet_in_TM(alphabet)

    def set_tape(self,tape):
        self.tm.set_tape_in_TM(tape)

    def remove(self, instance):
        ds = self.drawing_space
        if len(ds.children) > 0:
            print ds.children[0].stateName
            self.tm.removestate(str(ds.children[0].stateName))
            ds.remove_widget(ds.children[0])
            self.nameCounter -= 1

    def set_initialstate(self, instance, value):
        if value == 'down':
            self.set_state = True
        else:
            self.set_state = False

    def set_finalstates(self, instance, value):
        if value == 'down':
            self.final_states = True
        else:
            self.final_states = False

    def new_machine(self, instance):
        self.turing_creator.manager.current = 'titlescreen'

    def set_initialtape(self, instance):
        p = TapePopup()
        p.bind(on_dismiss=self.tape_callback)
        p.open()
        popup = AlphabetPopup()
        popup.bind(on_dismiss=self.alphabet_callback)
        popup.open()

    def tape_callback(self, instance):
        self.initialtape = instance.getInfo()
        self.tm.set_alphabet_in_TM(self.alphabet)
        self.tm.set_tape_in_TM(self.initialtape, self.blank)
        return False

    def alphabet_callback(self, instance):
        self.alphabet = instance.getInfo()
        print self.alphabet
        return False


    def newTM(self, instance):
        #TODO WE need to check the user's input (No spaces or what ever)
        self.alphabet = ''
        self.initialstate = ''
        self.initialtape = ''
        self.finalstates = set()
        self.blank = 'b'
        self.drawing_space.clear_widgets()
        self.nameCounter = 0
        self.updateTM()
        # p = AlphabetPopup()
        # p.open()

    def unselect_all(self):
        for child in self.drawing_space.children:
            child.unselect()

    def on_translation(self,instance,value):
        for child in self.drawing_space.children:
            if child.selected:
                child.translate(*self.translation)

    def updateTM(self):
        self.tm = TuringMachine(self.alphabet, self.initialstate, self.initialtape, self.finalstates, self.blank)

    def test(self):
        print self.alphabet
        print self.tm.states
        print self.tm.gettape()

class TapePopup(Popup):
    initialtape = ''
    def getInfo(self):
        return self.initialtape

    def grabInputFromTape(self, tape):
        #remove the spaces
        tape = tape.replace(" ", "")
        #set everything to lowerCase
        tape = tape.lower()
        #check against the alphabet
        #TODO: get the actualy input

        ####### We will sort the alphebet, eliminate all duplicated variables from a copy of tape, then compare the two
        # copyOfTape = "".join(set(tape))
        # copyOfTape = sorted(copyOfTape)
        # copyOfAlphabet = sorted(alphabet)
        # print "This is the tape:\t" + tape
        self.initialtape = str(tape)

        # for x in copyOfTape:
        #     if x not in copyOfAlphabet:
        #         print "It is not a match"
        #         return IOError
        # print "It is a match"
        # Match = True
        # return tape

class AlphabetPopup(Popup):
    alphabet = ''
    def getInfo(self):
        return self.alphabet

    def grabInputFromTape(self, alphabet):
        #Test the user input for irregular input
        # strip out the spaces
        alphabet.replace(" ", "")
        # eliminate all duplicate characters
        alphabet = "".join(set(alphabet))
        self.alphabet = alphabet.lower()

class TransitionPopup(Popup):
    pass
