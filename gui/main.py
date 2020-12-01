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


try:
    conn = sqlite3.connect(r'database/meals.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee")
    query_result = cursor.fetchall()
except sqlite3.Error as error:
    print("Error while reading from cursor : ", error)
print(query_result)

Window.size = (1024, 768)
Window.minimum_width, Window.minimum_height = Window.size

class AskId(Widget):
    def change_label_method(self):
        self.layout_widget.text = 'test'
        print('test')
        
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

    
if __name__ == "__main__":
    Meals().run()