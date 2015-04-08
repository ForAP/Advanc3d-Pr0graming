__author__ = "O'Keeffe"
import xml.etree.cElementTree as ET

# import necessary libraries
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty

# class for add XML form
class XMLApp(App):
    pass

class MakeXML(BoxLayout):
    xml_input = ObjectProperty()

    def save_xml(self):
        print("The user searched for '{}'".format(self.xml_input.text))
        root = ET.Element('root')
        child = ET.Element('child')
        root.append(child)
        child.attrib['name'] = self.xml_input.text
        file = open("test.xml", 'w')
        ET.ElementTree(root).write(file)
        file.close()

# run the MakeXML App with the .run() command
if __name__ == "__main__":
    XMLApp().run()
