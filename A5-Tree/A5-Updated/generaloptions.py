# File name: generaloptions.py
import kivy
kivy.require('1.7.0')
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.properties import NumericProperty, ListProperty
from turingmachine import TuringMachine
import time

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
    transInfo = []
    transitionCounter = 0

    ##This method will change the color of states, it uses negative indices.  Just pass it the ID of the state that you
    # want changes and it will display it as a start/initial state!
    def change_state_color_to_initial(self,stateId):
        #increment the state ID for accessing list purposes
        id = stateId + 1
        #define ds to equal the drawing space
        ds = self.drawing_space

        #check is valid
        if self.check_id_valid_for_accessing_ds(id,ds) == True:
            ds.children[-id-self.transitionCounter].change_color_please("green")
    ##This method will change the color of states, it uses negative indices.  Just pass it the ID of the state that you
    # want changes and it will display it as a final/accepting state!
    def change_state_color_to_final(self,stateId):
        #increment the state ID for accessing list purposes
        id = stateId + 1
        #define ds to equal the drawing space
        ds = self.drawing_space

        #check is valid
        if self.check_id_valid_for_accessing_ds(id,ds) == True:
            ds.children[-id].change_color_please("red")
    ##Checks that the state ID that was passed in is a valid ID and it is actually part of the list. If not no action
    # will be taken
    def check_id_valid_for_accessing_ds(self,id,ds):
        #checks the length and makes sure that the requested state exists
        if len(ds.children) > 0 and id <= len(ds.children):
            return True
        else:
            return False

    def get_state_rep_location(self,stateId):
        #increment the state ID for accessing list purposes
        id = stateId + 1
        #define ds to equal the drawing space
        ds = self.drawing_space
        #check is valid
        if self.check_id_valid_for_accessing_ds(id,ds) == True:
            return (ds.children[-id].get_local())

    def add_state(self, state):
        self.tm.addstate(str(self.nameCounter), state)
        self.nameCounter += 1

        print "HELLO"

        ##TODO Remove below line THESE ARE FOR TESTING PURPOSES [ SEE HERE DAVE ]
        #Here are a few methods that I whacked together. Just have a look. They are only activated when a new touch is called
        #You can change the trigger or at least we should. (The base methods are in the turingwidgets.py class. but these can
        #be called from anywhere
        # self.change_state_color_to_final(3)
        # self.change_state_color_to_initial(0)
        # #There is also a highlight method in turingWidgets.py but I haven't implemented one for generaloptions yet.
        # self.get_state_rep_location(1)
        # print self.get_state_rep_location(4)
        #Also still need to be able to change the states back after we change the color etc... just need to edit the color in the code..



    def run_tm(self, instance):
        '''Run the machine to completion.  Prints an execution trace
        Returns:
            nothing
        '''
        print "initial state=", self.tm.currentstate
        print "initial tape=", self.tm.gettape()
        print " "
        steps = 0
        sb = self.parent.status_bar
        if sb.paused == True:
            self.step_tm()
            return
        while self.tm.step():
            steps += 1
            print "steps = ", steps
            print "state = ", self.tm.currentstate
            print "tape = ", self.tm.gettape()
            print " "
        if int(self.tm.currentstate) in self.tm.finalstates:
            self.halted = "halted with answer yes"
        else:
            self.halted = "halted with answer no"
        self.finaltape = self.tm.gettape()
        sb.finished(self.halted, self.finaltape)

    # This method will be called to step though a turing machine --- Still to implement
    def step_tm(self):
        #TODO : still need to write the method in the turingMachine.py and call it below.
        sb = self.parent.status_bar
        if self.tm.step() == True:
            sb.stepthrough(self.tm.currentstate, self.tm.gettape())
        else:
            if int(self.tm.currentstate) in self.tm.finalstates:
                self.halted = "halted with answer yes"
            else:
                self.halted = "halted with answer no"
            sb.finished(self.tm.halted, self.tm.finaltape)

    # def clear(self, instance):
    #     self.drawing_space.clear_widgets()

    def set_alphabet(self,alphabet):
        self.tm.set_alphabet_in_TM(alphabet)

    def set_tape(self,tape):
        self.tm.set_tape_in_TM(tape)


    def collect_trans_info(self,value,counter,current_state_name):
        self.transInfo.append(value)
        if counter == 4:
            print "Here we have to actually add the transitions"
            # self.tm.states[current_state_name]
            self.parent.tool_box.tool_transition.draw_transition(current_state_name, self.transInfo, self.transitionCounter)
            self.tm.states[current_state_name].add_transition(self.transInfo[0],self.transInfo[1],self.transInfo[2],self.transInfo[3])
            self.transInfo = []
            self.transitionCounter += 1

            print "NOW PRINTING THE LIST"

            for x in self.transInfo:
                print x
            #add_transition(self, seensym, writesym, newstate, move)


    #This class removes the last State to be made (Pops it if you think like a stack data structure)
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

        #HERE WE ADD IN CHARACTER TO THE TM depending on the tape input

        copyOfTape = "".join(set(self.initialtape))
        copyOfTape = sorted(copyOfTape)
        copyOfAlphabet = sorted(self.alphabet)
        for x in copyOfTape:
             if x not in copyOfAlphabet:
                copyOfAlphabet.append(x)
                # we added a new character to the alphabet

        stringAlphabet = "".join(copyOfAlphabet)
        self.tm.set_alphabet_in_TM(stringAlphabet)
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
        self.transInfo = []
        self.updateTM()
        self.transitionCounter = 0
        # p = AlphabetPopup()
        # p.open()

    def unselect_all(self):
        for child in self.drawing_space.children:
            child.unselect()

    def on_translation(self,instance,value):
        dsc = self.drawing_space.children
        for child in dsc:
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

    #get the input of the user input.
    def grabInputFromTape(self, tape):
        #remove the spaces
        tape = tape.replace(" ", "")
        #set everything to lowerCase
        tape = tape.lower()
        #check against the alphabet
        #TODO: get the actualy alphabet


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
