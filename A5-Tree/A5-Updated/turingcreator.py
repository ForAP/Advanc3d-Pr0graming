import kivy
kivy.require('1.7.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from turingmachine import TuringMachine

Builder.load_file('toolbox.kv')
Builder.load_file('turingwidgets.kv')
Builder.load_file('drawingspace.kv')
Builder.load_file('generaloptions.kv')
Builder.load_file('statusbar.kv')
Builder.load_file('turingcreator.kv')
Builder.load_file('homescreen.kv')

class TuringScreenManager(ScreenManager):
    def newTM(self, alphabet, initialstate, initialtape, finalstates, blank):
        #TODO WE need to check the user's input (No spaces or what ever)
        print "Should show an instance of the turning machine object just below"
        tm = TuringMachine(alphabet, initialstate, initialtape, finalstates, blank)
        print tm
class TuringScreenManagerApp(App):
    def build(self):
        return TuringScreenManager()
if __name__=="__main__":
    TuringScreenManagerApp().run()
