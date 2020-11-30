#! /usr/bin/python3

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.widget import Widget

Window.size = (1024, 768)
Window.minimum_width, Window.minimum_height = Window.size


class MyGridLayout(Widget):
        print('Labo 1 - App General ')
        # Mise en place de class, mise au propre du fichier gui.py

class Meals(App):
    def build(self):
        return MyGridLayout()

    
if __name__ == "__main__":
    Meals().run()