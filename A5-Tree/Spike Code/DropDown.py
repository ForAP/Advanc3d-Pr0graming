import kivy
kivy.require('1.8.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
import glob
import os

class HomeScreen(Screen):

    def __init__(self, *args, **kwargs):
        super(HomeScreen, self).__init__(*args, **kwargs)

        dropdown = DropDown()

        os.chdir("./SavedTMs/")
        turingMachines = []
        for file in glob.glob("*.xml"):
            turingMachines.append(str(file))

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

        # show the dropdown menu when the main button is released
        # note: all the bind() calls pass the instance of the caller (here, the
        # mainbutton instance) as the first argument of the callback (here,
        # dropdown.open.).
        mainbutton.bind(on_release=dropdown.open)
        #dd_btn.bind(on_release=dropdown.open)

        # one last thing, listen for the selection in the dropdown list and
        # assign the data to the button text.
        #dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
        #dropdown.bind(on_select=lambda instance, x: setattr(dd_btn, 'text', x))

        self.top_layout.add_widget(mainbutton)

    def printMeth(self):
        print "yo"



class dropdApp(App):

    def build(self):

        return HomeScreen()



if __name__ == '__main__':
    dropdApp().run()