import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file("Day_5.kv")

class MyGridLayout(Widget):
    name = ObjectProperty()
    pizza = ObjectProperty()
    color = ObjectProperty()

    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        print(f"Hello {name}! You like {pizza} and ur fav colour is {color}.")

        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()
