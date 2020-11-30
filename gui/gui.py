#! /usr/bin/python3

 
import kivy
 
from kivy.app import App
from kivy.core.window import Window
 
Window.size = (1024, 768)
 
class GeneralLayout(App):
    def build(FloatLayout):
        pass
 
if __name__ == '__main__':
    GeneralLayout().run()