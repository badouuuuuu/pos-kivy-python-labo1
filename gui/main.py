#! /usr/bin/python3

import kivy
import sqlite3
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

from app.meals_management_v1 import get_id_list, get_employee_name, get_employee_id

'''
try:
    conn = sqlite3.connect(r'database/meals.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee")
    query_result = cursor.fetchall()
except sqlite3.Error as error:
    print("Error while reading from cursor : ", error)
print(query_result)
'''

Window.size = (1024, 768)
Window.minimum_width, Window.minimum_height = Window.size
Window.borderless = True
id = None

# Get Employee List on startup
employee_list = get_id_list('employee')

for list in employee_list:
    print(list)
    print(get_employee_name(list))
        
        
class PopUpShow(FloatLayout):
    def show_popup_unknown():
        show = PopUpShow() # Create a new instance of the P class 

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


class AskId(Widget):

    def change_label_method(self):
        show = PopUpShow() # Create a new instance of the P class 

        self.layout_widget.text = '0'

        if id == None:
            PopUpShow.show_popup_unknown()
            print('id nok')
        else:
            print('id ok')
    def deleteLine(self, **kwargs):
        print('Delete Line')

class MyGridLayout(Widget):
    def add_user(self):
        print('Add User')
    # Mise en place de class, mise au propre du fichier gui.py
    
    def modify_user(self):
        print('Modify User')
        
    def add_menu(self):
        print('Add menu')
    
    def modify_menu(self):
        print('Modify menu')

class Meals(App):
    def build(self):
        return AskId()
    
class ExampleApp(App):
    def Pressbtn(self, instance):
        instance.parent.ids.lobj.text = str(instance)
        instance.parent.ids.ltext.text = instance.text
        instance.parent.ids.lid.text= self.get_id(instance)

    def get_id(self,  instance):
        for id, widget in instance.parent.ids.items():
            if widget.__self__ == instance:
                return id
    
if __name__ == "__main__":
    Meals().run()