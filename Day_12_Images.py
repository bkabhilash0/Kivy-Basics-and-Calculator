import kivy
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file("Day_12.kv")

class MyLayout(Widget):
    pass

class MyApp(App):
    def build(self):
        Window.clearcolor = (118/255, 232/255, 173/255,1)
        return MyLayout()

if __name__=='__main__':
    MyApp().run()