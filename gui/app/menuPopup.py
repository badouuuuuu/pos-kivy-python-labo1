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
        name = self.ids.label_name.text
        email = self.ids.label_email.text
        family = self.ids.label_familyname.text
    
        if name == '' or email == '' or family == '':
            print('pas de champs vide')
        else:
            popupWindow = Popup(
            title='Enregistré', 
            content=Label(text=f"Ajouté au registre\n"), 
            size_hint=(None,None),
            size=((400,200)),
            background = 'atlas://data/images/defaulttheme/button_pressed',
            background_color = (0,0,0.1,0.75),
            opacity = 1,
                                ) 
            popupWindow.open()
            confirm = 'y'
            add_employee(name, family, email, confirm)
            self.ids.label_name.text = ''
            self.ids.label_email.text = ''
            self.ids.label_familyname.text = ''

    
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
        
        


class PopUpShow2(BoxLayout):

    value = []
    
    def __init__(self, **kwargs):
        super(PopUpShow2, self).__init__(**kwargs)
        self.ids.label_email2.text = ''
        self.ids.label_familyname2.text = ''
        self.ids.label_name2.text = ''

    def popup_modifyuser(self):
        name = self.ids.label_name2.text
        email = self.ids.label_email2.text
        family = self.ids.label_familyname2.text
    
        if name == '' or email == '' or family == '':
            print('pas de champs vide')
        else:
            popupWindow = Popup(
            title='Enregistré', 
            content=Label(text=f"Ajouté au registre\n"), 
            size_hint=(None,None),
            size=((400,200)),
            background = 'atlas://data/images/defaulttheme/button_pressed',
            background_color = (0,0,0.1,0.75),
            opacity = 1,
                                ) 
            popupWindow.open()
            confirm = 'y'
            add_employee(name, family, email, confirm)
            self.ids.label_name2.text = ''
            self.ids.label_email2.text = ''
            self.ids.label_familyname2.text = ''

    
    def backPopup(self):
        self.ids.label_email2.text = ''
        self.ids.label_familyname2.text = ''
        self.ids.label_name2.text = ''
        
    def show_popup_unknown():
        show = PopUpShow2() 

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
        show = PopUpShow2() 

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
        show = PopUpShow2() 

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
        show = PopUpShow2() 

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