#! /usr/bin/python3

# Import 
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

# Fenetre general
Window.size = (1024, 768)
Window.minimum_width, Window.minimum_height = Window.size
Window.clearcolor = (0,0,0.3,0.1)

class MainApp(App):
    def build(self):
        layout = GridLayout(
            cols=4,
            row_force_default=True,
            row_default_height=40,  

            spacing= 20,
            padding=40
            )
        btn = Button(text='Button 1')
        btn2 = Button(text='Button 2')
        btn3 = Button(text='Button 3')
        btn4 = Button(text='Button 4')
        
        layout.add_widget(btn)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        return layout

MainApp().run()