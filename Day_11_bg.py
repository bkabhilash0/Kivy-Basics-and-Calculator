import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget

Builder.load_file("Day_11.kv")

class MyLayout(Widget):
    pass

class MyApp(App):
    def build(self):
        Window.clearcolor = (174/255, 235/255, 223/255,1)
        return MyLayout()

if __name__=='__main__':
    MyApp().run()   