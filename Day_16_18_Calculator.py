from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.app import App
from kivy.core.window import Window

Window.size = (500,700)
Builder.load_file('Day_16.kv')

class Calculator(Widget):
    def __init__(self):
        super().__init__()

    def clear(self):
        self.ids.calc_input.text = "0"
    
    def button_press(self,n):
        prior = self.ids.calc_input.text
        if prior == '0':
            self.ids.calc_input.text = str(n)
        else:
            self.ids.calc_input.text = f'{prior}{n}'
        
    def math_sign(self,sign):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}{sign}'

    def dot(self):
        prior = self.ids.calc_input.text
        num_list = prior.split('+')
        if "+" in prior and "." not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior
        elif "." in prior:
            pass
        else:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior

    def remove(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = prior[:-1]

    def pos_neg(self):
        prior = self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-","")}'
        else:
            self.ids.calc_input.text = f'-{prior}'

    def equals(self):
        expr = self.ids.calc_input.text
        answer = 0
        if "+" in expr:
            try:
                # expr = map(float,expr.split('+'))
                # total = sum(expr)
                # self.ids.calc_input.text = str(total)
                answer = eval(expr)
                self.ids.calc_input.text = str(answer)
            except Exception as e:
                self.ids.calc_input.text = "Invalid Input!"
                # print(e.args)

class MyApp(App):
    def build(self):
        return Calculator()
    
if __name__=='__main__':
    MyApp().run()