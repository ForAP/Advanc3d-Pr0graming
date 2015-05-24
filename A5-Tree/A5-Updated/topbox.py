import kivy
kivy.require('1.8.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup
import glob
import os
import xml.etree.cElementTree as ET
import saveOrLoadTuring


class TopBox(BoxLayout):
    # THIS INIT CREATES AND POPULATES THE DROP DOWN
    def __init__(self, *args, **kwargs):
        super(TopBox, self).__init__(*args, **kwargs)

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
        mainbutton = Button(text='Load TM', size_hint=(1, 1))
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
        dropdown.bind(on_select=lambda instance, x: self.load_turing_machine(getattr(x,'text',x)))


        self.add_widget(mainbutton)

    #this method updates the dropdown after a new file has been saved.
    def refresh_dropdown(self):

        dropdown = self.dropdown
        mainbutton = self.mainbutton
        dropdown.open

        self.remove_widget(mainbutton)
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
        mainbutton = Button(text='Load TM', size_hint=(1, 1))
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
        # dropdown.bind(on_select=lambda instance, x: self.load_turing_machine(getattr(x,'text',x)))
        #


        self.add_widget(mainbutton)

    def load_turing_machine(self, filename):
        #TODO ---- implement
        go = self.general_options
        go.newTM()
        go.parseTuringMachine(filename)


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
        self.refresh_dropdown()
        self.call_saving(fileName)
        print "We need to call the save xml method here and name is %s" % str(fileName)


    ####DAVE THIS IS THE METHOD THAT WILL CALL THE SAVING
    def call_saving(self, fileName):
        go = self.general_options
        ds = self.drawing_space
        tb = self.tool_box
        if go.nameCounter > 1:
            saveIt = saveOrLoadTuring.Saver(go, ds ,tb).create_xml(fileName)

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
