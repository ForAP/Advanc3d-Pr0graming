__author__ = 'Fabrizio'


# import necessary libraries
from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

#class for the Spike_zoomApp
class Spike_ZoomApp(App):
    def build(self):
        float = FloatLayout() # define the float layout (enables a dynamic screen)
        scatt = Scatter() # create a scatter
        scattTwo = Scatter() # create a second scatter
        but = Button(text="test", # create a button with large font size
                      background_color=(0,.5,0,1),
                      font_size=150)
        butTwo = Button() # create a button with no font

        float.add_widget(scatt) # add the first scatter
        float.add_widget(scattTwo) # add the second scatter
        scatt.add_widget(but) # add the first button to the first scatter
        scattTwo.add_widget((butTwo)) # add the second button to the second scatter

        return float # return the float layout

# run the Spike_zoom App with the .run() command
if __name__ == "__main__":
    Spike_ZoomApp().run()