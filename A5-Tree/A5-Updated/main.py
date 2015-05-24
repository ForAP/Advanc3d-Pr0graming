import kivy
kivy.require('1.7.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from turingmachine import TuringMachine

Builder.load_file('toolbox.kv')
Builder.load_file('turingwidgets.kv')
Builder.load_file('drawingspace.kv')
Builder.load_file('statusbar.kv')
Builder.load_file('generaloptions.kv')
Builder.load_file('turingcreator.kv')
Builder.load_file('aboutTMs.kv')
Builder.load_file('InstructionScreen.kv')
Builder.load_file('homescreen.kv')
Builder.load_file('topbox.kv')

class Main(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return Main()

if __name__=="__main__":
    MainApp().run()
