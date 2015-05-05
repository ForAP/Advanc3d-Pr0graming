__author__ = 'Fabrizio'
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
import turingmachine

class ScreenWidget(Widget):

    def createTuringMachine(self,*args):
        label = self.ids['create_New_Turing_Machine']
        tm = turingmachine.parseTuringMachine("test4-blank-in-middle.xml")
        label.text = "Yieeew"
        print tm



    def printSomething(self):
        print "Good Afternoon, This is just a test method \n\tYou should see this printed in Idle if it was done\n\t\tCorrectly"





class ScreenApp(App):
    def build(self):

        return ScreenWidget()




