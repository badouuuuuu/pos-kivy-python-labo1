

from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout

class PopUpShow(FloatLayout):
    
    def show_popup_unknown():
        show = PopUpShow() 

        popupWindow = Popup(
            title="Identifiant introuvable", 
            content=show, 
            size_hint=(None,None),
            size=(600,400),
            background = 'atlas://data/images/defaulttheme/button_pressed',
            background_color = (0,0,0.1,0.75),
            opacity = 1
                            ) 
        # Create the popup window

        popupWindow.open() # show the popup