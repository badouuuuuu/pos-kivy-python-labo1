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
        GeneralLayout = GridLayout(
            cols=4,
            row_force_default=True,
            row_default_height=40,  

            spacing= 20,
            padding=40
            )
        
        newlayout = GridLayout(
            
        )
        
        btn_addUser= Button(text='Add user')
        btn_modifyUser = Button(text='Modify user')
        btn_addMenu = Button(text='Add Menu')
        btn_modifyMenu = Button(text='Modify Menu')
        
        
        GeneralLayout.add_widget(btn_addUser)
        GeneralLayout.add_widget(btn_modifyUser)
        GeneralLayout.add_widget(btn_addMenu)
        GeneralLayout.add_widget(btn_modifyMenu)
        return GeneralLayout

MainApp().run()