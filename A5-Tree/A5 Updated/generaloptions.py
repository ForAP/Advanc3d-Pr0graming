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
    group_mode = False
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

    def clear(self, instance):
        self.drawing_space.clear_widgets()

    def remove(self, instance):
        ds = self.drawing_space
        if len(ds.children) > 0:
            ds.remove_widget(ds.children[0])

    def group(self, instance, value):
        if value == 'down':
            self.group_mode = True
        else:
            self.group_mode = False
            self.unselect_all()

    def new_machine(self, instance):
        self.turing_creator.manager.current = 'titlescreen'

    def get_caption(self, instance):
        p = TapePopup()
        p.open()

    def newTM(self, alphabet, initialstate, initialtape, finalstates, blank):
        #TODO WE need to check the user's input (No spaces or what ever)
        tm = TuringMachine(alphabet, initialstate, initialtape, finalstates, blank)
        p = AlphabetPopup()
        p.open()

    def gestures(self, instance, value):
        pass

    def unselect_all(self):
        for child in self.drawing_space.children:
            child.unselect()

    def on_translation(self,instance,value):
        for child in self.drawing_space.children:
            if child.selected:
                child.translate(*self.translation)

class TapePopup(Popup):
    def get_caption(self, instance):
        p = AlphabetPopup()
        p.open()

class AlphabetPopup(Popup):
    pass
