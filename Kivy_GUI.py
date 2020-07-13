#############################################################################
# Filename    : Kivy_GUI.py
# Description : Prova software per interfaccia grafica
# Author      : Andrea
# Date        : 13 July 2020
# Revision    : R0
# note        : Inizio codifica per l'interfaccia grafica
########################################################################
# Importo le librerie che mi interessano
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# Definisco le classi che mi servono
class MyGrid(GridLayout):                                                                                               #definisco la classe per la costruzione del layout della mia GUI
    def __init__(self, **kwargs):                                                                                       #**kwargs non mi pone limiti hai caratteri che inserisco
        super(MyGrid, self).__init__(**kwargs)                                                                          #genera la griglia generale
        self.cols = 1

        self.inside = GridLayout()                                                                                      # genera una griglia all'interno della griglia pricipale
        self.inside.cols = 2


        self.inside.add_widget(Label(text='First Name: '))
        self.firstname = TextInput(multiline=False)
        self.inside.add_widget(self.firstname)

        self.inside.add_widget(Label(text='Last Name: '))
        self.lastname = TextInput(multiline=False)
        self.inside.add_widget(self.lastname)

        self.inside.add_widget(Label(text='Email: '))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text='Submit', font_size=40,)                                                              #classe per quando si preme un bottone
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        #print("pressed")
        name = self.firstname.text
        last = self.lastname.text
        email = self.email.text

        print("Name:", name, "Last name:", last, "Email:", email)
        self.firstname.text = ''
        self.lastname.text = ''
        self.email.text = ''


class MyApp(App):
    def build(self):
        #return Label(text='Hello world')
        return MyGrid()

# Definisco le funzioni che mi servono



# Main proram
if __name__ == "__main__":
    MyApp().run()