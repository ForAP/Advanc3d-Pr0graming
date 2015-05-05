# File name: homescreen.py
import kivy
kivy.require('1.7.0')
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import sys
import turingmachine

#This is the first screen that comes up.
class HomeScreen(Screen):
    def endProgram(self):
        sys.exit()

    def newTM(self, alphabet, initialstate, initialtape, finalstates, blank):
        #TODO WE need to check the user's input (No spaces or what ever)
        print "Should show an instance of the turning machine object just below"
        tm = TuringMachine(alphabet, initialstate, initialtape, finalstates, blank)
        print tm


# #This screen gets input from the user.
# class GetInputScreenWidget(Widget):
#
#     def endProgram(self):
#             sys.exit()
#
#     def createNewTuringMachine(self,alphabet,tape,blankChar):
#         #TODO WE need to check the user's input (No spaces or what ever)
#         print "Should show an instance of the turning machine object just below"
#         tm = turingmachine.TuringMachine(str(alphabet), '1', str(tape), [], str(blankChar))
#         print tm
#
#     def checkValidXml(self,file):
#         #TODO implement this method
#         print "Checking XML"
#         if (str(file[-4:]) == ".xml"):
#             return True
#         else:
#             #TODO write some more code to tell the user that there has been an error
#             return False
#
#     def loadTuringMachine(self,file):
#         print "loading an xml file"
#             #error Check the xml and make sure that the path is correct.
#             #call the parse method from the Turing machine
#         tm = turingmachine.parseTuringMachine(file)
#         print tm
#             #TODO we will now need to call a method to build the visual representation of the Turing Machine
#
# class ActionScreenWidget(Widget):
#     #TODO add in more code like drag and drop etc
#     pass
#
#
# """This class just builds our Widget, takes App as arguments"""
# class HomeScreenApp(App):
#     def build(self):
#         self.homeScreen = HomeScreenWidget()
#         self.inputScreen = GetInputScreenWidget()
#         self.actionScreen = ActionScreenWidget()
#         return self.homeScreen
#
#
# if __name__ == '__main__':
#     HomeScreenApp().run()
