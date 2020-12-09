import kivy
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.core.window import Window

Builder.load_file('Day_15.kv')
Window.size = (500,700)

class Calculator(Widget):
    def __init__(self):
        super().__init__()

    def clear(self):
        self.ids.calc_input.text = "0"

    def button_press(self,button):
        prior = self.ids.calc_input.text
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    def add(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}+'

    def equals(self):
        prior = self.ids.calc_input.text
        expression = prior.split('+')
        try:
            expression = list(map(int,expression))
            self.ids.calc_input.text = str(sum(expression))
        except ValueError:
            self.ids.calc_input.text = "Invalid Input"

class MyApp(App):
    def build(self):
        return Calculator()

if __name__=='__main__':
    MyApp().run()