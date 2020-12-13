#! /usr/bin/python3

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty, ListProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.scrollview import ScrollView
# from app.getFunction import getEmployee, getMenuList
from app.meals_management_v1 import add_employee
from kivy.uix.recycleview import RecycleView 


class PopUpShow(BoxLayout):

    value = []
    
    def __init__(self, **kwargs):
        super(PopUpShow, self).__init__(**kwargs)
        self.ids.label_email.text = ''
        self.ids.label_familyname.text = ''
        self.ids.label_name.text = ''
    
    
    def popup_adduser(self):

        self.value.append(self.ids.label_email.text)
        self.value.append(self.ids.label_familyname.text)
        self.value.append(self.ids.label_name.text)
        
        print(self.value)
        name = self.value[2]
        email = self.value[0]
        family = self.value[1]
        confirm = 'y'
        add_employee(name, family, email, confirm)

    
    def backPopup(self):
        self.ids.label_email.text = ''
        self.ids.label_familyname.text = ''
        self.ids.label_name.text = ''
        
    def show_popup_unknown():
        show = PopUpShow() 

        popupWindow = Popup(
            title='', 
            content=show, 
            size_hint=(None,None),
            size=(600,400),
            background = 'atlas://data/images/defaulttheme/button_pressed',
            background_color = (0,0,0.1,0.75),
            opacity = 1,
            
                            ) 
        # Create the popup window
    def show_popup_askid():
        show = PopUpShow() 

        popupWindow = Popup(
            title='Votre id est inconnu', 
            content=Label(text="Cet utilisateur n'existe pas"), 
            size_hint=(None,None),
            size=(600,400),
            background = 'atlas://data/images/defaulttheme/button_pressed',
            background_color = (0,0,0.1,0.75),
            opacity = 1,
            
                            ) 
        # Create the popup window
        popupWindow.open() # show the popup
        
    def show_popup_nomenu():
        show = PopUpShow() 

        popupWindow = Popup(
            title='Menu inexistant', 
            content=Label(text="Le menu n'existe pas"), 
            size_hint=(None,None),
            size=(600,400),
            background = 'atlas://data/images/defaulttheme/button_pressed',
            background_color = (0,0,0.1,0.75),
            opacity = 1,
            
                            ) 
        # Create the popup window
        popupWindow.open() # show the popup
        
        
    def ErrorMessage():
        show = PopUpShow() 

        popupWindow = Popup(
            title='Menu inexistant', 
            content=Label(text="Veuillez n'encoder qu'un seul chiffre a la fois"), 
            size_hint=(None,None),
            size=(600,400),
            background = 'atlas://data/images/defaulttheme/button_pressed',
            background_color = (0,0,0.1,0.75),
            opacity = 1,
            
                            ) 
        # Create the popup window
        popupWindow.open() # show the popup