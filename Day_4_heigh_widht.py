import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

class MyGridLayout(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.row_force_default = True
        self.col_force_default = True
        self.row_default_height = 120
        self.col_default_width = 100

        self.top_grid = GridLayout(
            row_force_default = True,
            col_force_default = True,
            row_default_height = 40,
            col_default_width = 140
        )
        self.top_grid.cols = 2

        self.top_grid.add_widget(Label(text="Name"))
        self.name = TextInput(multiline=False)
        self.top_grid.add_widget(self.name)

        self.top_grid.add_widget(Label(text="Favourite Pizza"))
        self.pizza = TextInput(multiline=False)
        self.top_grid.add_widget(self.pizza)

        self.top_grid.add_widget(Label(text="Favourite Color"))
        self.color = TextInput(multiline=False)
        self.top_grid.add_widget(self.color)

        self.add_widget(self.top_grid)

        self.submit = Button(text="Submit",
        size_hint_x=None,
        size_hint_y=None,
        width=200,
        height=50)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self,instance):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        self.add_widget(Label(text=f"Hello {name}! You like {pizza} and ur fav colour is {color}."))

        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()