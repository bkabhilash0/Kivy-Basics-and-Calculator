import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file("Day_13.kv")

class MyLayout(Widget):
    def __init__(self):
        super().__init__()
    
    pass
class MyApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return MyLayout()

if __name__=='__main__':
    MyApp().run()