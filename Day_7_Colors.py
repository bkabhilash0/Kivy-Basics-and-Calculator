import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty

Builder.load_file("Day_7.kv")

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