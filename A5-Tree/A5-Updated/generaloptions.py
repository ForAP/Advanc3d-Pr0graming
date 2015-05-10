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
    translation = ListProperty(None)
    alphabet = ''
    initialstate = ''
    initialtape = ''
    finalstates = set()
    blank = ''
    tm = TuringMachine(alphabet, initialstate, initialtape, finalstates, blank)
    nameCounter = 0


    def add_state(self, state):
        self.tm.addstate(str(self.nameCounter), state)
        self.nameCounter += 1
        print state

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

    def new_machine(self, instance):
        self.turing_creator.manager.current = 'titlescreen'

    def get_caption(self, instance):
        popup = AlphabetPopup()
        popup.bind(on_dismiss=self.my_callback)
        popup.open()
        p = TapePopup()
        p.bind(on_dismiss=self.my_callback)
        p.open()
        print self.initialtape

    def my_callback(instance):
        self.initialtape = instance.getInfo()
        print self.initialtape
        # self.tm = TuringMachine(self.alphabet, self.initialstate, self.initialtape, self.finalstates, self.blank)
        # print('Popup', instance, 'is being dismissed but is prevented!')
        return False

    def newTM(self, instance):
        #TODO WE need to check the user's input (No spaces or what ever)
        self.alphabet = ''
        self.initialstate = ''
        self.initialtape = ''
        self.finalstates = set()
        self.blank = ''
        self.tm = TuringMachine(self.alphabet, self.initialstate, self.initialtape, self.finalstates, self.blank)
        self.drawing_space.clear_widgets()
        self.nameCounter = 0
        # p = AlphabetPopup()
        # p.open()

    def unselect_all(self):
        for child in self.drawing_space.children:
            child.unselect()

    def on_translation(self,instance,value):
        for child in self.drawing_space.children:
            if child.selected:
                child.translate(*self.translation)

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
        alphabet = "01b"

        ####### We will sort the alphebet, eliminate all duplicated variables from a copy of tape, then compare the two
        copyOfTape = "".join(set(tape))
        copyOfTape = sorted(copyOfTape)
        copyOfAlphabet = sorted(alphabet)
        print "This is the tape:\t" + tape
        initialtape = str(tape)

        for x in copyOfTape:
            if x not in copyOfAlphabet:
                print "It is not a match"
                return IOError
        print "It is a match"
        Match = True
        return tape

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
