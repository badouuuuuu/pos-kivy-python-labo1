#! /usr/bin/python3

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup


class PopUpShow(FloatLayout):

    def add_user():
        show = PopUpShow() 

        popupWindow = Popup(
            title="Ajouter un employée", 
            content=show, 
            size_hint=(None,None),
            size=(600,400),
            background = 'atlas://data/images/defaulttheme/button_pressed',
            background_color = (0,0,0.1,0.75),
            opacity = 1
                            ) 
        # Create the popup window

        popupWindow.open() # show the popup