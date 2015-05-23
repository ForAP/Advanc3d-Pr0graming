__author__ = 'Fabrizio'
import glob
import os
import xml.etree.cElementTree as ET


"""When you call this class you must pass it the following:
            1) the Turing Machine Object
            2) The ds.children list
            3) the name counter from generaloptions.py"""

class Saver():


    def __init__(self, TM, drawing_space,nameCounter):
        self.TM = TM
        self.drawing_space = drawing_space
        self.nameCounter = nameCounter

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







        #### NOW ADD IN THE COORDINATES AND NAMES OF EACH STATE UNDER ds.children tag

        drawingSpace = ET.SubElement(root, "ds.children")
        for x in self.make_list_of_state_coordinates():
            state_coordinates = ET.SubElement(drawingSpace, "state_coordinates")
            state_coordinates.set("ID", str(x[2]))
            state_coordinates.set("x", str(x[0]))
            state_coordinates.set("y", str(x[1]))


        # parse to a tree and export to an xml file
        tree = ET.ElementTree(root)
        tree.write(open(r"./SavedTMs/%s" % name,'w'))


    def load_turing_machine(self,fileName):
        #parse the TM to a useable turing machine object
        turingMachine = self.TM.parseturing(fileName)

        #TODO ---- implement a parser that can get the DS children information

        # return turing machine object
        return turingMachine


    #this method returns a list of length 3 [x coord, y coord, ID number of state]
    def get_state_rep_location(self,stateName,object):

        #define ds to equal the drawing space
        ds = self.drawing_space
        #check is valid

        final = (object.get_local())
        final.append(stateName)
        return final




    #this method returns a list of lists that are of length 3 [x coord, y coord, ID number of state]
    def make_list_of_state_coordinates(self):
        print "calling the make list of state coord"
        ds = self.drawing_space

        #cut out the transitions
        ID = self.nameCounter - 1

        print str(ID)

        #need to get all the ID's
        # then call the below
        full_list = []


        for x in ds.children:
            print type(x)
            if str(type(x)) == "<class 'turingwidgets.StateRep'>":
                print "It is a state object"
                full_list.append(self.get_state_rep_location(ID,x))
                ID = ID - 1
            else:
                print "It is a transition, you need to write a method to get the details from transition"

        print full_list
        return full_list


    ##Checks that the state ID that was passed in is a valid ID and it is actually part of the list. If not no action
    # will be taken
    def check_id_valid_for_accessing_ds(self,id,ds):
        #checks the length and makes sure that the requested state exists
        if len(ds.children) > 0 and id <= len(ds.children):
            return True
        else:
            return False