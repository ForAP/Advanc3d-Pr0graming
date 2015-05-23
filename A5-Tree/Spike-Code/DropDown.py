import kivy
kivy.require('1.8.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup
import glob
import os
import xml.etree.cElementTree as ET

###########FOR TESTING DUE TO REMOVE############
import turingmachine
from turingmachine import parseTuringMachine



class topBar(Screen):



    ##This method will build a turing machine based on the current TM
    #### NEEDS THE turing machine object and the ds.children attributes to be added
    def create_xml(self,name):

        ###############TESTING################## TODO - Remove the below line
        turingmachine = parseTuringMachine("../SavedTMs/flipper.xml")

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






        myList = [[0,1],[2,4],[3,6]]
        drawingSpace = ET.SubElement(root, "ds.children")
        for x in myList:
            state_coordinates = ET.SubElement(drawingSpace, "state_coordinates")
            state_coordinates.set("ID", "need to get")
            state_coordinates.set("x", str(x[0]))
            state_coordinates.set("y", str(x[1]))
















        tree = ET.ElementTree(root)
        tree.write(open(r"../SavedTMs/%s" % name,'w'))

    # THIS INIT CREATES AND POPULATES THE DROP DOWN
    def __init__(self, *args, **kwargs):
        super(topBar, self).__init__(*args, **kwargs)

        dropdown = DropDown()
        self.dropdown = dropdown

        os.chdir("./SavedTMs/")
        turingMachines = []
        for file in glob.glob("*.xml"):
            turingMachines.append(str(file))

        #Check that there is a file to load, if not display "No saved Files"
        if len(turingMachines) == 0:
            # the size_hint_y) so the dropdown can calculate the area it needs.
            btn = Button(text="No Saved Files", size_hint_y=None, height=30)
            # then add the button inside the dropdown
            dropdown.add_widget(btn)

        for tms in turingMachines:
            # when adding widgets, we need to specify the height manually (disabling
            # the size_hint_y) so the dropdown can calculate the area it needs.
            btn = Button(text='%s' % tms, size_hint_y=None, height=30)

            # for each button, attach a callback that will call the select() method
            # on the dropdown. We'll pass the text of the button as the data of the
            # selection.
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))

            # then add the button inside the dropdown
            dropdown.add_widget(btn)

        # create a big main button
        mainbutton = Button(text='Load Turing Machine', size_hint=(1, 1))
        print 'load Turing Machine has been selected'
        self.mainbutton = mainbutton

        # show the dropdown menu when the main button is released
        # note: all the bind() calls pass the instance of the caller (here, the
        # mainbutton instance) as the first argument of the callback (here,
        # dropdown.open.).
        mainbutton.bind(on_release=dropdown.open)
        #dd_btn.bind(on_release=dropdown.open)

        # one last thing, listen for the selection in the dropdown list and
        # assign the data to the button text.
        #dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

        # USE THE BELOW CODE TO CALL METHODS FROM THIS CLASS
        dropdown.bind(on_select=lambda instance, x: self.printMeth(getattr(x,'text',x)))


        self.top_layout.add_widget(mainbutton)

    #this method updates the dropdown after a new file has been saved.
    def refresh_dropdown(self):

        dropdown = self.dropdown
        mainbutton = self.mainbutton
        dropdown.open

        self.top_layout.remove_widget(mainbutton)
        dropdown.clear_widgets()

        turingMachines = []
        for file in glob.glob("*.xml"):
            turingMachines.append(str(file))

        #Check that there is a file to load, if not display "No saved Files"
        if len(turingMachines) == 0:
            # the size_hint_y) so the dropdown can calculate the area it needs.
            btn = Button(text="No Saved Files", size_hint_y=None, height=30)
            # then add the button inside the dropdown
            dropdown.add_widget(btn)

        for tms in turingMachines:
            # when adding widgets, we need to specify the height manually (disabling
            # the size_hint_y) so the dropdown can calculate the area it needs.
            btn = Button(text='%s' % tms, size_hint_y=None, height=30)

            # for each button, attach a callback that will call the select() method
            # on the dropdown. We'll pass the text of the button as the data of the
            # selection.
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))

            # then add the button inside the dropdown
            dropdown.add_widget(btn)

        # create a big main button
        mainbutton = Button(text='Load Turing Machine', size_hint=(1, 1))
        print 'load Turing Machine has been selected'
        self.mainbutton = mainbutton

        # show the dropdown menu when the main button is released
        # note: all the bind() calls pass the instance of the caller (here, the
        # mainbutton instance) as the first argument of the callback (here,
        # dropdown.open.).
        mainbutton.bind(on_release=dropdown.open)
        #dd_btn.bind(on_release=dropdown.open)

        # one last thing, listen for the selection in the dropdown list and
        # assign the data to the button text.
        #dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))


        # USE THE BELOW CODE TO CALL METHODS FROM THIS CLASS
        # Commented out as there is no need for a second binding as the __init__ already did it!
        #dropdown.bind(on_select=lambda instance, x: self.printMeth(getattr(x,'text',x)))


        self.top_layout.add_widget(mainbutton)

    #This is a test method to show you how to call the selected name
    def printMeth(self,b):
        print "yo\n\n ()()()()() YOU CAN CALL THE tm.parseTuring(%s) Here " % b

    def load_turing_machine(self,fileName):
        #TODO ---- implement
        #tm.parseturing(filename)

        pass

    #calls the pop up to be triggered
    def save_file(self, instance):
        p = SavePopup()
        p.bind(on_dismiss=self.save_callback)
        p.open()

    #typical call back that also triggers creation of a new XML file and the refreshing of the xml file
    def save_callback(self, instance):
        fileName = instance.getInfo()
        # strip out the spaces
        fileName = fileName.replace(" ", "")
        # add the .xml on the end
        fileName = fileName + ".xml"
        self.create_xml(fileName)
        self.refresh_dropdown()
        print "We need to call the save xml method here and name is %s" % str(fileName)

class SavePopup(Popup):
    fileName = '.xml'
    def getInfo(self):
        return self.fileName

    def grabInputFromTape(self, fileName):
        #Test the user input for irregular input
        # strip out the spaces
        fileName.replace(" ", "")
        # eliminate all duplicate characters
        self.fileName = fileName


class dropdApp(App):

    def build(self):

        return topBar()



if __name__ == '__main__':
    dropdApp().run()