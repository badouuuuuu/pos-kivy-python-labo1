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
from app.meals_management_v1 import add_employee, modify_employee, add_menu, modify_menu, get_id_list
from kivy.uix.recycleview import RecycleView 


class PopUpShowAddMenu(BoxLayout):
    def popup_addmenu(self):
        new_menu_description = self.ids.label_menu_add_description.text
        new_menu_price = self.ids.label_menu_add_price.text
     
    
        if new_menu_description == '' or new_menu_price == '':
            print('pas de champs vide')
        else:
            popupWindow = Popup(
            title='Enregistré', 
            content=Label(text=f"Menu a été registre\n"), 
            size_hint=(None,None),
            size=((400,200)),
            background = 'atlas://data/images/defaulttheme/button_pressed',
            background_color = (0,0,0.1,0.75),
            opacity = 1,
                                ) 
            popupWindow.open()
            add_menu(new_menu_description, new_menu_price)
            
            self.ids.label_menu_add_description.text = ''
            self.ids.label_menu_add_price.text = ''
            
            

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
            content=Label(text="Le menu n'existe pas"), 
            size_hint=(None,None),
            size=(600,400),
            background = 'atlas://data/images/defaulttheme/button_pressed',
            background_color = (0,0,0.1,0.75),
            opacity = 1,
            
                            ) 
        # Create the popup window
        popupWindow.open() # show the popup
        
        
class PopShowModifyMenu(ScrollView):

    def popup_modifymenu(self):
    
        id_to_change = self.ids.label_idmodify.text
        new_description = self.ids.label_menu_modify_description.text
        new_price = self.ids.label_menu_modify_price.text
        
        if new_description == '' or new_price == '' or id_to_change == '':
            popupWindowNoInfo = Popup(
            title="Erreur", 
            content=Label(text="Menu inexistant / info manquante"),
            size_hint=(None,None),
            size=((400,200)),
            background = 'atlas://data/images/defaulttheme/button_pressed',
            background_color = (0,0,0.1,0.75),
            opacity = 1,
                                ) 
            popupWindowNoInfo.open()
        else:
            popupWindow = Popup(
            title="Modification du menu", 
            content=Label(text=f"Le menu : #{id_to_change}\na bien été modifié\n{new_description} - {new_price}"),
            size_hint=(None,None),
            size=((400,200)),
            background = 'atlas://data/images/defaulttheme/button_pressed',
            background_color = (0,0,0.1,0.75),
            opacity = 1,
                                ) 
            popupWindow.open()

            modify_menu(id_to_change, new_description, new_price)
            
            self.ids.label_idmodify.text = ''
            self.ids.label_menu_modify_description.text = ''
            self.ids.label_menu_modify_price.text = ''

class PopUpShow2(BoxLayout):

    value = []
    
    def __init__(self, **kwargs):
        super(PopUpShow2, self).__init__(**kwargs)
        self.ids.label_email2.text = ''
        self.ids.label_familyname2.text = ''
        self.ids.label_name2.text = ''

    def popup_modifyuser(self):
        id_to_change = self.ids.label_idmodify.text
        new_firstname = self.ids.label_name2.text
        new_email = self.ids.label_email2.text
        new_familyname = self.ids.label_familyname2.text
    
        if new_firstname == '' or new_email == '' or new_familyname == '':
            print('pas de champs vide')
        else:
            popupWindow = Popup(
            title="Modification d'employé", 
            content=Label(text=f"'L'utilisateur : {id_to_change} \n a bien été modifié'\n"), 
            size_hint=(None,None),
            size=((400,200)),
            background = 'atlas://data/images/defaulttheme/button_pressed',
            background_color = (0,0,0.1,0.75),
            opacity = 1,
                                ) 
            popupWindow.open()
            modify_employee(id_to_change, new_firstname, new_familyname, new_email)
            confirm = 'y'
            
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