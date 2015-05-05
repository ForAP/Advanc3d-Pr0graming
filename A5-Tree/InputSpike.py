__author__ = 'Fabrizio'

import kivy
from kivy.app import App
from kivy.uix.widget import Widget

class myWidget(Widget):
    def check(self):
        print" Enter has been Pressed"

    def keepInput(self,input):
        print "The input to the text box is: \n\t%s" % input

class mySecondWidget(Widget):
    pass

class inputSpikeApp(App):

    def build(self):
        self.first = myWidget()
        self.second = mySecondWidget()
        return self.first


if __name__ == '__main__':
    inputSpikeApp().run()


