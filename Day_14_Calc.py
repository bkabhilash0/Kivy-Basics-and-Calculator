from kivy.uix.widget import Widget
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (500,700)
Builder.load_file("Day_14_Calc.kv")

class Calculator(Widget):
    def __init__(self):
        super().__init__()
    
    def clear(self):
        self.ids.calc_input.text = "0"

class MyApp(App):
    def build(self):
        return Calculator()

if __name__=='__main__':
    MyApp().run()