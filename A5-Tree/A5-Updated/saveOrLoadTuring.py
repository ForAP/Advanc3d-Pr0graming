__author__ = 'Fabrizio'
import glob
import os
import xml.etree.cElementTree as ET


"""When you call this class you must pass it the following:
            1) the Turing Machine Object
            2) The ds.children list"""


class Saver():


    def __init__(self, TM, drawing_space):
        self.TM = TM
        self.drawing_space = drawing_space

     ##This method will build a turing machine based on the current TM
    #### NEEDS THE turing machine object and the ds.children attributes
    def create_xml(self,name):

        turingmachine = self.TM

        #create the root and name it turingmachine
        root = ET.Element("turingmachine")
        #add alphebet as a subelement
        alphabet = ET.SubElement(root, "alphabet")
        #add an attribute to the alphabet
        alphabet.text = str(turingmachine.alphabet)


        #add as a subelement (remove the tape head from the tape to avoid crashing when loaded
        initialtape = ET.SubElement(root, "initialtape")
        initialtape.text = str(turingmachine.gettape().replace("*", ""))


        #### WILL MANUALLY SET (Blank char will always be 'b'
        blank = ET.SubElement(root, "blank")
        blank.set('char', 'b')

        initialstate = ET.SubElement(root, "initialstate")
        initialstate.set("name",str(turingmachine.initialstate))

        finalstates = ET.SubElement(root, "finalstates")

        #Will need a for loop here ---- Done!
        for x in turingmachine.finalstates:
            finalstate = ET.SubElement(finalstates,"finalstate")
            finalstate.set("name",str(x))

        states = ET.SubElement(root, "states")

        #Will need a for loop here ---- Done!
        for x in turingmachine.states:
            state = ET.SubElement(states, "state")
            state.set("name",str(x))

            #Will need a Nested for loop here ---- Done!
            for y in turingmachine.states.get(x).get_all_transition():
                transition= ET.SubElement(state, "transition")
                transition.set("move", turingmachine.states.get(x).get_all_transition()[y].get_next_direction())
                transition.set("newstate", turingmachine.states.get(x).get_all_transition()[y].get_next_state())
                transition.set("writesym", turingmachine.states.get(x).get_all_transition()[y].get_write_sym())
                transition.set("seensym",turingmachine.states.get(x).get_all_transition()[y].get_seen_sym())

        tree = ET.ElementTree(root)
        tree.write(open(r"../SavedTMs/%s" % name,'w'))


    def load_turing_machine(self,fileName):
        #parse the TM to a useable turing machine object
        turingMachine = self.TM.parseturing(fileName)

        #TODO ---- implement a parser that can get the DS children information

        # return turing machine object
        return turingMachine



    def get_state_rep_location(self,stateId):
        #increment the state ID for accessing list purposes
        id = stateId + 1
        #define ds to equal the drawing space
        ds = self.drawing_space
        #check is valid
        if self.check_id_valid_for_accessing_ds(id,ds) == True:
            return (ds.children[-id].get_local())

    def make_list_of_state_coordinates(self):
        ds = self.drawing_space

        