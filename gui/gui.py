#! /usr/bin/python3

 
from kivy.base import runTouchApp
from kivy.lang import Builder
import sys
sys.path.insert(1, 'app/my_sqlite3_v1.py')



runTouchApp(Builder.load_string("""

BoxLayout:
    orientation: 'vertical'
    BoxLayout:
        size_hint: 1, .15
        padding: 1
        canvas.before:
            Color:
                rgba: 0, 0, 0, 50
            Rectangle:
                size: self.size
                pos: self.pos

        Button:
            text: "Add User"
        Button:
            text: "Modify User"
        Button:
            text: "Add Menu"
        Button:
            text: "Modify Menu"
    BoxLayout:
        orientation: 'vertical'

        canvas.before:
            Color:
                rgba: 0, 0, 1, 1
            Rectangle:
                size: self.size
                pos: self.pos

        Label:
            text: "INFO DATABASE ICI"

    BoxLayout:
        size_hint: 1, 0.75

        GridLayout:
            size_hint: .7, 1
            padding: 1
            canvas.before:
                Color:
                    rgba: 1, 0, 0, 1


            cols: 3

            Button:
                text: "7"
            Button:
                text: "8"
            Button:
                text: "9"
            Button:
                text: "4"
            Button:
                text: "5"
            Button:
                text: "6"      
            
            Button:
                text: "1"
            Button:
                text: "2"
            Button:
                text: "3"      
                
                        
            Button:
                text: "Cancel"
            Button:
                text: "Enter"
            Button:
                text: "."






"""))
